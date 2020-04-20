import React from 'react';
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";


class ChuteSizeContainer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            cw: 0.9,
            a: 3.0,
            g: 9.807,
            v: 80,
            rho: 1.184,
            mass: 60,
        };

        this.changeHandler = this.changeHandler.bind(this);
    }

    round(num) { // https://stackoverflow.com/a/11832950/3080611
        return Math.round(num * 1000) / 1000;
    }

    changeHandler(event) {
        const {target: {name, value}} = event;
        const parsedValue = parseInt(value);
        this.setState({[name]: parsedValue});
        if (name === "a") {
            const mass = this.state.cw * this.state.a;
            this.setState({mass: this.round(mass)});
        }
        if (name === "mass" || name === "cw") {
            const a = this.state.mass / this.state.cw;
            this.setState({a: this.round(a)});
        }
    }


    render() {
        return (
            <div>
                <Typography variant="h5" style={{marginBottom: 8}}>Chute Size Calculator</Typography>
                <div style={{flexGrow: 1}}>


                    <Grid container
                          direction="column"
                          alignItems="flex-start"
                    >


                        <TextField
                            name="v"
                            label="speed"
                            type="number"
                            variant="outlined"
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.v}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="g"
                            label="g"
                            type="number"
                            variant="outlined"
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.g}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="rho"
                            label="rho"
                            type="number"
                            variant="outlined"
                            style={{margin: 10}}
                            onChange={this.changeHandler}
                            value={this.state.rho}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="a"
                            onChange={this.changeHandler}
                            label="a"
                            type="number"
                            variant="outlined"
                            style={{margin: 10}}
                            value={this.state.a}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="cw"
                            label="Widerstandsbeiwert"
                            type="number"
                            variant="outlined"
                            style={{margin: 10}}
                            value={Math.round(this.state.cw)}
                            onChange={this.changeHandler}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>

                </div>


            </div>)
    }
}

export default ChuteSizeContainer;