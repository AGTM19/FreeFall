from Environment import Environment


class StationaryCWA:

    @staticmethod
    def get_cw_a(m, v, h):
        """

        :param m: Mass
        :param v: Velocity
        :param h: Height
        :return: c_w * Area
        """
        return 2 * m * Environment.g(h) / (v ** 2 * Environment.rho(h))

    @staticmethod
    def get_a(cwa, cw):
        return cwa / cw

    @staticmethod
    def get_cw(cwa, a):
        return cwa / a


def demo():
    print(StationaryCWA.get_cw_a(80,30, 3000))


if __name__ == "__main__":
    demo()
