class Bug:
    def __init__(self,win,pos,con,ext,h,hrt):
        self.counter = 0
        self.win = win
        self.position = [pos[0],pos[1]]
        self.contracted = con
        self.extended = ext
        self.hrt = hrt
        self.height = 50
        self.width = 50
        self.heart = h
        
    def counterup(self):
        self.counter += 1
        if self.counter >= 60:
            self.counter = 0
    
    def display(self):
        if (not self.heart):
            if (self.counter % 30 < 15):
                self.win.blit(self.contracted,(self.position[0],self.position[1]))
            else:
                self.win.blit(self.extended,(self.position[0],self.position[1]))
            self.counterup()
        else:
            self.win.blit(self.hrt,(self.position[0],self.position[1]))
    
    def move(self):
        self.position[1] += 1
    
    def iscolliding(self,p):
        if ((p.pos[0]>=self.position[0]+self.width) or (p.pos[0]+p.width<=self.position[0]) or (p.pos[1]+p.height<=self.position[1]) or (p.pos[1]>=self.position[1]+self.height)):
            return False
        else:
            return True
