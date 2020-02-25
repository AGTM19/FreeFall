from Environment.ChuteManager import ChuteManager


def getInput():
    mass = 60  # Masse der Rakete
    chutes = Input.getChutes()

    x0 = [0, 2000, 80, 0]  # [pos_x, pos_y, vel_x, vel_y] StartingVector
    t = np.linspace(0, 170, 10000)  # TimeVector
    return mass, chutes, x0, t

def __getChutes():
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
