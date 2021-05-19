import matplotlib.pyplot as pl
import tikzplotlib

xlabel = ["Velocity [m/s]"]
title = ["Operating range of the drogue ejection "]
save_title = ["Operating range"]

# Wertebereich für x-Achse festlegen:
x = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]

# v=[250,575,750,800,900,1000,1100,1200,1300,1400,1500,1600]
#
#
#
# h=[10000,20000,30000,40000,50000,60000,70000,80000,90000,100000,110000,120000]
#
# q=[14000,1400,7100,2400,3000,3000,3000,3000,3000,3000,3000,3000]
# h=[10000,20000,30000,40000]


x2 = [num**2 for num in x]
x3 = [num**3 for num in x]

# Einzelne Diagramm-Linien plotten:
pl.plot(v, h, 'b-')
pl.plot(q, h,'g-')
# pl.plot(x, x3,'g^')

# Plotstyle:
pl.grid(True)
pl.title(title[0])
pl.ylabel('Height [m]')
pl.xlabel("Velocity [m/s]")
pl.savefig(save_title[0] + ".png")
# Diagramm ausgeben:
pl.show()


# v=[2,3,4,5,6]
# h=2,3,4,5,6
#
#         pl.plot(v,h)
#         pl.ylabel('Height [m]')
#         pl.xlabel("Velocity [m/s]")
#         # h_index = 1
#         # h = x[:, h_index]
#         # for index in range(x.shape[1]):
#         #     pl.figure(index + 1)
#         #     vec = x[:, index]
#         #     fraction = 1
#         #     if index is h_index:
#         #         pl.plot(t[::fraction], vec[::fraction])
#         #         pl.xlabel('Time [s]')
#         #         pl.ylabel(xlabel[index])
#         #     else:
#         #         pl.plot(vec[::fraction], h[::fraction])
#         #         pl.ylabel('Height [m]')
#         #         pl.xlabel(xlabel[index])
#             pl.title(title)
#             # pl.legend()
#             pl.grid(True)
#             pl.savefig(save_title + ".png")
#             # tikzplotlib.save(title + ".tex")
#         pl.show()



