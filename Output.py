import matplotlib.pyplot as pl

from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Slider, Div
from bokeh.models.widgets import Paragraph


def visualize(x, t):
    __matplot(x, t)


def __matplot(x, t):
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