import React from 'react';
import CloseIcon from '@material-ui/icons/Close';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import {red} from '@material-ui/core/colors';


class ParaChute extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            chuteData: this.props.initState,
            errors: new Set(),
        };
        this.state.chuteData['customName'] = '';
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
                const chuteData = this.state.chuteData;
                this.setState({errors, chuteData: {...chuteData, [name]: value}});
                return;
            }
        } catch (e) {
            const errors = new Set(this.state.errors);
            errors.add(name);
            const chuteData = this.state.chuteData;
            this.setState({errors, chuteData: {...chuteData, [name]: value}});
            return;
        }
        const errors = new Set(this.state.errors);
        errors.delete(name);
        const chuteData = {...this.state.chuteData, [name]: parsedValue};
        this.setState({chuteData, errors});
        this.props.changeChute(chuteData)
    }


    render() {
        const {chuteData, errors} = this.state;
        const {
            deleteChute,
        } = this.props;
        return (
            <Paper className={this.props.styles.chuteBG}>
                <Grid container wrap="nowrap">
                    <Grid item>
                        <TextField
                            name="customName"
                            label={chuteData.customName ? 'Name' : chuteData.name}
                            type="text"
                            variant="outlined"
                            style={{margin: 10}}
                            value={chuteData.customName}
                            onChange={this.changeHandler}

                        />
                    </Grid>
                    <Grid item>
                        <Button onClick={deleteChute} style={{padding: 10, marginTop: 10}}>

                            <CloseIcon style={{color: red[500]}}/>

                        </Button>
                    </Grid>
                </Grid>


                <TextField
                    error={errors.has('A_max')}
                    name="A_max"
                    label="a [m²]"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.A_max}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    error={errors.has('cw')}
                    name="cw"
                    label="drag coefficient"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.cw}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    error={errors.has('openingHeight')}
                    name="openingHeight"
                    label="opening height [m]"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.openingHeight}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    error={errors.has('cutHeight')}
                    name="cutHeight"
                    label="cut height [m]"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.cutHeight}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    error={errors.has('openingDelay')}
                    name="openingDelay"
                    label="opening delay [s]"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.openingDelay}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    error={errors.has('openingDuration')}
                    name="openingDuration"
                    label="opening duration [s]"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={this.changeHandler}
                    value={chuteData.openingDuration}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
            </Paper>
        );
    }
}

export default ParaChute;