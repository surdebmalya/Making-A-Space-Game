import pygame
import random
import math
import sys
from pygame import mixer
pygame.init()
bg=pygame.image.load('bg.png')
icon=pygame.image.load('alien.png')
player_ship=pygame.image.load('ship.png')
bullet=pygame.image.load('bullet.png')

screenWidth,screenHeight=598,360

playerX=(screenWidth//2)-32
playerY=(screenHeight-10)-64
playerX_change=0
playerVelocity=3

enemy_ship=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemy=3

for i in range(no_of_enemy):
    enemy_ship.append(pygame.image.load('ufowithalien.png'))
    enemyX.append(random.randint(0,screenWidth-64))
    enemyY.append(random.randint(10,(screenHeight//3)-64))
    enemyX_change.append(2)
    enemyY_change.append(30)

bulletX=0
bulletY=(screenHeight-10)-64
bulletX_change=0
bulletY_change=3
bullet_state="ready"

score_value=0
font=pygame.font.Font('freesansbold.ttf',20)
textX=10
textY=10
gameOverFont=pygame.font.Font('freesansbold.ttf',32)

def game_over_text():
    over_text=gameOverFont.render("GAME OVER",True,(66, 105, 211))
    win.blit(over_text,(200,140))

def show_score(x,y):
    score=font.render("Score :"+str(score_value),True,(0,150,0))
    win.blit(score,(x,y))

def player(x,y):
    win.blit(player_ship,(x,y))

def enemy(x,y,i):
    win.blit(enemy_ship[i],(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    win.blit(bullet,(x+16,y+10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt(pow(enemyX-bulletX,2)+pow(enemyY-bulletY,2))
    if distance<27:
        return True
    return False

def redraw():
    global bulletY
    global bulletVelocity
    global bullet_state
    if bulletY<=0:
        bulletY=(screenHeight-10)-64
        bullet_state="ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletVelocity
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

win=pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Space Game")
pygame.display.set_icon(icon)
enemyVelocity=enemyX_change[0]
bulletVelocity=bulletY_change

LoadingFont=pygame.font.Font('freesansbold.ttf',64)
for i in range(3000):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    if i<=1000:
        win.fill((152,93,38))
        load_text=LoadingFont.render("Loading .",True,(0, 0, 0))
        win.blit(load_text,(150,140))
    elif i>1000 and i<=2000:
        win.fill((152,93,38))
        load_text=LoadingFont.render("Loading ..",True,(0, 0, 0))
        win.blit(load_text,(150,140))
    else:
        win.fill((152,93,38))
        load_text=LoadingFont.render("Loading ...",True,(0, 0, 0))
        win.blit(load_text,(150,140))
    pygame.display.update()
RuleFont=pygame.font.Font('freesansbold.ttf',32)
otherFont=pygame.font.Font('freesansbold.ttf',20)
for i in range(1000):
    win.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    if i<=50:
        rule_text=RuleFont.render(" Rules :",True,(255, 255, 255))
        win.blit(rule_text,(20,20))
    elif i>50 and i<=300:
        rule_text=RuleFont.render(" Rules :",True,(255, 255, 255))
        win.blit(rule_text,(20,20))
        other_text=otherFont.render(" 1. Press 'A' or '<-': Space Ship Will Move Towards Left",True,(66, 105, 211))
        win.blit(other_text,(20,80))
    elif i>300 and i<=550:
        rule_text=RuleFont.render(" Rules :",True,(255, 255, 255))
        win.blit(rule_text,(20,20))
        other_text=otherFont.render(" 1. Press 'A' or '<-': Space Ship Will Move Towards Left",True,(66, 105, 211))
        win.blit(other_text,(20,80))
        other_text=otherFont.render(" 2. Press 'D' or '->': Space Ship Will Move Towards Right",True,(66, 105, 211))
        win.blit(other_text,(20,120))
    elif i>550 and i<=800:
        rule_text=RuleFont.render(" Rules :",True,(255, 255, 255))
        win.blit(rule_text,(20,20))
        other_text=otherFont.render(" 1. Press 'A' or '<-': Space Ship Will Move Towards Left",True,(66, 105, 211))
        win.blit(other_text,(20,80))
        other_text=otherFont.render(" 2. Press 'D' or '->': Space Ship Will Move Towards Right",True,(66, 105, 211))
        win.blit(other_text,(20,120))
        other_text=otherFont.render(" 3. If Enemy Reaches The Red Line, The Game Will Over",True,(66, 105, 211))
        win.blit(other_text,(20,160))
    else:
        rule_text=RuleFont.render("Let's Begin",True,(0, 255, 0))
        win.blit(rule_text,(200,140))
    pygame.display.update()
mixer.music.load('bg.wav')
mixer.music.play(-1)
run=True
while run:
    win.blit(bg,(0,0))
    x=0
    for i in range(screenWidth+1):
        y=(screenHeight-10)-70
        pygame.draw.circle(win,(220,60,20),(x,y),1)
        x+=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT or event.key==pygame.K_a:
                playerX_change=-playerVelocity
            if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
                playerX_change=playerVelocity
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound=mixer.Sound('shoot.wav')
                    bullet_sound.play()
                    bulletX=playerX
                    fire_bullet(bulletX,bulletY)    
        if event.type==pygame.KEYUP:
            playerX_change=0
    playerX+=playerX_change
    if playerX<=0:
        playerX=0
    elif playerX>=screenWidth-64:
        playerX=screenWidth-64
    for i in range(no_of_enemy):
        if enemyY[i]>=(screenHeight-144):
            for j in range(no_of_enemy):
                enemyY[j]=2000
            game_over_text()
            break
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=enemyVelocity
            enemyY[i]+=enemyY_change[i]
        elif enemyX[i]>=screenWidth-64:
            enemyX_change[i]=-enemyVelocity
            enemyY[i]+=enemyY_change[i]
        collision=isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            explosion_sound=mixer.Sound('bomb.wav')
            explosion_sound.play()
            bulletY=(screenHeight-10)-64
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,screenWidth-64)
            enemyY[i]=random.randint(10,(screenHeight//3)-64)
        enemy(enemyX[i],enemyY[i],i)
    redraw()
pygame.quit()
