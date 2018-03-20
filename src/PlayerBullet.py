import pygame

from spriteSheetToList import *

class PlayerBullet:
    def __init__ (self, position):
        self.image = pygame.image.load("dorito.png")
        self.image = spriteSheetToList(self.image, 1)
        self.mask = pygame.mask.from_surface(self.image[0])
        self.rect = self.image[0].get_rect()

        self.speed = 5
        self.rect.center = position

        self.count = 0
        self.updateCount = 0

    def draw(self, screen):
        screen.blit(self.image[self.count%len(self.image)], self.rect)
        self.updateCount +=1
        if self.updateCount%5  ==0:
            self.count +=1

    def update(self):
        self.rect.y -= self.speed

    def offs(self):
        if self.rect.bottom <=  0:
            return True
        else:
            return False
        
        
        
