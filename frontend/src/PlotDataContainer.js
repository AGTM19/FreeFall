import React from 'react';
import TextField from '@material-ui/core/TextField';


class PlotDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {};
    }


    render() {
        return (
            <div>
                <h1>Plot Configuration:</h1>
                <div className={this.props.styles.containerbg}>
                    <TextField
                        label="t_min"
                        type="number"
                        defaultValue="0"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        label="t_max"
                        type="number"
                        defaultValue="170"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        label="t_steps"
                        type="number"
                        defaultValue="10000"
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                </div>
            </div>);
    }


}

export default PlotDataContainer;