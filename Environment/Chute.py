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
        return self.get_a(t) * self.cw

    def get_a(self, t):
        relative_time = abs(t - self.__openingTime)
        return self.A_max if relative_time > self.openingDuration else self.A_max * relative_time / self.openingDuration

    def printDate(self):
        print("A_max: ", self.A_max, "\nopeningHeight: ", self.openingHeight, "\ncutHeight: ", self.cutHeight,
              "\nopeningDelay: ", self.openingDelay, "\nopeningDuration:", self.openingDuration, "\ncw: ", self.cw,
              "\n__openingTime: ", self.__openingTime)
