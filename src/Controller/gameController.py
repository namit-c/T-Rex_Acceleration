import pygame
from time import * 

from homeMenu import *
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '../Model')
from Dino import *
from DisplayObstacle import *
from Obstacle import *
import DetectCollision
from Powerups import *
from background import *
from score_count import *
from DisplayPowerups import *

def loadObstacles(screen):
    obstacle = Obstacle("Cactus", 70, 100, 10, '../images/cactus.png') 
    obstacle_2 = Obstacle("Cactus", 120, 100, 10, '../images/cactus_2.png')
    displayObstacle = DisplayObstacle(screen)

    return obstacle, obstacle_2, displayObstacle

def checkEvents(dino):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_DOWN:
          dino.duck()
        if event.key == pygame.K_UP:
          dino.jump()
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
          dino.stand()

def game_loop(screen):
    running = True
    dino = Dino(screen)
    powerups = pygame.sprite.Group()

    floor, floor_position = loadFloor()

    obstacle, obstacle_2, displayObstacle = loadObstacles(screen)

    obstaclePosX = 500 + 100 #Starting slightly outside the window
    obstaclePosY = 370 #Starting towards the bottom of Window as a fixed position

    score = 0
    startTime = time()
    obstacleSpawnTime = startTime

    RGB = [153,255,255]

    prevScore = -1

    bg = loadBackground()

    while running:
        clock.tick(30)
        screen.fill((RGB[0], RGB[1], RGB[2]))
        screen.blit(bg, (0,0))
        floor_position = updateFloor(floor, floor_position, screen)
        checkEvents(dino)
        
        checkScore(score,prevScore, screen, RGB)

        obstacleSpawnTime = displayObstacle.generateRandomObstacle(obstaclePosX, obstaclePosY, obstacle, obstacle_2 , obstacleSpawnTime)

        score, prevScore = updateScore(score, prevScore, startTime)

        displayObstacle.displayMsg("Current Score is: " + str(score), (250,10))
        displayObstacle.displayMsg("FPS: " + str(int(clock.get_fps())), (10,10)) 

        if (time() - startTime < 5):
            displayObstacle.displayMsg("To play: Jump is Up Arrow, Duck is Down Arrow", (25,50))


        event = displayObstacle.updateObstacleDisplay(dino, screen, obstaclePosX, score)

        if event == "Collision":
            wait(screen, font)
            running = False

        generatePowerUp(powerups, dino, screen)
        

        
        dino.update()
        pygame.display.update()


def wait(screen, font):
  while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        elif event.type == pygame.KEYDOWN:
          return
                    # This runs on any key press.


pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

running = True

while running:
    action = game_intro(screen, font)

    if action == "Play":
        game_loop(screen)
    else:
        running = False
pygame.quit()


