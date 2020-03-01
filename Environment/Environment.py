class Environment:
    h0 = 0  # m
    t0 = 288.15  # K
    p0 = 1  # kg / (m * s**2)
    rho0 = 1.225  # kg / m**3
    g0 = 9.807  # m / s**2
    kappa = 1.402  # -
    mol = 0.02896  # kg / mol
    r = 8.314  # 1 / (K * mol)

    @staticmethod
    def temperature(h):
        if h < 0:
            h = 0
        return Environment.t0 * (1 - Environment.__a(h) * (h - Environment.h0) / Environment.t0)

    @staticmethod
    def __a(h):
        if h < 0:
            h = 0
        return (Environment.kappa - 1) / Environment.kappa * Environment.mol * Environment.g(h) / Environment.r

    @staticmethod
    def rho(h):
        if h < 0:
            h = 0
        return Environment.rho0 * (1 - Environment.__a(h) * (h - Environment.h0) / Environment.t0) ** (
                1 / (Environment.kappa - 1))

    @staticmethod
    def g(h):
        if h < 0:
            a = 0
        return Environment.g0 * ((6371 * 1000) / (6371 * 1000 + h)) ** 2
