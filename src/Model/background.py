import pygame
def loadFloor():
    # loading the floor
    floor = pygame.image.load('../images/ground.png')
    floor = pygame.transform.scale(floor, (500, 117))
    floor_position = -26

    return floor, floor_position

def loadBackground():
    bg = pygame.image.load('../images/background.png')
    bg = pygame.transform.scale(bg, (500, 500))

    return bg

def draw_floor(floor,floor_position,  screen):
  screen.blit(floor, (floor_position, 410))
  screen.blit(floor, (floor_position+500, 410))

def updateFloor(floor, floor_position, screen):
    floor_position -= 8
    draw_floor(floor, floor_position, screen)
    if floor_position <= -500:
      floor_position = 0
    
    return floor_position