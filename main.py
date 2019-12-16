import numpy as np

from IO import Input, Output
from solver.solver import solve

mass = 60  # Masse der Rakete
chutes = Input.getChutes()

x0 = [0, 2000, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
t = np.linspace(0, 170, 10000)  # TimeVector
args = (mass, chutes)  # additional arguments

x = solve(x0, t, *args)  # [pos_x, pos_y, vel_x, vel_y, acc_x, acc_y]
Output.visualize(x, t, (0, 1, 2, 3, 4, 5))
