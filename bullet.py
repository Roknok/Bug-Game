class Bullet:
    def __init__(self,win,pos,img):
        self.win = win
        self.pos = [pos[0],pos[1]]
        self.img = img
        self.height = 10
        self.width = 7
    
    def display(self):
        self.win.blit(self.img,(self.pos[0],self.pos[1]))
    
    def move(self):
        self.pos[1] += -3