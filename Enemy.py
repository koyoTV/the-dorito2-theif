import pygame
import random

from spriteSheetToList import *

class Enemy:
    def __init__ (self, x, y, wave):
        self.speed = wave
        self.image = pygame.image.load("ptheif.png")
        newwidth = self.image.get_width() *2
        newheight = self.image.get_height() *2
        self.image = pygame.transform.scale(self.image, [newwidth, newheight])
        self.image = spriteSheetToList(self.image, 4)
        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()

        self.rect.topleft = [x, y]
        self.count = 0
        self.updateCount = 0
        self.bulletchance = 1000-100*wave
        
    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5  ==0:
            self.count +=1

    def update(self):
        self.rect.x += self.speed
        
    def isCollision(self, width):
        if self.rect.right > width or self.rect.left < 0:
            return True
        else:
            return False
        
    def shiftDown(self):
        self.speed = -self.speed
        self.rect.y += 10

    def hit(self, bullet):
        xoffset = self.rect.left- bullet.rect.left
        yoffset = self.rect.top - bullet.rect.top
        return bullet.mask.overlap(self.mask, [xoffset, yoffset])
    
    def fire(self):
        return random.randint(0,self.bulletchance) == 0
        
        
