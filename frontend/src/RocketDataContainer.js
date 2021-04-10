import React from 'react';
import TextField from '@material-ui/core/TextField';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";


class RocketDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rocketData: {...this.props.initialConfig},
            errors: new Set()
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
                const rocketData = this.state.rocketData;
                this.setState({errors, rocketData: {...rocketData, [name]: value}});
                return;
            }
        } catch (e) {
            const errors = new Set(this.state.errors);
            errors.add(name);
            const rocketData = this.state.rocketData;
            this.setState({errors, rocketData: {...rocketData, [name]: value}});
            return;
        }
        const errors = new Set(this.state.errors);
        errors.delete(name);
        const rocketData = {...this.state.rocketData, [name]: parsedValue};
        this.setState({rocketData, errors});
        this.props.update(rocketData)//todo: only if no errors. already done?!
    }


    render() {
        const {errors, rocketData} = this.state;
        return (
            <Paper style={{padding: 20}}>
                <div>
                    <Typography variant="h5" style={{marginBottom: 8}}>
                        Rocket Configuration
                    </Typography>

                    <div>


                        <Grid container
                              direction="column"
                              alignItems="flex-start"
                        >
                            <TextField
                                       error={errors.has('mass')}
                                       name="mass"
                                       label="mass [kg]"
                                       type="number"
                                       variant="outlined"
                                       style={{margin: 10}}
                                       onChange={this.changeHandler}
                                       value={rocketData.mass}
                                       InputLabelProps={{
                                           shrink: true,
                                       }}
                            />
                            <TextField
                                       label="x position [m]"
                                       error={errors.has('pos_x')}
                                       name="pos_x"
                                       type="number"
                                       variant="outlined"
                                       style={{margin: 10}}
                                       onChange={this.changeHandler}
                                       value={rocketData.pos_x}
                                       InputLabelProps={{
                                           shrink: true,
                                       }}

                            />
                            <TextField
                                       label="y position [m]"
                                       error={errors.has('pos_y')}
                                       name="pos_y"
                                       type="number"
                                       variant="outlined"
                                       style={{margin: 10}}
                                       onChange={this.changeHandler}
                                       value={rocketData.pos_y}
                                       InputLabelProps={{
                                           shrink: true,
                                       }}

                            />
                            <TextField
                                       name="vel_x"
                                       label="x velocity [m/s]"
                                       error={errors.has('vel_x')}
                                       type="number"
                                       variant="outlined"
                                       style={{margin: 10}}
                                       onChange={this.changeHandler}
                                       value={rocketData.vel_x}
                                       InputLabelProps={{
                                           shrink: true,
                                       }}

                            />
                            <TextField
                                       label="y velocity [m/s]"
                                       error={errors.has('vel_y')}
                                       name="vel_y"
                                       type="number"
                                       variant="outlined"
                                       style={{margin: 10}}
                                       onChange={this.changeHandler}
                                       value={rocketData.vel_y}
                                       InputLabelProps={{
                                           shrink: true,
                                       }}
                            />
                        </Grid>

                    </div>

                </div>
            </Paper>
        );
    }
}

export default RocketDataContainer;