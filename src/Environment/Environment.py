import numpy as np
from Util.Interpolator import Interpolator
import matplotlib.pyplot as pl


class Environment:
    h0 = 0  # m
    t0 = 288.15  # K
    p0 = 1  # kg / (m * s**2)
    rho0 = 1.184  # 1.225  # kg / m**3
    g0 = 9.807  # m / s**2
    kappa = 1.402  # -
    mol = 0.02896  # kg / mol
    r = 8.314  # 1 / (K * mol)

    @staticmethod
    def temperature(h):
        T_h = {0: 288.15, 11000: 216.65, 20000: 216.65, 32000: 228.65, 47000: 270.65, 51000: 270.65, 71000: 214.65}
        # if h < 0:
        #    h = 0
        # return Environment.t0 * (1 - Environment.__a(h) * (h - Environment.h0) / Environment.t0)
        return Interpolator.getInterpolatedValue(T_h, h)

    @staticmethod
    def __a__(h):
        if h < 0:
            h = 0
        return (Environment.kappa - 1) / Environment.kappa * Environment.mol * Environment.g(h) / Environment.r

    @staticmethod
    def rho(h):
        rho_h = {0: 1.225, 11000: .36391, 20000: .08803, 32000: .01322, 47000: .00143, 51000: .00086, 71000: .000064}
        # if h < 0:
        #    h = 0
        # return Environment.rho0 * (1 - Environment.__a__(h) * (h - Environment.h0) / Environment.t0) ** (
        #        1 / (Environment.kappa - 1))
        return Interpolator.getInterpolatedValue(rho_h, h)

    @staticmethod
    def g(h):
        if h < 0:
            a = 0  # TODO: wofür wird a gebraucht?
        return Environment.g0 * (6371000 / (6371000 + h)) ** 2

    @staticmethod
    def mach(h, v):
        return v / np.sqrt(Environment.kappa * Environment.r / Environment.mol * Environment.temperature(h))


def demo():
    hv = np.linspace(0, 70000, 7100)  # TimeVector
    tv = []
    g = []
    rhov = []

    for h in hv:
        tv.append(Environment.temperature(h))
        g.append(Environment.g(h))
        rhov.append(Environment.rho(h))

    pl.figure("Temperature")
    pl.plot(hv, tv)
    pl.xlabel("Height [m]")
    pl.ylabel("Temperature [K]")

    pl.figure("Gravity")
    pl.plot(hv, g)
    pl.xlabel("Height [m]")
    pl.ylabel("Gravity [m/s²]")

    pl.figure("Density")
    pl.plot(hv, rhov)
    pl.xlabel("Height [m]")
    pl.ylabel("Density [kg/m³]")

    pl.show()


def vFromMach(mach, h):
    return mach * np.sqrt(Environment.kappa * Environment.r / Environment.mol * Environment.temperature(h))


def vFromLast(Last, h):
    return np.sqrt(Last * 2 / (2.55 * 0.8 * Environment.rho(h)))


def diag():
    mach4 = []
    mach6 = []
    mach8 = []
    mach1 = []
    N1000 = []
    N2500 = []
    N5000 = []
    N10000 = []

    hv = np.linspace(0, 40000, 4000)  # TimeVector

    for h in hv:
        mach4.append(vFromMach(0.4, h))
        mach6.append(vFromMach(0.6, h))
        mach8.append(vFromMach(0.8, h))
        mach1.append(vFromMach(1.0, h))
        N1000.append(vFromLast(1000, h))
        N2500.append(vFromLast(2500, h))
        N5000.append(vFromLast(5000, h))
        N10000.append(vFromLast(10000, h))

    pl.figure("Mach")
    l1, = pl.plot(mach4, hv, '-')
    l1.set_label("Mach = 0.4")
    l2, = pl.plot(mach6, hv, '--')
    l2.set_label("Mach = 0.6")
    l3, = pl.plot(mach8, hv, '-.')
    l3.set_label("Mach = 0.8")
    l4, = pl.plot(mach1, hv, ':')
    l4.set_label("Mach = 1.0")
    l5, = pl.plot(N1000, hv, '-')
    l5.set_label("1.0 kN")
    l6, = pl.plot(N2500, hv, '--')
    l6.set_label("2.5 kN")
    l7, = pl.plot(N5000, hv, '-.')
    l7.set_label("5.0 kN")
    l8, = pl.plot(N10000, hv, ':')
    l8.set_label("10.0 kN")
    
    pl.xlabel("Velocity [m/s]")
    pl.ylabel("Height [m]")
    pl.xlim(0, 600)
    pl.legend()
    pl.grid(True)
    #pl.savefig(title[index] + ".png")
    # tikzplotlib.save(title[index] + ".tex")
    pl.show()



if __name__ == '__main__':
    demo()
    diag()
