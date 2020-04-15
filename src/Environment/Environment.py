import numpy as np
from Util.Interpolator import Interpolator
import matplotlib.pyplot as pl


class Environment:
    h0 = 0  # m
    t0 = 288.15  # K
    p0 = 1  # kg / (m * s**2)
    rho0 = 1.184 #1.225  # kg / m**3
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
    hv = np.linspace(0, 71000, 7100)  # TimeVector
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


if __name__ == '__main__':
    demo()
