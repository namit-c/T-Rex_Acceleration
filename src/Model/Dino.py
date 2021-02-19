import pygame
import time
from time import *

class Dino(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('../images/Dino.png'), (75, 75))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + 100
        self.rect.bottom = self.screen_rect.bottom - 40
        self.isDucking = False
        self.isJumping = False
        self.isDead = False
        self.isInvincible = False
        self.movement = [0,0]
        self.start_time = 0
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def duck(self):
        if self.isJumping == False:
            self.isDucking = True
            if self.isInvincible == False:
                self.image = pygame.transform.scale(pygame.image.load('../images/Dino.png'), (85, 35))
                self.rect = self.image.get_rect()
                self.rect.bottom = self.screen_rect.bottom - 40
                self.rect.left = self.screen_rect.left + 100
            else: 
                self.image = pygame.transform.scale(pygame.image.load('../images/DinoInvincible.jpg'), (85, 35))
                self.rect = self.image.get_rect()
                self.rect.bottom = self.screen_rect.bottom - 40
                self.rect.left = self.screen_rect.left + 100

    def stand(self):
        if self.isJumping == False:
            self.isDucking = False
            if self.isInvincible == False:
                self.image = pygame.transform.scale(pygame.image.load('../images/Dino.png'), (75, 75))
                self.rect = self.image.get_rect()
                self.rect.bottom = self.screen_rect.bottom - 40
                self.rect.left = self.screen_rect.left + 100
            else:
                self.image = pygame.transform.scale(pygame.image.load('../images/DinoInvincible.jpg'), (75, 75))
                self.rect = self.image.get_rect()
                self.rect.bottom = self.screen_rect.bottom - 40
                self.rect.left = self.screen_rect.left + 100

    def jump(self):
        if self.isJumping == False and self.isDucking == False:
            self.isJumping = True
            self.movement[1] = -20
    def checkbounds(self):
        if self.rect.bottom > self.screen_rect.bottom - 40:
            self.rect.bottom = self.screen_rect.bottom - 40
            self.isJumping = False
    def dead(self):
        self.isDead = True
    def invincible(self):
        self.isInvincible = True
        self.start_time = pygame.time.get_ticks()
        self.image = pygame.transform.scale(pygame.image.load('../images/DinoInvincible.jpg'), (75, 75))
        self.rect = self.image.get_rect()
        self.rect.left = self.screen_rect.left + 100
        self.rect.bottom = self.screen_rect.bottom - 40

    def update(self):
        self.blitme()
        if self.isJumping:
            self.movement[1] += 1
        self.rect = self.rect.move(self.movement)   
        self.checkbounds()
        if self.start_time + 5000 < pygame.time.get_ticks() and self.isInvincible == True and self.isDucking == False:
            self.isInvincible = False
            self.image = pygame.transform.scale(pygame.image.load('../images/Dino.png'), (75, 75))
            self.rect = self.image.get_rect()
            self.rect.left = self.screen_rect.left + 100
            self.rect.bottom = self.screen_rect.bottom - 40
        elif self.start_time + 5000 < pygame.time.get_ticks() and self.isInvincible == True and self.isDucking == True:
            self.isInvincible = False
            self.image = pygame.transform.scale(pygame.image.load('../images/Dino.png'), (85, 35))
            self.rect = self.image.get_rect()
            self.rect.left = self.screen_rect.left + 100
            self.rect.bottom = self.screen_rect.bottom - 40
