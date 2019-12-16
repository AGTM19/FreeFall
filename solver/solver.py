import numpy
from scipy.integrate import odeint
from Environment.environment import rho, g


def solve(x0, t, *args):
    y = odeint(__height, x0, t, args=args)
    a = __resAcc(y, t, *args)
    x = numpy.concatenate((y, a), axis=1)
    return x


def __height(x, t, *args):
    pos_x, pos_y, velocity_x, velocity_y = x

    if pos_y > 0:
        a = __acceleration(x, t, *args)
        f = [velocity_x, velocity_y, a[0], a[1]]
    else:
        f = [0, 0, 0, 0]
    return f


def __acceleration(x, t, *args):
    pox_x, pos_y, velocity_x, velocity_y = x
    velocity_abs = numpy.ma.sqrt(velocity_x ** 2 + velocity_y ** 2)
    acc = 0.5 * rho(pos_y) * velocity_abs ** 2 * args[1].getCWA(t, pos_y) / args[0]  # luftwiderstand
    return acc * -velocity_x / velocity_abs, acc * -velocity_y / velocity_abs - g(pos_y)  # gesamtbeschleunigung


def __resAcc(x, t, *args):
    a = numpy.transpose(numpy.array([
        [__acceleration(x[i], t[i], *args)[0] for i in range(len(t))],
        [__acceleration(x[i], t[i], *args)[1] for i in range(len(t))]
        ]))
    return a
