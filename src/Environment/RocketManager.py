from Util.Interpolator import Interpolator
from math import pi

# class RocketManager:
#
#     def __init__(self):
#         self.mass = 11
#         self.area = 0.120 ** 2 * pi
#         self.cw = {0.1: 0.4196,
#                    0.25: 0.3711,
#                    0.5: 0.3396,
#                    0.7: 0.326,
#                    0.8: 0.3223,
#                    0.9: 0.3767,
#                    1: 0.5254,
#                    1.1: 0.5618,
#                    1.2: 0.5532,
#                    1.3: 0.5323,
#                    1.4: 0.5149,
#                    1.5: 0.4964,
#                    1.75: 0.4499,
#                    2: 0.4051,
#                    2.5: 0.3373,
#                    3: 0.3949,
#                    3.5: 0.3228,
#                    4: 0.2905,
#                    4.5: 0.2685}
#
#         # just an example dict. implement file-reader later


class RocketManager:

    def __init__(self):
        self.mass = 90
        self.area = 0.256**2*pi
        self.cw = {0.1:0.4196,
                   0.25:0.3711,
                   0.5:0.3396,
                   0.7:0.326,
                   0.8:0.3223,
                   0.9:0.3767,
                   1:0.5254,
                   1.1:0.5618,
                   1.2:0.5532,
                   1.3:0.5323,
                   1.4:0.5149,
                   1.5:0.4964,
                   1.75:0.4499,
                   2:0.4051,
                   2.5:0.3373,
                   3:0.3949,
                   3.5:0.3228,
                   4:0.2905,
                   4.5:0.2685}

        # just an example dict. implement file-reader later



    def getCWA(self, mach):
        return self.area * Interpolator.getInterpolatedValue(self.cw, mach)
