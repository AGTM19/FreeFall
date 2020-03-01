from Chute import Chute
from ChuteManager import ChuteManager


def getInput():
    mass = 60
    chutes = ChuteManager()  # klärt, welcher Fallschirm gerade genutzt wird

    chute = Chute()  # aktuell einziger Fallschirm
    chute.name = "Chute"
    chute.A_max = 1.5
    chute.cutHeight = 500
    chute.openingHeight = 2000
    chute.cw = 2
    chute.openingDelay = 0
    chute.openingDuration = 5  # muss positiv ungleich 0 sein

    chuty = Chute()
    chuty.name = "Chuty"
    chuty.A_max = 3.5
    chuty.cutHeight = -1
    chuty.openingHeight = 500
    chuty.cw = 2
    chuty.openingDelay = 0
    chuty.openingDuration = 5  # muss positiv ungleich 0 sein

    chutes.addChute(chute)
    chutes.addChute(chuty)
    chute.printDate()
    chuty.printDate()

    args = (mass, chutes)
    return args
