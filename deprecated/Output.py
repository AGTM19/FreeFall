import matplotlib.pyplot as pl


def visualize(res):
    x, t = res
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
