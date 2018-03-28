import pygame, random
import PowerUp from PowerUp

class vodka(PowerUp):
    def __init__ (self, width, speed):
        super(PowerUp, self).__init__(width, speed)
        self.image = pygame.image.load("vodka.png")
        
                                       
