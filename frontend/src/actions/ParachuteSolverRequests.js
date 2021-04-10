import * as superagent from 'superagent'


class ParachuteSolverRequests{

    solve(chutes, rocketData, plotConfig){
        return superagent
            .post('http://localhost:8000/solve')
            .send({ chutes, rocketData, plotConfig })
    }

}

export default ParachuteSolverRequests;