import pygame
import random
from Dino import *
from Powerups import *

def generatePowerUp(powerups, dino, screen):
    if(random.random() < 0.003):
      powerup = Powerups(screen)
      powerups.add(powerup)
    for element in powerups:
      element.blitme()
      element.update()
    P = pygame.sprite.spritecollideany(dino, powerups)
    if P:
      dino.invincible()
      powerups.remove(P)