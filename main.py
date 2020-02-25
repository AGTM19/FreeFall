import numpy as np

from IO import Input, Output
from solver.solver import solve

mass, chutes, x0, t = Input.getInput()
args = (mass, chutes)  # additional arguments
x = solve(x0, t, *args)  # [pos_x, pos_y, vel_x, vel_y, acc_x, acc_y]
Output.visualize(x, t, (0, 1, 2, 3, 4, 5))
