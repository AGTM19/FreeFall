class ChuteManager:

    def __init__(self):
        self.chutes = list()

    def addChute(self, chute):
        self.correctChuteHeights(chute)
        self.chutes.append(chute)

    def correctChuteHeights(self, chute):
        if not self.chutes:
            print("No chutes yet")
            return
        print("There are already ", self.chutes.__sizeof__(), " Chutes")
        c = self.chutes[self.chutes.__sizeof__()-1]
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
