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
from Environment import rho, g


def solve(args):
    """
    Demands the mass of the Rocket and a valid initialized ChuteManager.
    Uses environmental parameters from class File Environment.
    Returns a Vector with height/velocity and the time vector.

    :param args: (mass, ChuteManager)
    :return: x, t
    """
    x0 = [0, 2000, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
    t = np.linspace(0, 170, 1000000)
    x = odeint(height, x0, t, args=args)
    return x, t


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
