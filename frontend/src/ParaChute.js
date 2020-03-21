import React from 'react';
import CloseIcon from '@material-ui/icons/Close';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';


class ParaChute extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            chuteData: this.props.initState
        }
    }

    changeState(update){
        this.setState({chuteData: {...this.state.chuteData, ...update}});
        this.props.changeChute({...this.state.chuteData, ...update})
    }


    render() {
        const chuteData = this.state.chuteData;
        const {
            deleteChute,
        } = this.props;
        return (
            <Paper className={this.props.styles.chuteBG}>
                <TextField
                    label="Name"
                    type="text"
                    value={chuteData.name}
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
                    onChange={e => this.changeState({ A_max: e.target.value })}
                    value={chuteData.A_max}
                />
                <TextField
                    label="cw"
                    type="number"
                    onChange={e => this.changeState({ cw: e.target.value })}
                    value={chuteData.cw}
                />
                <TextField
                    label="opening height"
                    type="number"
                    onChange={e => this.changeState({ openingHeight: e.target.value })}
                    value={chuteData.openingHeight}
                />
                <TextField
                    label="cut height"
                    type="number"
                    onChange={e => this.changeState({ cutHeight: e.target.value })}
                    value={chuteData.cutHeight}
                />
                <TextField
                    label="opening delay"
                    type="number"
                    onChange={e => this.changeState({ openingDelay: e.target.value })}
                    value={chuteData.openingDelay}
                />
                 <TextField
                    label="opening duration"
                    type="number"
                    onChange={e => this.changeState({ openingDuration: e.target.value })}
                    value={chuteData.openingDuration}
                />
            </Paper>
        );
    }
}

export default ParaChute;