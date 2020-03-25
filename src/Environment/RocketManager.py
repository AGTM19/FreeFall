from Util.Interpolator import Interpolator


class RocketManager:

    def __init__(self):
        self.mass = 60
        self.area = 0.2
        self.cw = {0.1: 0.5096, 0.5: 0.4227, 0.75: 0.4073}  # just an example dict. implement file-reader later

    def getCWA(self, mach):
        return self.area * Interpolator.getInterpolatedValue(self.cw, mach)
