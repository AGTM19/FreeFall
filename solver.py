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
chutes = ChuteManager()  # klärt, welcher Fallschirm gerade genutzt wird

chute = Chute()  # aktuell einziger Fallschirm
chute.A_max = 2.5
chute.cutHeight = -1
chute.openingHeight = 1000
chute.cw = 2
chute.openingDelay = 0
chute.openingDuration = 5  # muss positiv ungleich 0 sein

chutes.addChute(chute)

args = (mass, chutes)


# print("mass: ", args[0])
# print("chutes: ", args[1].getName())


def height(x, t, *args):
    pos_y, velocity_y = x

    if pos_y > 0:
        a = acceleration(x, t, *args)
        f = [velocity_y, a]
    else:
        f = [0, 0]
    return f


def acceleration(x, t, *args):
    pos_y, velocity_y = x
    sign = velocity_y / abs(velocity_y)
    # print(args[1].getCWA(t, pos_y))
    acc_y = - sign * 0.5 * rho(pos_y) * velocity_y ** 2 * args[1].getCWA(t, pos_y) / args[0]  # luftwiderstand
    return acc_y - g(pos_y)  # gesamtbeschleunigung


x0 = [2000, 80]  # [pos_y, vel_y] StartingVector
t = np.linspace(0, 100, 10000)
x = odeint(height, x0, t, args=args)
chute.printDate()
# print(x)  # print Lösungsvektor der Höhe (?)

pl.figure(1)
pl.plot(t, x[:, 0])
pl.legend()
pl.figure(2)
pl.plot(t, x[:, 1])
pl.show()
