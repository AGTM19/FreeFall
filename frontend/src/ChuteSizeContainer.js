import React from 'react';
import Paper from "@material-ui/core/Paper";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import Grid from "@material-ui/core/Grid";


class ChuteSizeContaier extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            cw: 0.9,
            a_max: 3.0,
            mass: 60
        };

        this.changeHandler = this.changeHandler.bind(this);
    }

    round(num) { // https://stackoverflow.com/a/11832950/3080611
        return Math.round(num * 1000) / 1000;
    }

    changeHandler(event) {
        const {target: {name, value}} = event;
        this.setState({[name]: value});
        if (name === "a_max") {
            const mass = this.state.cw * this.state.a_max;
            this.setState({mass: this.round(mass)});
        }
        if (name === "mass" || name === "cw") {
            const a = this.state.mass / this.state.cw;
            this.setState({a_max: this.round(a)});
        }
    }


    render() {
        return (
            <div>
                <h1>Chute Size Calculator:</h1>
                <div style={{flexGrow: 1}}>


                    <Grid container
                          direction="column"
                          alignItems="flex-start"
                    >
                        <TextField
                            name="cw"
                            label="Widerstandsbeiwert"
                            type="number"
                            value={Math.round(this.state.cw)}
                            onChange={this.changeHandler}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="mass"
                            label="Mass"
                            type="number"
                            onChange={this.changeHandler}
                            value={this.state.mass}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                        <TextField
                            name="a_max"
                            onChange={this.changeHandler}
                            label="A_max"
                            type="number"
                            value={this.state.a_max}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>

                </div>


            </div>)
    }
}

export default ChuteSizeContaier;