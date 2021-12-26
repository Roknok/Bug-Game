from types import WrapperDescriptorType
import pygame
import random

import bug
import bullet
import ship


difficulty = 1

WIDTH, HEIGHT = 500,500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('practice game')

BUG_EXTENDED_IMAGE = pygame.image.load('assets/bug-extended.png')
BUG_EXTENDED_IMAGE = pygame.transform.scale(BUG_EXTENDED_IMAGE,(50,50))
BUG_EXTENDED_IMAGE = pygame.transform.rotate(BUG_EXTENDED_IMAGE,180)

BUG_CONTRACTED_IMAGE = pygame.image.load('assets/bug-contracted.png')
BUG_CONTRACTED_IMAGE = pygame.transform.scale(BUG_CONTRACTED_IMAGE,(50,50))
BUG_CONTRACTED_IMAGE = pygame.transform.rotate(BUG_CONTRACTED_IMAGE,180)

SHIP_IMAGE = pygame.image.load('assets/space-ship.png')
SHIP_IMAGE = pygame.transform.scale(SHIP_IMAGE,(40,50))

BLUE_BULLET_IMAGE = pygame.image.load('assets/blue-bullet.png')
BLUE_BULLET_IMAGE = pygame.transform.scale(BLUE_BULLET_IMAGE,(7,10))

RED_BULLET_IMAGE = pygame.image.load('assets/red-bullet.png')
RED_BULLET_IMAGE = pygame.transform.scale(RED_BULLET_IMAGE,(7,10))

GREEN_BULLET_IMAGE = pygame.image.load('assets/green-bullet.png')
GREEN_BULLET_IMAGE = pygame.transform.scale(GREEN_BULLET_IMAGE,(7,10))

HEART_IMAGE = pygame.image.load('assets/heart.png')
HEART_IMAGE = pygame.transform.scale(HEART_IMAGE,(30,30))
BIG_HEART_IMAGE = pygame.transform.scale(HEART_IMAGE,(50,50))



player = ship.Ship(WIN,[WIDTH/2-20,400],SHIP_IMAGE)

pygame.font.init()

font = pygame.font.SysFont('Comic Sans MS', 30)



FPS = 60




def draw(bullets,bugs,s,h):

    WIN.fill((100,100,255))
    
    for b in bullets:
        b.move()
        b.display()

    for bug in bugs:
        bug.display()
        bug.move()

    WIN.blit(font.render("SCORE : " + str(s),1,(0,0,0)),(0,0))
    
    for i in range(0,h):
        WIN.blit(HEART_IMAGE,(WIDTH-30-(30 * i),0))


    player.move(WIDTH)
    player.display()


    pygame.display.update() 



def main():
    clock =pygame.time.Clock()
    
    player.pos = [WIDTH/2-20,400]

    run = True
    end_screen = True
    menu_screen = True
    
    bugs = []
    bullets = []

    bug_timer = 1
    BULLET_TIMER = 60
    SCORE = 0
    HEALTH = 0


    while menu_screen:

        clock.tick(FPS)


        WIN.fill((100,200,100))

        fnt = font.render("EASY",1,(255,255,255))

        x1 =round(WIDTH/4 -fnt.get_width()/2-20)
        y1 =round(HEIGHT/2 - fnt.get_height()/2-10)
        x2=round(fnt.get_width()+40)
        y2=round(fnt.get_height()+20)


        pygame.draw.rect(WIN,(0,0,200),[x1,y1,x2,y2])
        pygame.draw.rect(WIN,(0,0,0),[x1,y1,x2,y2],1)
        WIN.blit(fnt,(round(WIDTH/4 -fnt.get_width()/2),round(HEIGHT/2 - fnt.get_height()/2)))


        
        fnt2 = font.render("HARD",1,(255,255,255))

        x12 =round(WIDTH/2 +WIDTH/4 -fnt2.get_width()/2-20)
        y12 =round(HEIGHT/2 - fnt2.get_height()/2-10)
        x22=round(fnt2.get_width()+40)
        y22=round(fnt2.get_height()+20)


        pygame.draw.rect(WIN,(200,0,0),[x12,y12,x22,y22])
        pygame.draw.rect(WIN,(0,0,0),[x12,y12,x22,y22],1)
        WIN.blit(fnt2,(round(WIDTH/2 + WIDTH/4 -fnt2.get_width()/2),round(HEIGHT/2 - fnt2.get_height()/2)))



        fnt = font.render("USE A,D OR ARROWS KEYS",1,(50,50,50))

        WIN.blit(fnt,(round(WIDTH/2 -fnt.get_width()/2),round(75)))

        fnt = font.render("TO MOVE LEFT AND RIGHT",1,(50,50,50))

        WIN.blit(fnt,(round(WIDTH/2 -fnt.get_width()/2),round(125)))

        fnt = font.render("USE SPACE OR ENTER KEY",1,(50,50,50))

        WIN.blit(fnt,(round(WIDTH/2 -fnt.get_width()/2),round(325)))

        fnt = font.render("TO SHOOT BULLETS AT BUGS",1,(50,50,50))

        WIN.blit(fnt,(round(WIDTH/2 -fnt.get_width()/2),round(375)))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                end_screen = False
                menu_screen = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (pos[0]>x1 and pos[0]< x1+x2):
                    if(pos[1]>y1 and pos[1]<y1+y2):
                        menu_screen = False
                        difficulty = 0
                        HEALTH = 3

                if (pos[0]>x12 and pos[0]< x12+x22):
                    if(pos[1]>y12 and pos[1]<y12+y22):
                        menu_screen = False
                        difficulty = 1
                        HEALTH = 1
        

        pygame.display.update() 

    while run:
        
        clock.tick(FPS)


        BULLET_TIMER += 1
        if(BULLET_TIMER >= 30):
            BULLET_TIMER = 30



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                end_screen = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.goleft()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.goright()

                if ((event.key == pygame.K_SPACE or event.key == pygame.K_RETURN )and BULLET_TIMER == 30):

                    BULLET_TIMER = 0
                    
                    r = random.randint(1,3)
                    if r == 1:
                        i = BLUE_BULLET_IMAGE

                    if r == 2:
                        i = RED_BULLET_IMAGE

                    if r == 3:
                        i = GREEN_BULLET_IMAGE

                    bullets.append(bullet.Bullet(WIN,[round(player.pos[0]+20 - 7/2),player.pos[1]],i))

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.stopleft()
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.stopright()


        bug_timer -= 1/60
        if (bug_timer <= 0):
            if difficulty == 0:
                bug_timer = random.randint(2,3)
            elif difficulty == 1:
                bug_timer = random.randint(1,2)

            rnd = 0
            if (difficulty == 0):
                rnd = 50
            if (difficulty == 1):
                rnd = 100
            
            if (random.randint(1,rnd) == 1):
                bugs.append(bug.Bug(WIN,[round(random.random()*9) *( WIDTH - 50)/9,-100],BUG_CONTRACTED_IMAGE,BUG_EXTENDED_IMAGE,True,BIG_HEART_IMAGE))
            else:
                bugs.append(bug.Bug(WIN,[round(random.random()*9) *( WIDTH - 50)/9,-100],BUG_CONTRACTED_IMAGE,BUG_EXTENDED_IMAGE,False,BIG_HEART_IMAGE))


        for b in bugs:
            if b.iscolliding(player):
                if (not b.heart):    
                    bugs.remove(b)
                    HEALTH -= 1
                else:
                    bugs.remove(b)
                    HEALTH += 1
                
        for b in bugs:
            for i in bullets:
                if b.iscolliding(i):
                    if (not b.heart):    
                        bullets.remove(i)
                        bugs.remove(b)
                        SCORE += 1
                    else:
                        bullets.remove(i)
                        bugs.remove(b)
                        HEALTH +=1
                        SCORE+=2

            if b.position[1] > HEIGHT:
                bugs.remove(b)
                if not b.heart:
                    HEALTH -=1
        
        if (difficulty == 0):
            if (HEALTH > 5):
                HEALTH = 5
        if (difficulty ==1):
            if (HEALTH > 3):
                HEALTH = 3
        
        if HEALTH == 0:
            run = False

        draw(bullets,bugs,SCORE,HEALTH)

    while end_screen :

        clock.tick(FPS)
        WIN.fill((200,200,200))

        fnt = font.render("PLAY AGAIN",1,(50,50,50))

        x1 =round(WIDTH/2 -fnt.get_width()/2-20)
        y1 =round(HEIGHT/2 - fnt.get_height()/2-10)
        x2=round(fnt.get_width()+40)
        y2=round(fnt.get_height()+20)

        pygame.draw.rect(WIN,(0,200,0),[x1,y1,x2,y2])
        pygame.draw.rect(WIN,(0,0,0),[x1,y1,x2,y2],1)
        WIN.blit(fnt,(round(WIDTH/2 -fnt.get_width()/2),round(HEIGHT/2 - fnt.get_height()/2)))



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                end_screen = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if (pos[0]>x1 and pos[0]< x1+x2):
                    if(pos[1]>y1 and pos[1]<y1+y2):
                        end_screen = False
                        player.left = False
                        player.right = False
                        main()
        

        fnt =font.render("SCORE : " + str(SCORE),1,(50,50,50))

        WIN.blit(fnt,(round(WIDTH/2 - fnt.get_width()/2),round(HEIGHT/4 -fnt.get_height()/2)))




        pygame.display.update()



if __name__ == '__main__':
    main()