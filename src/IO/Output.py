import matplotlib.pyplot as pl
import numpy as np
import tikzplotlib

xlabel = ["X-Position [m]", "Altitude [m]", "X-Velocity [ms$^{-1}$]", "Y-Velocity [ms$^{-1}$]", "X-acceleration [ms$^{-2}$]",
          "Y-acceleration [ms$^{-2}$]", "Velocity [ms$^{-1}$]", "Mach [-]", "Dynamic pressure [Nm$^{-2}$]", "Load [N]"]
title = ["Horizontal position", "Altitude", "Horizontal velocity", "Vertical velocity", "Horizontal acceleration",
         "Vertical acceleration", "Absolute velocity", "Mach number", "Dynamic pressure", "Opening shock load"]
save_title = ["Horizontal_Position", "Altitude", "Horizontal_Velocity", "Vertical_Velocity", "Horizontal_Acceleration",
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
                if index == 8:
                    print(xlabel[index])
                    print(vec[::1])
                    print(h[::1])

                # print vec[::fraction], h[::fraction]) in eine csv mitnamen xlabel[index]
                pl.plot(vec[::fraction], h[::fraction])
                pl.ylabel('Altitude [m]')
                # pl.xlim([-40,1500])
                # pl.ylim([-40, 620])
                pl.xlabel(xlabel[index])
            pl.title(title[index])
            # pl.legend()
            pl.grid(True)
            pl.savefig(save_title[index] + ".png")
            # tikzplotlib.save(title[index] + ".tex")
        pl.show()

    @staticmethod
    def compare(x1, x2, t1, t2):
        np.max(np.max(np.shape(t2)), np.max(np.shape(t1)))
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
                pl.ylabel('Altitude [m]')
                pl.xlabel(xlabel[index])
            pl.title(title[index])
            # pl.legend()
            pl.grid(True)
            pl.savefig(save_title[index] + ".png")
            # tikzplotlib.save(title[index] + ".tex")
        pl.show()




