import React from 'react';
import AddIcon from '@material-ui/icons/Add';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';

import ParaChute from "./ParaChute";


class ParaChuteContainer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            chutes: [],
            totalCreatedCount: 0,
            defaultChute: this.props.defaultChute,
        };
    }

    renderNewButton() {
        return (
                <Button
                    color="primary"
                    className={this.props.styles.newChuteButton}
                    onClick={() => this.addChute()}
                >
                    <div>
                        <AddIcon/>
                    </div>
                </Button>
        );
    }

    addChute() {
        const chutes = this.state.chutes;
        const chute = {
            ...this.state.defaultChute,
            uuid: this.state.totalCreatedCount,
            name: `Chute ${this.state.totalCreatedCount + 1}`,
        };
        chutes.push(chute);
        this.setState({chutes, totalCreatedCount: this.state.totalCreatedCount + 1});
        this.update(chutes)
    }

    deleteChute(uuid) {
        const chutes = [...this.state.chutes];
        chutes.splice(chutes.findIndex(chute => chute.uuid === uuid), 1);
        this.setState({chutes});
        this.update(chutes)
    }

    changeChute(uuid, newData) {
        const chutes = [...this.state.chutes];
        const chuteIdx = chutes.findIndex(chute => chute.uuid === uuid);
        chutes.splice(chuteIdx, 1, newData);
        this.setState({chutes});
        this.update(chutes)
    }

    update(chutes){
        this.props.update(chutes);
    }


    render() {
        const {
            chutes,
        } = this.state;
        return (
            <div><h1>Parachutes:</h1>
                <div className={this.props.styles.containerbg}>
                    <Grid container direction="row" justify="flex-start"
                          alignItems="flex-start">
                        {
                            chutes.map((chute) => {
                                    return (<Grid item key={chute.uuid}>
                                        <ParaChute styles={this.props.styles}
                                                   initState={chute}
                                                   changeChute={(newData) => this.changeChute(chute.uuid, newData)}
                                                   deleteChute={() => this.deleteChute(chute.uuid)}
                                        />
                                    </Grid>);
                                }
                            )
                        }
                        <Grid item xs>
                            {this.renderNewButton()}
                        </Grid>
                    </Grid>
                </div>
            </div>)
    }
}

export default ParaChuteContainer;