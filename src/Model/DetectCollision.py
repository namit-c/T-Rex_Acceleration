import pygame
def DetectCollision(character, obstacle):
    #print(character.rect, obstacle.rect, obstacle.getWidth(), obstacle.getHeight())

    return character.rect.colliderect(obstacle.getRect()) 

