import matplotlib.pyplot as pl

from bokeh.plotting import figure
from bokeh.layouts import row, column
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, Slider, Div
from bokeh.models.widgets import Paragraph


def visualize(x, t, args):
    __matplot(x, t, args)


def __matplot(x, t, args):
    index = 0
    for a in args:
        pl.figure(index+1)
        pl.plot(t, x[:, index])
        pl.legend()
        index += 1
    pl.show()