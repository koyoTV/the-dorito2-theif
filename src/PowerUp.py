import pygame, random


class PowerUp:
    def __init__ (self, width, speed):
        self.image = pygame.image.load("mdew.png")
        self.rect = self.image.get_rect()
        neww = self.image.get_width()
        newh=self.image.get_height()
        self.image = pygame.transform.scale(self.image, [int(neww//4), int(newh//4)])
        self.mask = pygame.mask.from_surface(self.image)

        self.speed = 5

        self.count = 0

        self.rect.x = random.randint(0, width)
        self.rect.bottom = 0

        self.updateCount = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        self.updateCount +=1
        if self.updateCount%5  ==0:
            self.count +=1

    def update(self):
        self.rect.y += 1

    def offs(self, height):
        if self.rect.bottom <=  0 or self.rect.top > height:
            return True
        else:
            return False

    def collision(self, player):
        offsetX = player.rect.left - self.rect.left
        offsetY = player.rect.top - self.rect.top
        if self.mask.overlap(player.mask, (offsetX, offsetY)) !=None:
            return True
        else:
            return False


        
        
        
        
