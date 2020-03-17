from Environment.ChuteManager import ChuteManager
from Environment.Chute import Chute

import numpy as np


class Input:
    mass = 0
    x0 = []
    t = None
    additional_args = {}  # hier kann man hinzufuegen, falls in odeint extra Parameter wie 'col_deriv' gebraucht werden
    chute_manager = ChuteManager()
    chutes = [
        Chute(
            name="Chute1",
            A_max=1.5,
            cw=2,
            openingHeight=2000,
            cutHeght=500,
            openingDelay=0,
            openingDuration=2),
        Chute(
            name="Chute2",
            A_max=3.5,
            cw=2,
            openingHeight=500,
            cutHeght=-1,
            openingDelay=0,
            openingDuration=2)
    ]

    def retrieve_input(self):
        """
        assigns x0, t, and mass to the class
        adds all chutes to classes' chute_manager
        """
        self.mass = 60  # Masse der Rakete
        for c in self.chutes:
            self.chute_manager.addChute(c)

        self.x0 = [0, 2000, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
        self.t = np.linspace(0, 170, 10000)  # TimeVector

