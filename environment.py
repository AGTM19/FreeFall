def rho(h):
    default = 1000
    value = default/h if h > 1 else default
    return value


def g(h):
    return 9.807 * ((6371 * 1000) / (6371 * 1000 + h)) ** 2


