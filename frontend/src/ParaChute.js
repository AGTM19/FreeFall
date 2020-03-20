import React from 'react';
import CloseIcon from '@material-ui/icons/Close';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';


class ParaChute extends React.Component {
    constructor(props) {
        super(props);
    }


    render() {
        const {name, A_max,cw,openingHeight,
            cutHeight,openingDelay,
            openingDuration,
        } = this.props.initState;
        const {
            deleteChute,
        } = this.props;
        return (
            <Paper className={this.props.styles.chuteBG}>
                <TextField
                    label="Name"
                    type="text"
                    defaultValue={name}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                  <span><Button color="primary" onClick={deleteChute}>
                <div>
                    <CloseIcon/>
                </div>
            </Button></span>
                <TextField
                    label="A_max"
                    type="number"
                    defaultValue={A_max}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    label="cw"
                    type="number"
                    defaultValue={cw}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    label="opening height"
                    type="number"
                    defaultValue={openingHeight}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    label="cut height"
                    type="number"
                    defaultValue={cutHeight}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                <TextField
                    label="opening delay"
                    type="number"
                    defaultValue={openingDelay}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
                 <TextField
                    label="opening duration"
                    type="number"
                    defaultValue={openingDuration}
                    InputLabelProps={{
                        shrink: true,
                    }}
                />
            </Paper>
        );
    }
}

export default ParaChute;