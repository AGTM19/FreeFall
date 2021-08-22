import numpy as np
from src.Util.Interpolator import Interpolator
import matplotlib.pyplot as pl
import tikzplotlib

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
        T_h = {0: 288.15, 11000: 216.65, 15000: 216.65, 20000: 216.65, 25000: 221.650, 32000: 228.65, 36000: 239.850, 42000: 256.65, 45000: 265.050, 47000: 270.65, 51000: 270.65, 71000: 214.65, 80000: 196.650, 86000: 186.946, 90000: 186, 100000: 205, 110000: 250, 120000: 373.15}
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
        rho_h = {0: 1.225, 11000: .36391, 15000: 0.193674, 20000: .08803, 25000: 0.0394658, 32000: .01322,  36000: 0.00703441, 42000: 0.00287802, 45000: 0.00188129, 47000: .00143, 51000: .00086, 71000: .000064, 80000: 0.0000157005, 86000: 0.00000564114, 95000: 0.00000044, 120000: 0.000000000001}
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
    pl.plot(tv, hv)
    pl.xlabel("Temperature [K]")
    pl.ylabel("Height [m]")

    pl.figure("Gravity")
    pl.plot(hv, g)
    pl.xlabel("Height [m]")
    pl.ylabel("Gravity [m/s²]")

    pl.figure("Density")
    pl.plot(hv, rhov)
    pl.xlabel("Height [m]")
    pl.ylabel("Density [kg/m³]")
    print(hv[::10])
    print(rhov[::10])

    pl.show()


def vFromMach(mach, h):
    return mach * np.sqrt(Environment.kappa * Environment.r / Environment.mol * Environment.temperature(h))

def vFromLast(Last, h):
    return np.sqrt(Last * 2 / (6.5 * 0.3 * Environment.rho(h)))

def vFromq(q, h):
    return np.sqrt(q * 2 / (Environment.rho(h)))

def v_apo(h):
    p1 = 3.166e-18
    p2 = -6.915e-14
    p3 = -6.017e-08
    p4 = 0.006602
    p5 = 1.455
    return p1 * h ** 4 + p2 * h ** 3 + p3 * h ** 2 + p4 * h + p5

def q_apo(h):
    return 0.5*Environment.rho(h)*v_apo(h)**2

# def max_h(h):
#
# def nominal_h(h):
#
# def min_h(h):

def diag():
    # mach4 = []
    # mach6 = []
    # mach8 = []
    mach1 = []
    mach2 = []
    mach25 = []
    mach3 = []
    # N1000 = []
    # N2500 = []
    # N5000 = []
    N30000 = []
    q1 =[]
    q2 = []


    hv = np.linspace(0, 120000, 4000)  # TimeVector

    for h in hv:
        # mach4.append(vFromMach(0.4, h))
        # mach6.append(vFromMach(0.6, h))
        # mach8.append(vFromMach(0.8, h))
        mach1.append(vFromMach(1.0, h))
        mach2.append(vFromMach(2.0, h))
        mach25.append(vFromMach(2.5, h))
        mach3.append(vFromMach(3.0, h))
        # N1000.append(vFromLast(1000, h))
        # N2500.append(vFromLast(2500, h))
        # N5000.append(vFromLast(5000, h))
        q1.append(vFromq(4500, h))
        N30000.append(vFromLast(30000, h))
        q2.append(vFromq(400, h))



    pl.figure("Mach")
    # l1, = pl.plot(mach4, hv, '-')
    # l1.set_label("Mach = 0.4")
    # l2, = pl.plot(mach6, hv, '--')
    # l2.set_label("Mach = 0.6")
    # l3, = pl.plot(mach8, hv, '-.')
    # l3.set_label("Mach = 0.8")
    l4, = pl.plot(mach1, hv, 'r-')
    l4.set_label("Mach = 1.0")
    # l5, = pl.plot(mach2, hv, 'r-')
    # l5.set_label("Mach = 2.0")
    l6, = pl.plot(mach25, hv, '--')
    l6.set_label("Mach = 2.5")
    l7, = pl.plot(mach3, hv, '--')
    l7.set_label("Mach = 3.0")
    # l5, = pl.plot(N1000, hv, '-')
    # l5.set_label("1.0 kN")
    # l6, = pl.plot(N2500, hv, '--')
    # l6.set_label("2.5 kN")
    # l7, = pl.plot(N5000, hv, '-.')
    # l7.set_label("5.0 kN")
    # l8, = pl.plot(q1, hv, ':')
    # l8.set_label("q = 4500 N/m²")
    l9, = pl.plot(N30000, hv, ':')
    l9.set_label("$F_{OP}$ = 30 kN")
    # l10, = pl.plot(q2, hv, ':')
    # l10.set_label("Dynamic Pressure = 4500 N/m²")
    l10, = pl.plot(v_apo(hv), hv, ':')
    l10.set_label("$v_{apo}$")



    pl.xlabel("Velocity [m/s]")
    pl.ylabel("Altitude [m]")
    pl.xlim(0, 1600)
    # pl.yticks( [0, 10000, 30000, 45000, 75900, 120000])
    pl.title("Apogee velocity")
    pl.legend(loc='upper right')
    pl.grid(True)
    save_title = ["Apogee_velocity"]
    pl.savefig(save_title[0] + ".png")
    # pl.savefig(title[index] + ".png")
    # tikzplotlib.save(save_title[0] + ".tex")

    # print(hv[::10])
    # print(mach1[::10])
    # print(mach3[::10])
    # print(v_apo[::10])


    pl.show()



if __name__ == '__main__':
    demo()
    diag()
