import React from 'react';
import Plot from 'react-plotly.js';
import PlotDataContainer from "./PlotDataContainer";
import Button from "@material-ui/core/Button";
import Grid from "@material-ui/core/Grid";

const labels =  ["Horizontal Position [m]", "Height [m]", "Horizontal Velocity [m/s]", "Vertical Velocity [m/s]", "Horizontal acceleration [m/s²]", "Vertical acceleration [m/s²]"]
const titles =  ["Horizontal Position", "Height", "Horizontal Velocity", "Vertical Velocity", "Horizontal Acceleration", "Vertical Acceleration"]


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
        this.state = {
            plotConfig: this.props.initialConfig,
            plotData: [],
        };
    }

    changeState(update) {
        const plotConfig = {...this.state.plotConfig, ...update};
        this.setState({plotConfig});
        this.props.update(plotConfig);
    }

    plot() {
        this.props
            .solve()
            .then((plotData) => {
                console.log(plotData.length);
                console.log(plotData[0].length);
                const x = plotData[0].map(x => isNaN(x) ? 1.111 : x);
                console.log(Math.min(...x));
                console.log(Math.max(...x));
                this.setState({plotData});
            });
    }


    render() {
        const {
            t_max, t_min, t_steps
        } = this.state.plotConfig;
        const plotData = this.state.plotData;
        return (

            <div>
                <PlotDataContainer
                    styles={this.props.styles}
                    initialConfig={this.state.plotConfig}
                    onChange={(update) => this.changeState(update)}
                />
                <div>
                    <h1>Plots</h1>
                    <span> <Button
                        color="primary"
                        onClick={() => this.plot()}
                    >solve</Button></span>

                    <div style={{flexGrow: 1}}>
                        <Grid container
                              direction="row"
                              alignItems="flex-start"
                        >


                            {
                                plotData.map((plot, i) => {
                                    return (
                                        <Plot item xs={12} sm={6} md={4}
                                            key={Math.random()}
                                            data={plotData ? [
                                                {
                                                    x: linspace(t_min, t_max, t_steps),
                                                    y: plot,
                                                    type: 'scatter'
                                                },

                                            ] : []}
                                            layout={{
                                                width: 520,
                                                height: 540,
                                                title: titles[i],
                                                showLegend: true,
                                                yaxis: {
                                                    title: {
                                                        text: labels[i]
                                                    }
                                                },
                                                 xaxis: {
                                                    title: {
                                                        text: 't'
                                                    }
                                                }
                                            }}
                                        />
                                    )
                                })
                            }

                        </Grid>

                    </div>

                </div>


            </div>
        );
    }


}


export default PlotContainer;