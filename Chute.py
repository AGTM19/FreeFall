class Chute:

    def __init__(self):
        self.A_max = 0
        self.openingHeight = 0
        self.cutHeight = 0
        self.openingDelay = 0
        self.openingDuration = 0
        self.cw = 0
        self.openingTime = None

    def get_cwa(self, t):
        if self.openingTime is None:
            self.openingTime = t
        return self.get_a(t) * self.cw

    def get_a(self, t):
        relative_time = t - self.openingTime
        if relative_time > self.openingDuration:
            return self.A_max
        # assert isinstance(self.openingTime, Chute)
        return self.A_max * relative_time / self.openingTime  # Logic for A(t)
