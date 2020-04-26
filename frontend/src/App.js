import React from 'react';
import 'typeface-roboto';
import {makeStyles} from "@material-ui/core/styles";
import ParaChuteContainer from './ParaChuteContainer.js'
import RocketDataContainer from "./RocketDataContainer";
import PlotContainer from "./PlotContainer";
import dataMock from "./datamock";
import PataChuteSolverRequests from './actions/ParachuteSolverRequests';
import ChuteSizeContainer from "./ChuteSizeContainer";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import useMediaQuery from '@material-ui/core/useMediaQuery';
import logo from './logo.png';


// https://material-ui.com/components/text-fields/
const useStyles = makeStyles(theme => ({
    newChuteButton: {
        marginLeft: theme.spacing(1),
        height: 200,
        width: 100,
        background: 'white'
    },
    body: {
        borderRadius: 30,
        padding: 30,
        background: "rgb(248,248,248)",
        [theme.breakpoints.down('lg')]: {
            marginLeft: "5%",
            marginRight: "5%",
            marginTop: 10,
        },
        [theme.breakpoints.up('lg')]: {
            marginLeft: "20%",
            marginRight: "20%",
            marginTop: 50,
        },
    },

    chuteBG: {
        backgroundColor: 'rgb(252,252,252)',
        borderRadius: 10,
        width: 300,
        padding: 20,
        margin: 20,
        marginLeft: 0,
        marginTop: 0,
    },

}));


function App() { // todo: add method to set invalid input, so that we can disable the plot/replot button and show a hint
    // todo: add import export button, or default configs, and reset button?
    const classes = useStyles();
    const solver = new PataChuteSolverRequests();
    const isWide = useMediaQuery('(min-width:600px)');

    let data = {
        rocketData: dataMock.rocket_default_config,
        chutes: dataMock.initChutes,
        plotConfig: dataMock.plot_default_config
    };

    const solve = () => {
        return solver.solve(data.chutes, data.rocketData, data.plotConfig)
            .then(res => {
                if (!res || !res.body || res.body.plotData === undefined) {
                    console.error('error in received result.');
                    console.error(`res: ${res}`);
                }
                if (res.error) {
                    console.log('error on solve');
                    console.error(res.error);
                    throw res.err;
                }

                return {
                    'plotData': res.body.plotData,
                    't': res.body.t
                };
            })
    };


    const update = (update) => {
        data = {...data, ...update};
    };


    return (
        <div className={classes.body}>
            {/* There is already an h1 in the page, let's not duplicate it. */}
            <Typography variant={isWide ? "h1" : "h3"} style={{marginBottom: 40}}>
                <img src={logo} alt="logo" style={{width: 100, height: 100}}/> Parachutes
            </Typography>

            <Grid container
                  spacing={3}
            >

                  <Grid item={true}>
                    <Grid container={true} direction="row" spacing={2} wrap={isWide ? "nowrap" : "wrap"}>
                        <Grid item={true} sm={12} md={6} style={{}}>
                            <RocketDataContainer
                                styles={classes}
                                initialConfig={data.rocketData}
                                update={(x) => update({rocketData: x})}
                            />
                        </Grid>
                        <Grid item={true} sm={12} md={6} style={{}}>
                            <ChuteSizeContainer
                                styles={classes}
                            />
                        </Grid>
                    </Grid>
                </Grid>

                <Grid item={true} xs={12} sm={12}>
                    <ParaChuteContainer
                        styles={classes}
                        update={(x) => update({chutes: x})}
                        chutes={data.chutes}
                    />
                </Grid>

                <Grid>
                    <PlotContainer
                        styles={classes}
                        initialConfig={dataMock.plot_default_config}
                        update={(x) => update({plotConfig: x})}
                        solve={() => solve()}
                    />
                </Grid>









            </Grid>
        </div>
    );
}

export default App;