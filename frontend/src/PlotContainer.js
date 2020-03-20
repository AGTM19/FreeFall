import React from 'react';
import Plot from 'react-plotly.js';
import dataMock from './datamock'
import PlotDataContainer from "./PlotDataContainer";
import datamock from "./datamock";


const linspace = (a,b,n) => {
    if(typeof n === "undefined") n = Math.max(Math.round(b-a)+1,1);
    if(n<2) { return n===1?[a]:[]; }
    let i,ret = Array(n);
    n--;
    for(i=n;i>=0;i--) { ret[i] = (i*b+(n-i)*a)/n; }
    return ret;
};

class PlotContainer extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            plotConfig: datamock.plot_default_config
        };
    }


    render() {
        const {
            t_max, t_min, t_steps,
        } = this.state.plotConfig;

        return (
            <div>
                <div>
                <h1>Plots:</h1>
                <div
                    className={this.props.styles.containerbg}>
                    <Plot
                        data={[
                            {
                                x: linspace(t_min, t_max, t_steps),
                                y: dataMock.plot1Data,
                                type: 'scatter',
                            },

                        ]}
                        layout={{width: 520, height: 540, title: 'Plot 1'}}
                    />
                </div>
            </div>

            <PlotDataContainer
                styles={this.props.styles}
                initialConfig={this.state.plotConfig}
                onChange={(plotConfig) => this.setState({plotConfig})}
            />
            </div>
        );
    }


}


export default PlotContainer;