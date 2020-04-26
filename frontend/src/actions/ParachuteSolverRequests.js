import * as superagent from 'superagent'


class ParachuteSolverRequests{

    solve(chutes, rocketData, plotConfig){
        return superagent
            .post('/solve')
            .send({ chutes, rocketData, plotConfig })
    }

}

export default ParachuteSolverRequests;