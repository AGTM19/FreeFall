import * as superagent from 'superagent'


class ParachuteSolverRequests{

    solve(chutes, rocketData, plotData){
        return superagent
            .post('http://localhost:5000/solve')
            .send({ chutes, rocketData, plotData })
    }

}

export default ParachuteSolverRequests;