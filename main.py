import numpy as np

from ChuteManager import ChuteManager
from Output import visualize
from solver import solve

mass = 60  # Masse der Rakete
chutes = ChuteManager()  # klärt, welcher Fallschirm gerade genutzt wird

chutes.addNewChute(name="Chute1",
                   A_max=1.5,
                   cw=2,
                   openingHeight=2000,
                   cutHeght=500,
                   openingDelay=0,
                   openingDuration=2)
chutes.addNewChute(name="Chute2",
                   A_max=3.5,
                   cw=2,
                   openingHeight=500,
                   cutHeght=-1,
                   openingDelay=0,
                   openingDuration=2)

x0 = [0, 2000, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
t = np.linspace(0, 170, 1000000)  # TimeVector
args = (mass, chutes)  # additional arguments

x = solve(x0, t, args)
visualize(x, t)


