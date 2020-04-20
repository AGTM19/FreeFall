import React from 'react';
import CloseIcon from '@material-ui/icons/Close';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import Paper from '@material-ui/core/Paper';
import Grid from "@material-ui/core/Grid";
import { red } from '@material-ui/core/colors';


class ParaChute extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            chuteData: this.props.initState
        }
    }

    changeState(update) {
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
                <Grid container wrap="nowrap">
                    <Grid item>
                        <TextField

                            label="Name"
                            type="text"
                    variant="outlined"
                    style={{margin: 10}}
                            value={chuteData.name}
                            InputLabelProps={{
                                shrink: true,
                            }}
                        />
                    </Grid>
                    <Grid item>
                        <Button onClick={deleteChute} style={{padding: 10, marginTop: 10}} >

                            <CloseIcon style={{ color: red[500] }} />

                        </Button>
                    </Grid>
                </Grid>


                <TextField
                    label="A_max"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({A_max: parseInt(e.target.value)})}
                    value={chuteData.A_max}
                />
                <TextField
                    label="cw"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({cw: parseInt(e.target.value)})}
                    value={chuteData.cw}
                />
                <TextField
                    label="opening height"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({openingHeight: parseInt(e.target.value)})}
                    value={chuteData.openingHeight}
                />
                <TextField
                    label="cut height"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({cutHeight: parseInt(e.target.value)})}
                    value={chuteData.cutHeight}
                />
                <TextField
                    label="opening delay"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({openingDelay: parseInt(e.target.value)})}
                    value={chuteData.openingDelay}
                />
                <TextField
                    label="opening duration"
                    type="number"
                    variant="outlined"
                    style={{margin: 10}}
                    onChange={e => this.changeState({openingDuration: parseInt(e.target.value)})}
                    value={chuteData.openingDuration}
                />
            </Paper>
        );
    }
}

export default ParaChute;