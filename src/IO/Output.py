import matplotlib.pyplot as pl


class Output:

    @staticmethod
    def visualize(x, t):
        index = 0
        for _ in range(x.shape[1]):
            pl.figure(index + 1)
            pl.plot(t, x[:, index])
            #pl.legend()
            index += 1
        pl.show()
