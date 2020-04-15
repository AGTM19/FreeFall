import React from 'react';
import TextField from '@material-ui/core/TextField';
import Grid from "@material-ui/core/Grid";
import {Paper} from "@material-ui/core";
import Typography from "@material-ui/core/Typography";


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
                               label="Mass"
                               type="number"
                               onChange={e => this.changeState({mass: e.target.value})}
                               value={rocketData.mass}
                    />
                    <TextField item
                               label="pos_x"
                               type="number"
                               onChange={e => this.changeState({pos_x: e.target.value})}
                               value={rocketData.pos_x}

                    />
                    <TextField item
                               label="pos_y"
                               type="number"
                               onChange={e => this.changeState({pos_y: e.target.value})}
                               value={rocketData.pos_y}

                    />
                    <TextField item
                               label="vel_x"
                               type="number"
                               onChange={e => this.changeState({vel_x: e.target.value})}
                               value={rocketData.vel_x}

                    />
                    <TextField item
                               label="vel_y"
                               type="number"
                               onChange={e => this.changeState({vel_y: e.target.value})}
                               value={rocketData.vel_y}
                    />
                </Grid>

            </div>

            </div>
        );
    }
}

export default RocketDataContainer;