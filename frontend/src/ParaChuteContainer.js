import React from 'react';
import AddIcon from '@material-ui/icons/Add';
import Button from '@material-ui/core/Button';
import Grid from '@material-ui/core/Grid';

import ParaChute from "./ParaChute";
import datamock from "./datamock";


class ParaChuteContainer extends React.Component {
    constructor(props) {
        super(props);

        this.state = {
            chutes: []
        };
    }

    componentDidMount() {
        this.addChute()
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
            ...datamock.chute_default_config,
            name: `Chute ${chutes.length + 1}`,
        };
        chutes.push(chute);
        this.setState({chutes});
    }

    deleteChute(name) {
        const chutes = [...this.state.chutes];
        chutes.splice(chutes.findIndex(chute => chute.name === name), 1);
        this.setState({chutes});
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
                                    return (<Grid item key={chute.name}>
                                        <ParaChute styles={this.props.styles}
                                                   initState={chute}
                                                   deleteChute={() => this.deleteChute(chute.name)}
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