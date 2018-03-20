import pygame

from spriteSheetToList import *

class Player:
    def __init__ (self, width, height):
        self.health = 3
        self.screenWidth = width
        self.speed = 5
        self.image = pygame.image.load("fighter.png")
        self.icon = pygame.image.load("icon.png")
        #self.icon = pygame.transform.scale(
        self.image  = spriteSheetToList(self.image, 2)
        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()

        self.rect.midbottom = [width//2, height]
        self.count = 0
        self.updateCount = 0

        self.pUp = False
        self.pUpCount = 0
                                        
    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5  ==0:
            self.count +=1

    def update(self):
        if self.pUp == True:
            self.speed = 15
            self.pUpCount += 1
            if self.pUpCount > 600:
                self.pUp = False
                self.pUpCount = 0
        else:
            self.speed = 5
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        if self.rect.left < 0:
                self.rect.left = 0
        elif self.rect.right > self.screenWidth:
                self.rect.right = self.screenWidth
                
    def hit(self, bullet):
        xoffset = self.rect.left - bullet.rect.left
        yoffset = self.rect.top - bullet.rect.top
        return bullet.mask.overlap(self.mask, [xoffset, yoffset])
    
                

                        
