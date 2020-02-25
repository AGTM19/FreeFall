import numpy as np


class Chute:

    def __init__(self):
        self.name = "C"
        self.A_max = 0
        self.openingHeight = 0
        self.cutHeight = 0
        self.openingDelay = 0
        self.openingDuration = 0
        self.cw = 0
        self.__openingTime = None

    def get_cwa(self, t):
        if self.__openingTime is None or self.__openingTime > t:
            self.__openingTime = t
        return self.__get_a(t) * self.cw

    def __get_a(self, t):
        """ Calculates the  """
        relative_time = abs(t - self.__openingTime)
        # a = relative_t / self.openingDuration
        # a = (1-np.e**(-4*relative_t/self.openingDuration))
        a = np.e ** (-0.7 * relative_time / self.openingDuration - 1)
        return self.A_max if relative_time > self.openingDuration else a

    def printDate(self):
        print("A_max: ", self.A_max, "\nopeningHeight: ", self.openingHeight, "\ncutHeight: ", self.cutHeight,
              "\nopeningDelay: ", self.openingDelay, "\nopeningDuration:", self.openingDuration, "\ncw: ", self.cw,
              "\n__openingTime: ", self.__openingTime)
