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
    pos_x, pos_y, velocity_x, velocity_y = x

    if pos_y > 0:
        a = acceleration(x, t, *args)
        f = [velocity_x, velocity_y, a[0], a[1]]
    else:
        f = [0, 0, 0, 0]
    return f


def acceleration(x, t, *args):
    pox_x, pos_y, velocity_x, velocity_y = x
    velocity_abs = sqrt(velocity_x ** 2 + velocity_y ** 2)
    acc = 0.5 * rho(pos_y) * velocity_abs ** 2 * args[1].getCWA(t, pos_y) / args[0]  # luftwiderstand
    return acc * -velocity_x / velocity_abs, acc * -velocity_y / velocity_abs - g(pos_y)  # gesamtbeschleunigung


x0 = [0, 2000, 80, 50]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
t = np.linspace(0, 70, 100000)

x = odeint(height, x0, t, args=args)
chute.printDate()
# print(x)  # print Lösungsvektor der Höhe (?)

pl.figure(1)
pl.plot(t, x[:, 0])
pl.legend()
pl.figure(2)
pl.plot(t, x[:, 1])
pl.figure(3)
pl.plot(t, x[:, 2])
pl.figure(4)
pl.plot(t, x[:, 3])
pl.show()
