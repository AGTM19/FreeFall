def rho(h):
    default = 1.000
    return default


def g(h):
    return 9.807 * ((6371 * 1000) / (6371 * 1000 + h)) ** 2


