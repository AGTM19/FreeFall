import React from 'react';
import TextField from '@material-ui/core/TextField';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Slider from "@material-ui/core/Slider";


class PlotDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ...this.props.initialConfig
        };
    }

    changeState(update) {
        this.setState(update);
        this.props.onChange(update);
    }


    render() {
        return (

            <div>
                <Typography variant="h5" style={{marginBottom: 8}}>Plot Configuration</Typography>
                <div style={{flexGrow: 1}}>


                    <Grid container
                          direction="column"
                          alignItems="flex-start"
                          wrap="wrap"
                    >
                        <TextField item
                                   label="start time [s]"
                                   type="number"
                                   variant="outlined"
                                   style={{margin: 10}}
                                   value={this.state.t_min}
                                   onChange={e => this.changeState({t_min: parseInt(e.target.value)})}
                                   InputLabelProps={{
                                       shrink: true,
                                   }}
                        />
                        <TextField item
                                   label="end time [s]"
                                   type="number"
                                   variant="outlined"
                                   style={{margin: 10}}
                                   value={this.state.t_max}
                                   onChange={e => this.changeState({t_max: parseInt(e.target.value)})}
                                   InputLabelProps={{
                                       shrink: true,
                                   }}
                        />
                        <TextField item
                                   label="number of steps"
                                   type="number"
                                   variant="outlined"
                                   style={{margin: 10}}
                                   value={this.state.t_steps}
                                   onChange={e => this.changeState({t_steps: parseInt(e.target.value)})}
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