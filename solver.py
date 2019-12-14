from math import tan

import numpy as np
from numpy.ma import sqrt
from scipy.integrate import odeint
import matplotlib.pyplot as pl
from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Slider, Div
from bokeh.models.widgets import Paragraph

from Chute import Chute
from ChuteManager import ChuteManager
from environment import rho, g

mass = 60
chutes = ChuteManager()

chute = Chute()
chute.A_max = 1
chute.cutHeight = -1
chute.openingHeight = 300
chute.cw = 2
chute.openingDelay = 0
chute.openingDuration = 3

chutes.addChute(chute)

args = (mass, chutes)


def height(x, t, *args):
    pos_x, pos_y, velocity_x, velocity_y = x

    if pos_y > 0:
        a = acceleration(x, t, args)
        f = [velocity_x, velocity_y, a[0], a[1]]
    else:
        f = [0, 0, 0, 0]
    return f


def acceleration(x, t, *args):
    pox_x, pos_y, velocity_x, velocity_y = x
    velocity_abs = sqrt(velocity_x**2 + velocity_y**2)
    a_abs = 0.5 * rho(pos_y) * (velocity_x**2 + velocity_y**2) * args[1].getCWA(t, pos_y) / args[0]
    return velocity_x / velocity_abs * a_abs, velocity_y / velocity_abs * a_abs - g(pos_y)


x0 = [2000, 0, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
t = np.linspace(0, 120, 1000)
x = odeint(height, x0, t, args=args)
print(x)

pl.figure(1)
pl.plot(t, x[:, 0])
pl.legend()
pl.show()
