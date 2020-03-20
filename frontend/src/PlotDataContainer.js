import React from 'react';
import TextField from '@material-ui/core/TextField';


class PlotDataContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            ...this.props.initialConfig
        };
    }


    render() {
        const {
            onChange
        } = this.props;
        return (
            <div>
                <h1>Plot Configuration:</h1>
                <div className={this.props.styles.containerbg}>
                    <TextField
                        label="t_min"
                        type="number"
                        onChange={() => onChange(this.state)}
                        value={this.state.t_min}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        label="t_max"
                        type="number"
                        onChange={() => onChange(this.state)}
                        value={this.state.t_max}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                    <TextField
                        label="t_steps"
                        type="number"
                        onChange={() => onChange(this.state)}
                        value={this.state.t_steps}
                        InputLabelProps={{
                            shrink: true,
                        }}
                    />
                </div>
            </div>);
    }


}

export default PlotDataContainer;