from Environment.ChuteManager import ChuteManager


def getChutes():
    chutes = ChuteManager()  # klärt, welcher Fallschirm gerade genutzt wird

    chutes.addNewChute(name="Chute1",
                       A_max=1.5,
                       cw=2,
                       openingHeight=2000,
                       cutHeght=500,
                       openingDelay=0,
                       openingDuration=2)
    chutes.addNewChute(name="Chute2",
                       A_max=3.5,
                       cw=2,
                       openingHeight=500,
                       cutHeght=-1,
                       openingDelay=0,
                       openingDuration=2)

    return chutes
