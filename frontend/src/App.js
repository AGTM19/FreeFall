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
        chutes: dataMock.initChutes,
        plotConfig: dataMock.plot_default_config
    };

    const solve = () => {
        return solver.solve(data.chutes, data.rocketData, data.plotData)
            .then(res => {
                if (res.error) {
                    console.log('error on solve');
                    console.error(res.error);
                    return;
                }
                data.plotData = res.body.plotData;
                return data.plotData;
            })
            .catch((err) => {
                console.error(err);
            });
    };



    const update = (update) => {
        data = {...data, ...update};
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
                chutes={data.chutes}
            />
            <PlotContainer
                styles={classes}
                initialConfig={dataMock.plot_default_config}
                update={(x) => update({plotData: x})}
                solve={() => solve()}
            />
        </div>
    );
}
