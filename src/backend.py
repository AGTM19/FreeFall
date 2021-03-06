from flask import Flask, request, jsonify
from Environment.Chute import Chute
from Environment.ChuteManager import ChuteManager
from Environment.DragManager import DragManager
from Environment.RocketManager import RocketManager
from solver import Solver
import numpy as np
from flask_cors import CORS
import math

app = Flask(__name__)
CORS(app)


@app.route('/solve', methods=['POST'])
def solve():
    params = request.json
    chute_manager = ChuteManager()
    rocket_manager = RocketManager()

    for chute in params['chutes']:
        chute_manager.addChute(Chute(
            name=chute['name'],
            A_max=chute['A_max'],
            cw=chute['cw'],
            openingHeight=chute['openingHeight'],
            cutHeght=chute['cutHeight'],
            openingDelay=chute['openingDelay'],
            openingDuration=chute['openingDuration']
        ))
    rocket_data = params['rocketData']
    rocket_manager.mass = rocket_data['mass']
    drag_manager = DragManager(rocket_manager, chute_manager)
    rocket_x0 = [rocket_data['pos_x'], rocket_data['pos_y'], rocket_data['vel_x'], rocket_data['vel_y']]
    # plot_data = params['plotData']
    t = np.linspace(0, 170, 10000)
    _, x = Solver.solve(rocket_x0, t, rocket_manager.mass, drag_manager)
    x = x.transpose().tolist()
    y = []

    for i, col in enumerate(x):
        new_col = []
        for j, val in enumerate(col):
            if not math.isfinite(val):
                new_col.append(0)
            else:
                new_col.append(val)
        y.append(new_col)

    return jsonify({
        'message': 'Hello World',
        'error': None,
        'plotData': y
    })


if __name__ == '__main__':
    app.run(port=5000)
