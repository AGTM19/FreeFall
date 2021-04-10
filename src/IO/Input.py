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
#     rocket_manager.mass = 11
#     chute_manager = ChuteManager()
#     chutes = [
#         Chute(
#             name="Chute1",
#             A_max=0.1576,
#             cw=1.5,
#             openingHeight=500,
#             cutHeight=-1,
#             openingDelay=4,
#             openingDuration=0.25),
#
#         Chute(
#             name="Chute2",
#             A_max=4.525,
#             cw=2.2,
#             openingHeight=300,
#             cutHeight=-1,
#             openingDelay=0,
#             openingDuration=2)
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
#         self.x0 = [0, 500, 0, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
#         self.t = np.linspace(0, 1250, 100000)  # TimeVector

class Input:
    x0 = []
    t = None
    additional_args = {}  # hier kann man hinzufuegen, falls in odeint extra Parameter wie 'col_deriv' gebraucht werden
    rocket_manager = RocketManager()
    rocket_manager.mass = 90
    chute_manager = ChuteManager()
    chutes = [

        Chute(
            name="Chute1",
            A_max=6.5967,
            cw=0.3,
            openingHeight=70000,
            cutHeight=3000,
            openingDelay=2,
            openingDuration=0.25),

        Chute(
            name="Chute2",
            A_max=25.06,
            cw=3.007,
            openingHeight=3000,
            cutHeight=-1,
            openingDelay=1,
            openingDuration=0.25)
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
        self.x0 = [0, 70000, 230, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
        self.t = np.linspace(0, 1250, 100000)  # TimeVector