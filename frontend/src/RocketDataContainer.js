import React from 'react';
import TextField from '@material-ui/core/TextField';
import datamock from "./datamock";


class RocketDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.defaults = {
            ...datamock.rocket_default_config
        };
        this.state = {};
    }


    render() {
        return (
            <div>
                <h1>Rocket Configuration:</h1>
                <div className={this.props.styles.containerbg}>
                    <TextField
                        label="Masse der Rakete"
                        type="number"
                        defaultValue={this.defaults.mass}

                    />
                    <TextField
                        label="pos_x"
                        type="number"
                        defaultValue={this.defaults.pos_X}

                    />
                    <TextField
                        label="pos_y"
                        type="number"
                        defaultValue={this.defaults.pos_y}

                    />
                    <TextField
                        label="vel_x"
                        type="number"
                        defaultValue={this.defaults.vel_x}

                    />
                    <TextField
                        label="vel_y"
                        type="number"
                        defaultValue={this.defaults.vel_y}

                    />

                </div>
            </div>);
    }


}

export default RocketDataContainer;