import React from 'react';

import {makeStyles} from "@material-ui/core/styles";
import ParaChuteContainer from './ParaChuteContainer.js'
import RocketDataContainer from "./RocketDataContainer";
import PlotContainer from "./PlotContainer";
import dataMock from "./datamock";
import PataChuteSolverRequests from './actions/ParachuteSolverRequests';


// https://material-ui.com/components/text-fields/
const useStyles = makeStyles(theme => ({
    newChuteButton: {
        marginLeft: theme.spacing(1),
        height: 200,
        width: 100,
        background: 'white'
    },
    containerbg: {
        margin: 30,
        backgroundColor: 'rgb(247,247,247)',
        borderRadius: 10,
        padding: 20,
    },
    chuteBG: {
        backgroundColor: 'rgb(252,252,252)',
        borderRadius: 10,
        width: 300,
        padding: 20,
        margin: 20,
    },
    newButton: {
        backgroundColor: 'rgb(252,252,252)',
        borderRadius: 10,
        padding: 20,
        margin: 20,
    },
    root: {
        padding: 100
    }
}));


export default function App() {
    const classes = useStyles();
    const solver = new PataChuteSolverRequests();

    let data = {
        rocketData: dataMock.rocket_default_config,
        chutes: [],
        plotData: dataMock.plot_default_config
    };


    const update = (update, requires_solve=true) => {
        data = {...data, ...update};
        if (!requires_solve){
            return;
        }
        console.log('requesting solve');
        solver.solve(1, 1)
            .then(res => {
                if (res.error) {
                    console.log('error on solve');
                    console.error(res.error);
                    return;
                }
                data.plotData = res.plotData;
                console.log('damn, I should have used state to rerender after data change!')
            })
            .catch((err) => console.error(err));
    };


    return (
        <div className={classes.root}>
            <RocketDataContainer
                styles={classes}
                initialConfig={data.rocketData}
                update={(x) => update({rocketData: x})}
            />

            <ParaChuteContainer
                styles={classes}
                update={(x) => update({chutes: x})}
                defaultChute={dataMock.chute_default_config}
            />
            <PlotContainer
                styles={classes}
                initialConfig={dataMock.plot_default_config}
                update={(x) => update({plotData: x}, false)}
                plotData={dataMock.plot1Data}
            />
        </div>
    );
}
