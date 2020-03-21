//import * as superagent from 'superagent'
import datamock from "../datamock";


class ParachuteSolverRequests{

    solve(chutes, rocketData){
       /* return superagent
            .get('localhost:8000/solve')
            .send({ chutes, rocketData })
            .then(res => {
                console.log(res);
            })*/
       return Promise.resolve(datamock.sample_response);
    }

}

export default ParachuteSolverRequests;