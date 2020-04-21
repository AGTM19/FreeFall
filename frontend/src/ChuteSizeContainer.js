import React from 'react';
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";
import Slider from "@material-ui/core/Slider";
import Paper from "@material-ui/core/Paper";
import VolumeDown from '@material-ui/icons/VolumeDown';
import VolumeUp from '@material-ui/icons/VolumeUp';


class ChuteSizeContainer extends React.Component {
    constructor(props) {
        super(props);
        this.cw_min = 0.1;
        this.cw_max = 4;
        this.changeHandler = this.changeHandler.bind(this);
        this.a_max = this.a_max.bind(this);
        this.a_min = this.a_min.bind(this);

        this.state = {
            cw: this.cw_max,
            a: null,
            g: 9.807,
            v: 80,
            rho: 1.184,
            mass: 60,
            a_max: 1,
            a_min: 2,
            errors: new Set()
        };

        const {mass, g, rho, v} = this.state;
        this.state.a_min = this.a_min(mass, g, rho, v, this.cw_max);
        this.state.a_max = this.a_max(mass, g, rho, v, this.cw_min);
        this.state.a = this.state.a_min;
        window.round = this.round;
    }

    round(num) { // https://stackoverflow.com/a/11832950/3080611
        return Math.round(num * 1000) / 1000;
    }

    a_min(mass, g, rho, v, cw_max){
        return ((2 * mass * g) / (rho * v * v * cw_max))
    }

    a_max(mass, g, rho, v, cw_min){
        return ((2 * mass * g) / (rho * v * v * cw_min))
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
        const {a, cw, g, v, rho, mass} = {...this.state, [name]: parsedValue};
        const errors = new Set(this.state.errors);
        errors.delete(name);
        const toBeUpdated = {[name]: parsedValue, errors};
        if (name === "a") {
            toBeUpdated['cw'] = ((2 * mass * g) / (rho * v * v * a));
        } else if (name === "cw") {
            toBeUpdated['a'] = ((2 * mass * g) / (rho * v * v * cw));
        } else {
            toBeUpdated['a_max'] = this.a_max(mass, g, rho, v, this.cw_min);
            toBeUpdated['a_min'] = this.a_min(mass, g, rho, v, this.cw_max);
            toBeUpdated['a'] = ((2 * mass * g) / (rho * v * v * cw));
            console.log(`a range: {${toBeUpdated['a_min']},${toBeUpdated['a_max']}}`)
        }
        this.setState(toBeUpdated)
    }


    render() {
        const {errors} = this.state;
        return (
         <Paper style={{padding: 20}}>
                <div>
                <Typography variant="h5" style={{marginBottom: 8}}>Chute Size Calculator</Typography>
                <div style={{flexGrow: 1}}>


                    <Grid container
                          direction="column"
                          alignItems="flex-start"
                    >
                        <TextField
                            name="v"
                            label="velocity [m/s]"
                            type="number"
                            variant="outlined"
                            error={errors.has('v')}
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.v}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="mass"
                            label="mass [kg]"
                            type="number"
                            variant="outlined"
                            error={errors.has('mass')}
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.mass}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="g"
                            label="g [m/s²]"
                            type="number"
                            variant="outlined"
                            error={errors.has('g')}
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.g}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="rho"
                            label="rho [kg/m³]"
                            type="number"
                            variant="outlined"
                            error={errors.has('rho')}
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.rho}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />

                        <div style={{width: 200, marginLeft: 20}}>
                            {<Typography gutterBottom>
                                {/*a = {this.round(this.state.a)}*/}
                                a [m²]
                            </Typography>}
                            <Grid container spacing={2}>

                                <Grid item xs>
                                    <Slider name="a"
                                            value={this.state.a}
                                            min={this.state.a_min}
                                            max={this.state.a_max}
                                            step={0.01}
                                            onChange={(x, newVal) => this.changeHandler(({
                                                target: {
                                                    name: 'a',
                                                    value: newVal
                                                }
                                            }))}/>
                                </Grid>

                            </Grid>
                            <TextField
                                name="a"
                                onChange={this.changeHandler}
                                /*label="a [m²]"*/
                                type="number"
                                variant="standard"
                                error={errors.has('a')}
                                style={{margin: 0}}
                                value={this.state.a}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                            />

                            <Typography gutterBottom style={{marginTop: 40}}>
                                {/*cw = {this.round(this.state.cw)}*/}
                                drag coefficient
                            </Typography>
                            <Grid container spacing={2}>

                                <Grid item xs>
                                    <Slider
                                        name="a"
                                        value={this.state.cw}
                                        min={this.cw_min}
                                        max={this.cw_max}
                                        step={0.01}
                                        onChange={(x, newVal) => this.changeHandler(({
                                            target: {
                                                name: 'cw',
                                                value: newVal
                                            }
                                        }))}
                                    />

                                </Grid>

                            </Grid>
                            <TextField
                                name="cw"
                                onChange={this.changeHandler}
                                type="number"
                                variant="standard"
                                error={errors.has('cw')}
                                style={{margin: 0}}
                                value={this.state.cw}
                                InputLabelProps={{
                                    shrink: true,
                                }}
                            />
                        </div>

                    </Grid>


                </div>


            </div>
         </Paper>
        )
    }
}

export default ChuteSizeContainer;