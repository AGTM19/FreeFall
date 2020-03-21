import React from 'react';
import TextField from '@material-ui/core/TextField';


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
                <h1>Rocket Configuration:</h1>
                <div className={this.props.styles.containerbg}>
                    <TextField
                        label="Masse der Rakete"
                        type="number"
                        onChange={e => this.changeState({ mass: e.target.value })}
                        value={rocketData.mass}
                    />
                    <TextField
                        label="pos_x"
                        type="number"
                        onChange={e => this.changeState({ pos_x: e.target.value })}
                        value={rocketData.pos_x}

                    />
                    <TextField
                        label="pos_y"
                        type="number"
                        onChange={e => this.changeState({ pos_y: e.target.value })}
                        value={rocketData.pos_y}

                    />
                    <TextField
                        label="vel_x"
                        type="number"
                        onChange={e => this.changeState({ vel_x: e.target.value })}
                        value={rocketData.vel_x}

                    />
                    <TextField
                        label="vel_y"
                        type="number"
                        onChange={e => this.changeState({ vel_y: e.target.value })}
                        value={rocketData.vel_y}
                    />
                </div>
            </div>);
    }


}

export default RocketDataContainer;