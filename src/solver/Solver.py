import numpy
from scipy.integrate import odeint
from Environment.Environment import Environment as Env


def solve(x0, t, *args):
    """
    Demands the mass of the Rocket and a valid initialized DragManager.
    Uses environmental parameters from class File Environment.
    Returns a Vector with height/velocity and the time vector.

    :param x0: starting Vector [pos_x, pos_y, vel_x, vel_y]
    :param t: timeVector (starts at starting time, ends at ending time, has as many entries as demanded timesteps for numerical solving)
    :param args: (mass, DragManager)
    :return: x, t
    """
    y = odeint(__height, x0, t, args=args)
    a = __resAcc(y, t, *args)
    velocity = __velAbs(y, t)
    mach = __mach(y[:, 1], velocity)
    dyn_pressure = __dynPressure(y[:, 1], velocity)
    load = __load(a, args[0])
    x = numpy.concatenate((y, a, numpy.transpose(numpy.array([velocity, mach, dyn_pressure, load]))), axis=1)
    t, x = __cutNullResult(x, t)

    return t, x


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
    acc = 0.5 * Env.rho(pos_y) * velocity_abs ** 2 * args[1].getCWA(t, pos_y, velocity_abs) / args[0]  # luftwiderstand
    velocity_abs = velocity_abs if velocity_abs > 0.0001 else 1
    return acc * -velocity_x / velocity_abs, acc * -velocity_y / velocity_abs - Env.g(
        pos_y)  # gesamtbeschleunigung


def __resAcc(x, t, *args):
    a = numpy.transpose(numpy.array([
        [__acceleration(x[i], t[i], *args)[0] for i in range(len(t))],
        [__acceleration(x[i], t[i], *args)[1] for i in range(len(t))]
    ]))
    return a


def __load(a, m):
    load = [None] * a.shape[0]
    for i in range(a.shape[0]):
        load[i] = numpy.sqrt(a[i, 0]**2+a[i, 1]**2) * m
    return load


def __velAbs(x, t):
    vel_abs = [None] * len(t)
    for i in range(len(t)):
        vel_abs[i] = numpy.sqrt(x[i, 2] ** 2 + x[i, 3] ** 2)
    return vel_abs


def __mach(h, v):
    mach = [None] * len(v)
    for i in range(len(v)):
        mach[i] = Env.mach(h[i], v[i])
    return mach


def __dynPressure(h, v):
    dyn_pressure = [None] * len(v)
    for i in range(len(v)):
        dyn_pressure[i] = Env.rho(h[i]) / 2 * v[i] ** 2
    return dyn_pressure


def __cutNullResult(x, t):
    total_length = len(t)
    last_index = len(t)
    for index in range(total_length):
        if numpy.abs(x[index][1]) < 0.0000001:
            last_index = index
            break

    x_new = x[:last_index][:]
    t = t[:last_index]
    return t, x_new
