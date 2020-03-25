from Environment import RocketManager
from Environment import ChuteManager
from Environment import Environment
import numpy as np


class DragManager:

    def __init__(self, rocketManager, chuteManager):
        """
        Constructs instance of DragManager.
        :param rocketManager: instance of RocketManager (containig Rocked Drag)
        :param chuteManager: instance of ChuteManager
        """
        self.rocketManager = rocketManager
        self.chuteManager = chuteManager

    def getCWA(self, t, h, v):
        chute_cwa = self.chuteManager.getCWA(t, h)
        rocket_cwa = self.rocketManager.getCWA(Environment.mach(h, v))
        return np.sqrt(chute_cwa ** 2 + rocket_cwa ** 2)
