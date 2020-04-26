import React from 'react';
import TextField from '@material-ui/core/TextField';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";


class PlotDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ...this.props.initialConfig,
            errors: new Set(), //todo: add helperText Dict, so that we can display the user a warning when t_steps is too small
        };
        this.changeHandler = this.changeHandler.bind(this);
    }

    changeHandler(event) {
        const {target: {name, value}} = event;
        let parsedValue;
        try {
            parsedValue = parseFloat(value);
            if (isNaN(parsedValue)) {
                const errors = new Set(this.state.errors);
                errors.add(name);
                this.setState({errors, [name]: value});
                return;
            }
        } catch (e) {
            const errors = new Set(this.state.errors);
            errors.add(name);
            this.setState({errors, [name]: value});
            return;
        }
        const errors = new Set(this.state.errors);
        errors.delete(name);
        this.setState({[name]: value, errors});
        this.props.onChange({[name]:value})
    }


    render() {
        const {errors} = this.state;
        return (

            <div>
                <Typography variant="h5" style={{marginBottom: 8}}>Plot</Typography>
                <div style={{flexGrow: 1}}>


                    <Grid container
                          direction="column"
                          alignItems="flex-start"
                          wrap="wrap"
                    >
                        <TextField
                                   error={errors.has('t_min')}
                                   label="start time [s]"
                                   type="number"
                                   variant="outlined"
                                   name="t_min"
                                   style={{margin: 10}}
                                   value={this.state.t_min}
                                   onChange={this.changeHandler}
                                   InputLabelProps={{
                                       shrink: true,
                                   }}
                        />
                        <TextField
                                   label="end time [s]"
                                   error={errors.has('t_max')}
                                   type="number"
                                   name="t_max"
                                   variant="outlined"
                                   style={{margin: 10}}
                                   value={this.state.t_max}
                                   onChange={this.changeHandler}
                                   InputLabelProps={{
                                       shrink: true,
                                   }}
                        />
                        <TextField
                                   label="number of steps"
                                   error={errors.has('t_Steps')}
                                   type="number"
                                   name="t_steps"
                                   variant="outlined"
                                   style={{margin: 10}}
                                   value={this.state.t_steps}
                                   onChange={this.changeHandler}
                                   InputLabelProps={{
                                       shrink: true,
                                   }}
                        />
                    </Grid>


                </div>
            </div>);
    }


}

export default PlotDataContainer;