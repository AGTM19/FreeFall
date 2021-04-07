import matplotlib.pyplot as pl
import tikzplotlib

xlabel = ["X-Position [m]", "Height [m]", "X-Velocity [m/s]", "Y-Velocity [m/s]", "X-acceleration [m/s²]",
          "Y-acceleration [m/s²]", "Velocity [m/s]", "Mach [-]", "Dynamic Pressure [N/m^2]", "Load [N]"]
title = ["Horizontal Position", "Height", "Horizontal Velocity", "Vertical Velocity", "Horizontal Acceleration",
         "Vertical Acceleration", "Absolute Velocity", "Mach Number", "Dynamic Pressure", "Shock Load"]
save_title = ["Horizontal_Position", "Height", "Horizontal_Velocity", "Vertical_Velocity", "Horizontal_Acceleration",
         "Vertical_Acceleration", "Absolute_Velocity", "Mach_Number", "Dynamic_Pressure", "Shock_Load"]


class Output:

    @staticmethod
    def visualize(x, t):
        h_index = 1
        h = x[:, h_index]
        for index in range(x.shape[1]):
            pl.figure(index + 1)
            vec = x[:, index]
            fraction = 1
            if index is h_index:
                pl.plot(t[::fraction], vec[::fraction])
                pl.xlabel('Time [s]')
                pl.ylabel(xlabel[index])
            else:
                pl.plot(vec[::fraction], h[::fraction])
                pl.ylabel('Height [m]')
                pl.xlabel(xlabel[index])
            pl.title(title[index])
            # pl.legend()
            pl.grid(True)
            pl.savefig(save_title[index] + ".png")
            # tikzplotlib.save(title[index] + ".tex")
        pl.show()

