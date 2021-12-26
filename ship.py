class Ship:


    def __init__(self,win,pos,img):
        self.win = win
        self.pos = [pos[0],pos[1]]
        self.img = img
        self.left = False
        self.right = False
        self.height = 50
        self.width = 40

    def display(self):
        self.win.blit(self.img,(self.pos[0],self.pos[1]))

    def move(self,wid):
        if self.left:
            self.pos[0] -= 3

        if self.right:
            self.pos[0] += 3

        if self.pos[0] < 0:
            self.pos[0] = 0

        if self.pos[0] > wid - 50:
            self.pos[0] = wid - 50

    def goleft(self):
        self.left = True

    def stopleft(self):
        self.left = False

    def goright(self):
        self.right = True

    def stopright(self):
        self.right = False
