from Environment.ChuteManager import ChuteManager
from Environment.Chute import Chute
from Environment.RocketManager import RocketManager
from Environment.DragManager import DragManager

import numpy as np


class Input:
    x0 = []
    t = None
    additional_args = {}  # hier kann man hinzufuegen, falls in odeint extra Parameter wie 'col_deriv' gebraucht werden
    rocket_manager = RocketManager()
    rocket_manager.mass = 100
    chute_manager = ChuteManager()
    chutes = [
        Chute(
            name="Chute1",
            A_max=1.8,
            cw=1.5,
            openingHeight=20000,
            cutHeght=2000,
            openingDelay=2,
            openingDuration=2),
        Chute(
            name="Chute2",
            A_max=18,
            cw=2.3,
            openingHeight=2000,
            cutHeght=-1,
            openingDelay=2,
            openingDuration=2)
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
        self.x0 = [0, 20000, 0, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
        self.t = np.linspace(0, 10, 10000)  # TimeVector
