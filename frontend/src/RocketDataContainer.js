import React from 'react';
import TextField from '@material-ui/core/TextField';
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Paper from "@material-ui/core/Paper";


class RocketDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            rocketData: {...this.props.initialConfig}
        };
    }

    changeState(update){
        const rocketData = {...this.state.rocketData, ...update};
        this.setState({rocketData});
        this.props.update(rocketData)
    }


    render() {
        const rocketData = this.state.rocketData;
        return (
            <Paper style={{padding: 20}}>
                <div>
                <Typography variant="h5" style={{marginBottom: 8}}>
                Rocket Configuration
                </Typography>

                 <div style={{flexGrow: 1}}>


                    <Grid container
                      direction="column"
                      alignItems="flex-start"
                >
                    <TextField item
                               label="mass [kg]"
                               type="number"
                               variant="outlined"
                               style={{margin: 10}}
                               onChange={e => this.changeState({mass: parseFloat(e.target.value)})}
                               value={rocketData.mass}
                    />
                    <TextField item
                               label="x position [m]"
                               type="number"
                               variant="outlined"
                               style={{margin: 10}}
                               onChange={e => this.changeState({pos_x: parseFloat(e.target.value)})}
                               value={rocketData.pos_x}

                    />
                    <TextField item
                               label="y position [m]"
                               type="number"
                               variant="outlined"
                               style={{margin: 10}}
                               onChange={e => this.changeState({pos_y: parseFloat(e.target.value)})}
                               value={rocketData.pos_y}

                    />
                    <TextField item
                               label="x velocity [m/s]"
                               type="number"
                               variant="outlined"
                               style={{margin: 10}}
                               onChange={e => this.changeState({vel_x: parseFloat(e.target.value)})}
                               value={rocketData.vel_x}

                    />
                    <TextField item
                               label="y velocity [m/s]"
                               type="number"
                               variant="outlined"
                               style={{margin: 10}}
                               onChange={e => this.changeState({vel_y: parseFloat(e.target.value)})}
                               value={rocketData.vel_y}
                    />
                </Grid>

            </div>

            </div>
            </Paper>
        );
    }
}

export default RocketDataContainer;