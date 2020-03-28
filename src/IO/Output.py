import matplotlib.pyplot as pl

ylabel = ["Horizontal Position [m]", "Height [m]", "Horizontal Velocity [m/s]", "Vertical Velocity [m/s]", "Horizontal acceleration [m/s²]", "Vertical acceleration [m/s²]"]

class Output:

    @staticmethod
    def visualize(x, t):
        for index in range(x.shape[1]):
            pl.figure(index + 1)
            pl.plot(t, x[:, index])
            pl.xlabel('Time [s]')
            pl.ylabel(ylabel[index])
            #pl.legend()
            pl.grid(True)
        pl.show()
