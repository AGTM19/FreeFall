from Environment.Chute import Chute


class ChuteManager:

    def __init__(self):
        self.chutes = list()
        self.activeChute = None

    def getName(self):
        return "ChuteManager"

    def addChute(self, chute):
        self.correctChuteHeights(chute)
        self.chutes.append(chute)
        if self.activeChute is None:
            self.activeChute = chute

    def addNewChute(self, name, A_max, cw, openingHeight, cutHeght, openingDelay, openingDuration):
        chute = Chute()
        chute.name = name
        chute.A_max = A_max
        chute.cw = cw
        chute.openingHeight = openingHeight
        chute.cutHeight = cutHeght
        chute.openingDelay = openingDelay
        chute.openingDuration = openingDuration
        self.addChute(chute)

    def correctChuteHeights(self, chute):
        if not self.chutes:
            print("No chutes yet")
            return
        print("There are already ", len(self.chutes), " Chutes")
        c = self.chutes[len(self.chutes) - 1]
        if c.cutHeight < chute.openingHeight:
            chute.openingHeight = c.cutHeight
            if chute.cutHeight < chute.openingHeight:
                chute.cutHeight = chute.openingHeight

    def getCWA(self, t, h):
        chute = None
        for c in self.chutes:
            if c.cutHeight < h < c.openingHeight:
                chute = c
                break
        if chute is None:
            return 0
        return chute.get_cwa(t)
