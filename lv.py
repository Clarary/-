import pygame
import sys
import pygame as pg
import time
from random import randint

WIDTH = 600
HEIGHT = 800
PERSON_WIDTH = 100
PERSON_HEIGHT = 80
MAO_WIDTH = 70
MAO_HEIGHT = 40
FIRST_WIDTH = 560
FIRST_HEIGHT = 250
OVER_WIDTH = 302
INTRO_WIDTH = 440
INTRO_HEIGHT = 80

fir_picture = r'.\static\first.png'
over_picture = r'.\static\over.jpg'
overs_picture = r'.\static\over_s.png'

class Obj:
    def __init__(self,picture,x,y):
        self.pic = pygame.image.load(picture)
        self.x = x
        self.y = y

def first(screen):
    picture = pygame.image.load(fir_picture)
    screen.blit(picture,[(WIDTH-FIRST_WIDTH)/2,100])
    while True:
        flag = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                flag = True
            if event.type == pygame.QUIT:
                print("退出")
                pygame.quit()
                sys.exit()
            else:
                time.sleep(0.2)
        if flag:
            break

def over(screen,score = 0):
    screen.fill((255,255,255))
    picture = pygame.image.load(over_picture)
    screen.blit(picture,[(WIDTH-OVER_WIDTH)/2,50])
    picture2 = pygame.image.load(overs_picture)
    screen.blit(picture2,[(WIDTH-FIRST_WIDTH)/2,400])
    score_font=pg.font.Font("symbol.ttf",100)
    score_sur = score_font.render(str(score),True,(106, 90, 205))
    score_rect = score_sur.get_rect()
    score_rect.center = ((WIDTH)/2,550)
    screen.blit(score_sur,score_rect)
    while True:
        flag = False
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                flag = True
            if event.type == pygame.QUIT:
                print("退出")
                pygame.quit()
                sys.exit()
            else:
                time.sleep(0.2)
        if flag:
            main(60,3,4,1.2)
    pass
	
#frequence:刷新频率，即每秒刷新次数
#mouse_speed:鼠标点击时人物移动速度
#drop_speed:绿帽下落速度
#num:每秒出现多少绿帽
def main(frequence = 60,mouse_speed = 3,drop_speed = 4,num = 1.2):
    pg.init()
    pg.font.init()
    clock = pygame.time.Clock() 
    screen=pg.display.set_mode((WIDTH,HEIGHT))
    screen.fill((255,255,255))
    pg.display.set_caption("躲绿帽")
    first(screen)
    person = Obj(r'.\static\person.jpg',(WIDTH-PERSON_WIDTH)/2,HEIGHT-PERSON_HEIGHT)
    mao = []
    print("事件循环")
    left_but = False
    right_but = False
    count = 0
    score = 0
    while True:
        screen.fill((255,255,255))
        pic = pygame.image.load(r'.\static\introduction.png')
        screen.blit(pic,[(WIDTH-INTRO_WIDTH)/2,0])
        score_font=pg.font.Font("symbol.ttf",40)
        score_sur = score_font.render(str(score),True,(0,255,0))
        score_rect = score_sur.get_rect()
        score_rect.center = ((WIDTH)/2+50,INTRO_HEIGHT*3/4+2)
        screen.blit(score_sur,score_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #print("退出")
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                left_but = True
                #print("按下左键")
            if event.type==pygame.MOUSEBUTTONDOWN and event.button == 3:
                right_but = True
                #print("按下右键")
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #print("放开左键")
                left_but = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                #print("放开右键")
                right_but = False
            else:
                #print("无事件")
                pass
        if right_but and not left_but:
            if person.x<=WIDTH-PERSON_WIDTH:
                #print(person.x)
                person.x+=mouse_speed
        if left_but and not right_but:
            if person.x>=0:
                #print(person.x)
                person.x-=mouse_speed
        if count%int(frequence/num) == 0:
            xx = randint(0,WIDTH-MAO_WIDTH)
            #print(xx)
            mao_x = Obj(r'.\static\lv.png',xx,80)
            mao.append(mao_x)
        if mao[0].y>=HEIGHT:
            mao.pop(0)
            score+=1
        #print(mao[0].y)
        if HEIGHT-PERSON_HEIGHT+5<=mao[0].y<=HEIGHT-15 and not mao[0].x>person.x+PERSON_WIDTH-20 and not mao[0].x+MAO_WIDTH<person.x+20:
            #print("GAME OVER!")
            over(screen,score)
            #break
        if count%600 == 0 and count>0:
            drop_speed+=2
            num+=0.4
        for i in mao:
            i.y +=drop_speed
            screen.blit(i.pic,[i.x,i.y])
        count+=1
        screen.blit(person.pic,[person.x,person.y])
        pygame.display.update()
        clock.tick(frequence)
		
if __name__ == "__main__":
    main(60,3,4,1.2)