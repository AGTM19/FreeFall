from Environment.ChuteManager import ChuteManager
from Environment.Chute import Chute
from Environment.RocketManager import RocketManager
from Environment.DragManager import DragManager

import numpy as np


# class Input:
#     x0 = []
#     t = None
#     additional_args = {}  # hier kann man hinzufuegen, falls in odeint extra Parameter wie 'col_deriv' gebraucht werden
#     rocket_manager = RocketManager()
#     rocket_manager.mass = 10.2
#     chute_manager = ChuteManager()
#     chutes = [
#         # Chute(
#         #     name="Chute1",
#         #     A_max=0.1576,
#         #     cw=1.5,
#         #     openingHeight=3000,
#         #     cutHeight=500,
#         #     openingDelay=0,
#         #     openingDuration=0.01),
#         #
#         # Chute(
#         #     name="Chute2",
#         #     A_max=4.525,
#         #     cw=2.2,
#         #     openingHeight=500,
#         #     cutHeight=-1,
#         #     openingDelay=0,
#         #     openingDuration=0.166)
#     ]
#     drag_manager = None
#
#     def retrieve_input(self):
#         """
#         assigns x0, t, and mass to the class
#         adds all chutes to classes' chute_manager
#         """
#         for c in self.chutes:
#             self.chute_manager.addChute(c)
#         self.drag_manager = DragManager(self.rocket_manager, self.chute_manager)
#         self.x0 = [0, 3000, 60, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
#         self.t = np.linspace(0, 1250, 100000)  # TimeVector

class Input:
    x0 = []
    t = None
    additional_args = {}  # hier kann man hinzufuegen, falls in odeint extra Parameter wie 'col_deriv' gebraucht werden
    rocket_manager = RocketManager()
    rocket_manager.mass = 80
    chute_manager = ChuteManager()
    chutes = [

        Chute(
            name="Chute1",
            # A_max=5.8638021,
            A_max=3.2983886667,
            cw=0.3,
            openingHeight=75900,
            cutHeight=3000,
            openingDelay=10,
            openingDuration=0.1),

        Chute(
            name="Chute2",
            A_max=25.06,
            cw=3.007,
            openingHeight=3000,
            cutHeight=-1,
            openingDelay=0.00001,
            openingDuration=0.0578)
            # openingDuration=0.265)
    ]
    drag_manager = None

    def retrieve_input(self):
        """
        assigns x0, t, and mass to the class
        adds all chutes to classes' chute_manager
        """
        for c in self.chutes:
            self.chute_manager.addChute(c)

        self.drag_manager = DragManager(self.rocket_manager, self.chute_manager)
        self.x0 = [0, 75900, 230, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
        self.t = np.linspace(0, 1250, 100000)  # TimeVector