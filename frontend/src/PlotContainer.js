import React, { Component, useRef } from 'react';
import Plot from 'react-plotly.js';
import PlotDataContainer from "./PlotDataContainer";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";
import CircularProgress from "@material-ui/core/CircularProgress";
import PlotIcon from "@material-ui/icons/Assessment"
import RefreshIcon from "@material-ui/icons/Refresh"
import Typography from "@material-ui/core/Typography";

const labels = ["Horizontal Position [m]", "Height [m]", "Horizontal Velocity [m/s]", "Vertical Velocity [m/s]", "Horizontal acceleration [m/s²]", "Vertical acceleration [m/s²]"];
const titles = ["Horizontal Position", "Height", "Horizontal Velocity", "Vertical Velocity", "Horizontal Acceleration", "Vertical Acceleration"];


const linspace = (a, b, n) => {
    if (typeof n === "undefined") n = Math.max(Math.round(b - a) + 1, 1);
    if (n < 2) {
        return n === 1 ? [a] : [];
    }
    let i, ret = Array(n);
    n--;
    for (i = n; i >= 0; i--) {
        ret[i] = (i * b + (n - i) * a) / n;
    }
    return ret;
};

window.lins = linspace;

class PlotContainer extends React.Component {

    constructor(props) {
        super(props);

        this.myRef = React.createRef();

        this.scrollToRef = (ref) => {
            console.log(ref.current);
            window.myref = ref.current;
            window.scrollTo(0, ref.current.offsetTop - 100);
        };



        this.state = {
            plotConfig: this.props.initialConfig,
            plotData: [],
            t: [],
            loading: false,
            buttonLabel: 'show plots',
            buttonIcon: PlotIcon,
            error: null,
        };
    }

    changeState(update) {
        const plotConfig = {...this.state.plotConfig, ...update.plotConfig};// todo: here, plotconfig gets nested instead of replaced
        console.log(plotConfig);
        this.setState({plotConfig});
        this.props.update(plotConfig);
    }

    plot() {
        this.setState({loading: true, buttonLabel: 'refresh plots', buttonIcon: RefreshIcon, error: null, plotData: [], t:[]});
        this.props
            .solve()
            .then((result) => {
                if(!result.plotData || !result.t){
                    console.log(result);
                    throw Error('no plot data received')
                }
                const {t, plotData} = result;
                console.log(plotData.length);
                console.log(plotData[0].length);
                const x = plotData[0].map(x => isNaN(x) ? 1.111 : x);
                console.log(Math.min(...x));
                console.log(Math.max(...x));
                this.setState({plotData, t, loading: false, error: null});
                setTimeout(() => {
                    this.scrollToRef(this.myRef)
                }, 10)
            })
            .catch((err) => {
                this.setState({error: err && err.message ? err.message : 'could not load plots', loading: false});
            })
    }


    render() {
        const {
            t_max, t_min, t_steps
        } = this.state.plotConfig;
        const {
            plotData,
            loading,
        } = this.state;
        return (

            <div>
                <PlotDataContainer
                    styles={this.props.styles}
                    initialConfig={this.state.plotConfig}
                    onChange={(update) => this.changeState({plotConfig: {...this.state.plotConfig, ...update}})}
                />
                <div style={{margin: 10}}>
                    {/*<Typography variant="h5" style={{marginBottom: 8}}>Plots</Typography>*/}
                    {!loading &&
                    <Button
                        color="primary"
                        variant="contained"
                        onClick={() => this.plot()}
                        startIcon={<this.state.buttonIcon/>}
                    >
                        {this.state.buttonLabel}
                    </Button>

                    }
                    {/*<Button variant="outlined" color="primary" style={{marginLeft: 10}}>reset configuration</Button>*/}
                    {loading && <CircularProgress/>}
                    {this.state.error &&
                    <div><Typography color="error" variant="caption">Error: {this.state.error}</Typography></div>
                    }
                    {
                        !loading &&

                        <div style={{flexGrow: 1}}>
                            <Grid container
                                  direction="row"
                                  alignItems="flex-start"
                                  ref={this.myRef}
                            >


                                {
                                    plotData.map((plot, i) => {
                                        return (
                                            <Plot item xs={12} sm={4} md={3}
                                                  style={{margin:20}}
                                                  key={Math.random()}
                                                  data={plotData ? [
                                                      {
                                                          x: this.state.t,
                                                          y: plot,
                                                          type: 'scatter',
                                                          line: {color: 'rgb(85, 108, 214);', width: 2}
                                                      },

                                                  ] : []}
                                                  layout={{
                                                      title: titles[i],
                                                      showLegend: true,
                                                      yaxis: {
                                                          title: {
                                                              text: labels[i]
                                                          }
                                                      },
                                                      xaxis: {
                                                          title: {
                                                              text: 'Time [s]'
                                                          }
                                                      }
                                                  }}
                                            />
                                        )
                                    })
                                }

                            </Grid>

                        </div>
                    }

                </div>


            </div>
        );
    }


}


export default PlotContainer;