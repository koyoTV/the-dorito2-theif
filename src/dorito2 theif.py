import pygame, sys
from Player import  *
from Enemy import Enemy
from PlayerBullet import *
from eBullet import EnemyBullet
from PowerUp import *
import sounds

pygame.init()
pygame.display.set_caption("dorito2 theif")
font = pygame.font.SysFont("Comic Sans", 30)
size = width, height= 1280, 720
screen= pygame.display.set_mode(size)
enemies = []
pBullets = []
eBullets = []
pUpList = []
player = Player(width, height)
score = 0

black= 0,0,0
white= 255,255,255

def spawn():
    for x in range(0, 350, 50):
        for y in range(0, 250, 50):
            enemy = Enemy(x, y, wave)
            enemies.append(enemy)
def getHighScore():
    file = open("highscores.txt","r")
    line = file.readline()
    high = 0
    while line != "":
        if int(line) > high:
            high =int(line)
        line = file.readline()
    return high

wave = 1
waveLabel = font.render("wave " +str(wave), False, white)
highscorelabel = font.render("high score " + str(getHighScore()), False, white)


background = pygame.image.load("background.png")
startLabel = font.render("start", False, white)
exitLabel = font.render("exit", False, white)
startRect = startLabel.get_rect()
exitRect = exitLabel.get_rect()
selectRect = player.icon.get_rect()
startRect.center = (width//2, height//2 + 150)
exitRect.center = (width//2, height //2 + 200)
startOffset = startRect.left - 10, startRect.centery
exitOffset = exitRect.left - 10, exitRect.centery
selectRect.midright = startOffset





 #nititalize phaze
clock = pygame.time.Clock()
FPS=60







gameScreen = 0


for x in range(0, 350, 50):
    for y in range(0, 250, 50):
        enemy = Enemy(x,y,2)
        enemies.append(enemy)

sounds.mutecity.play(loops = -1)

#game loop
while True:
    ##main menu
    if gameScreen == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type ==  pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selectRect.midright == startOffset:
                        selectRect.midright = exitOffset
                    else:
                        selectRect.midright = startOffset
                if event.key == pygame.K_UP:
                    if selectRect.midright == startOffset:
                        selectRect.midright = exitOffset
                    else:
                        selectRect.midright = startOffset
                if event.key == pygame.K_RETURN:
                    if selectRect.midright == startOffset:
                        gameScreen = 1
                    else:
                        pygame.quit()
                        sys.exit()
        screen.fill(black)
        screen.blit(startLabel, startRect)
        screen.blit(exitLabel, exitRect)
        screen.blit(player.icon, selectRect)
        pygame.display.flip()
        
                
                        
    if gameScreen == 1:
        
        if player.health <= 0:
            file = open("HighScores.txt", "a")
            file.write(str(score)+ "\n")
            file.close()

            gameScreen = 0
            enemies = []
            pBullets = []
            eBullets = []
            pUpList = []
            player = Player(width, height)
            wave = 1
            score = 0
          
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = PlayerBullet(player.rect.center)
                    pBullets.append(bullet)

        if len(enemies) == 0:
            wave += 1
            waveLabel = font.render("wave " +str(wave), False, white)
            spawn()

    ###user input/mothing things
        player.update()

        power = random.randint(1, 500)
        if power == 1:
            pUp = PowerUp(width, 1)
            pUpList.append(pUp)
            
        for pUp in pUpList:
            pUp.update()
            if pUp.collision(player):
                player.pUp = True
                pUpList.remove(pUp)

                


        for bullet in pBullets:
            bullet.update()


            for enemy in enemies:
                if enemy.hit(bullet):
                    score += 50
                    pBullets.remove(bullet)
                    enemies.remove(enemy)
                
                    break
                
            if bullet.offs():
                pBullets.remove(bullet)
                
        for bullet in eBullets:
            bullet.update()
            if player.hit(bullet):
                player.health -= 1
                eBullets.remove(bullet)
            if bullet.offs(height):
                eBullets.remove(bullet)

            
            
        for enemy in enemies:
            if enemy.fire():
                bullet = EnemyBullet(enemy.rect.center)
                eBullets.append(bullet)
            enemy.update()
            

        #check for bounds
        for enemy in enemies:
            if enemy.isCollision(width)==True:
                for enemy in enemies:
                    enemy.shiftDown()
                break

        ##draw phase
        screen.blit(background, [0,0])

        for bullet in pBullets:
            bullet.draw(screen)
            
        for bullet in eBullets:
            bullet.draw(screen)
        
        player.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        for pUp in pUpList:
            pUp.draw(screen)

        scoretext = font.render("Score " + str(score), False, white)
        screen.blit(scoretext, [0,0])
        livestext = font.render("Lives "+ str(player.health), False, white)
        screen.blit(livestext, [1200, 0])
        screen.blit(waveLabel, [640,0])
        screen.blit(highscorelabel, [640/2, 0])

        

        clock.tick(FPS)
                    
        pygame.display.flip()
        

