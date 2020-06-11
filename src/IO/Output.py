import matplotlib.pyplot as pl
import tikzplotlib

ylabel = ["X-Position [m]", "Y-Position [m]", "X-Velocity [m/s]", "Y-Velocity [m/s]", "X-acceleration [m/s²]", "Y-acceleration [m/s²]"]
title = ["Horizontal_Position", "Height", "Horizontal_Velocity", "Vertical_Velocity", "Horizontal_Acceleration", "Vertical_Acceleration"]
class Output:

    @staticmethod
    def visualize(x, t):
        for index in range(x.shape[1]):
            pl.figure(index + 1)
            vec = x[:, index]
            fraction = 1
            pl.plot(t[::fraction], vec[::fraction])
            pl.xlabel('Time [s]')
            pl.ylabel(ylabel[index])
            pl.title(title[index])
            #pl.legend()
            pl.grid(True)
            pl.savefig(title[index] + ".png")
            #tikzplotlib.save(title[index] + ".tex")
        pl.show()


