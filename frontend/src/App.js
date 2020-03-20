import React from 'react';

import Typography from '@material-ui/core/Typography';
import {makeStyles} from "@material-ui/core/styles";
import ParaChuteContainer from './ParaChuteContainer.js'
import RocketDataContainer from "./RocketDataContainer";
import PlotContainer from "./PlotContainer";


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
    return (
        <div className={classes.root}>
            <RocketDataContainer styles={classes}/>

            <ParaChuteContainer
                styles={classes}
            />
            <PlotContainer styles={classes} />
        </div>
    );
}
