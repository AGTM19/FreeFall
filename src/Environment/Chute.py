import numpy as np


class Chute:

    def __init__(self, name, A_max, cw, openingHeight, cutHeight, openingDelay, openingDuration):
        self.name = name
        self.A_max = A_max
        self.cw = cw
        self.openingHeight = openingHeight
        self.cutHeight = cutHeight
        self.openingDelay = openingDelay
        self.openingDuration = openingDuration
        self.__openingTime = None

    def get_cwa(self, t):
        if self.__openingTime is None or self.__openingTime > t:
            self.__openingTime = t
        return self.__get_a(t) * self.cw

    def __get_a(self, t):
        """ Calculates the  """
        relative_time = abs(t - self.__openingTime) - self.openingDelay
        relative_time = 0 if relative_time < 0 else relative_time
        # a = relative_t / self.openingDuration
        # a = (1-np.e**(-4*relative_t/self.openingDuration))

        if self.openingDuration != 0 and relative_time < self.openingDuration:
        #a = self.A_max * np.e ** (2 * (0.7 * relative_time / self.openingDuration - 0.7))
            a = self.A_max * relative_time / self.openingDuration * np.e ** (2 * (0.7 * relative_time / self.openingDuration - 0.7))

            #a = self.A_max * relative_time / self.openingDuration
        else:
            a = self.A_max
        return a

    def printDate(self):
        print("A_max: ", self.A_max, "\nopeningHeight: ", self.openingHeight, "\ncutHeight: ", self.cutHeight,
              "\nopeningDelay: ", self.openingDelay, "\nopeningDuration:", self.openingDuration, "\ncw: ", self.cw,
              "\n__openingTime: ", self.__openingTime)
