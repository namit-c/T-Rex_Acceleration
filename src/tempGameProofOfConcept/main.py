import pygame
from Dino import *
import sys

from DisplayObstacle import *
from Obstacle import *
import DetectCollision
# methods

# Colours
RED = (255, 0, 0)
DARKER_RED = (200, 0, 0)
GREEN = (0, 255, 0)
DARKER_GREEN = (0, 200, 0)
BLUE = (0, 0, 255)

# clouds
clouds = pygame.image.load("clouds.png")
clouds = pygame.transform.scale(clouds, (70, 70))
clouds2 = pygame.image.load("clouds.png")
clouds2 = pygame.transform.scale(clouds, (70, 70))

# clouds 
def blit_alpha(target, source, location, opacity):
  x = location[0]
  y = location[1]
  temp = pygame.Surface((source.get_width(), source.get_height())).convert()
  temp.blit(target, (-x, -y))
  temp.blit(source, (0, 0))
  temp.set_alpha(opacity)        
  target.blit(temp, location)

def draw_floor():
  screen.blit(floor, (floor_position, 410))
  screen.blit(floor, (floor_position+490, 410))
  #screen.blit(floor, (floor_position+820, 410))

	#screen.blit(floor, (floor_position, 410))
	#screen.blit(floor, (floor_position+410, 410))
  #screen.blit(floor, (floor_position, 410))
  # screen.sblit(floor, (floor_position+820, 410))

# for the button on the main menu
def buttons_intro():
  mouse_position = pygame.mouse.get_pos()
  mouse_clicked = pygame.mouse.get_pressed()

  # the play button
  if 100 < mouse_position[0] and mouse_position[0] < 100+100 and 350 < mouse_position[1] and mouse_position[1] < 350+50:
    pygame.draw.rect(screen, GREEN,(100,350,100,50))
    if mouse_clicked[0] == 1:
      game_loop()
  else: 
    pygame.draw.rect(screen, DARKER_GREEN,(100,350,100,50))

  # the quit button
  if 300 < mouse_position[0] and mouse_position[0] < 300+100 and 350 < mouse_position[1] and mouse_position[1] < 350+50:
    pygame.draw.rect(screen, RED,(300,350,100,50))
    if mouse_clicked[0] == 1:
      pygame.quit()
  else: 
    pygame.draw.rect(screen, DARKER_RED,(300,350,100,50))

  # text on buttons
  screen.blit(font.render('Play!', True, (0,0,0)), (110, 360))
  screen.blit(font.render('Quit!', True, (0,0,0)), (310, 360))
  
  return True

# controller for the main menu
def game_intro():
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    screen.fill((255, 255, 255))
    intro_text = font.render("T-Rex Acceleration", True, (0, 0, 0))
    screen.blit(intro_text, (85, 200))
    running = buttons_intro()
    pygame.display.update()



pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

# loading the floor
floor = pygame.image.load('ground.png')
floor = pygame.transform.scale(floor, (547, 130))
floor_position = -26

#cactus 
#cactus = pygame.image.load('cactus.png')
#cactus = pygame.transform.scale(cactus, (75, 75))
#position = 450

#character
#character = pygame.image.load('tyrannosaurus.png')
#character = pygame.transform.scale(character, (70, 70))

# intro screen
# game_intro()


obstacle = Obstacle("Cactus", 120, 60, 10, 'cactus.png') 
obstacle_2 = Obstacle("Cactus", 240, 60, 10, 'cactus_2.png')

displayObstacle = DisplayObstacle(screen)


# Game loop
def game_loop():
  running = True
  dino = Dino(screen)

  characterDimension = [dino.rect.width, dino.rect.height]

  obstaclePosX = 500 + 100 #Starting slightly outside the window
  obstaclePosY = 385  #Starting towards the bottom of Window as a fixed position

  score = 0
  startTime = time.time()
  obstacleSpawnTime = time.time()

  RGB = [153,255,255]
  
  prevScore = -1

  while running:
    clock.tick(30)
    screen.fill((RGB[0], RGB[1], RGB[2]))

    if (round(prevScore) != round(score) and round(score) % 5 == 0 and round(score) != 0):
        randomRGBChange = randint(1,3)
        if (randomRGBChange == 1):
            RGB[0] = (RGB[0] + 50) % 255
        elif (randomRGBChange == 2):
            RGB[1] = (RGB[1] + 50) % 255
        else:
            RGB[2] = (RGB[2] + 50) % 255
        screen.fill((RGB[0], RGB[1], RGB[2]))
    
    obstacleSpawnTime = displayObstacle.generateRandomObstacle(obstaclePosX, obstaclePosY, obstacle, obstacle_2 , obstacleSpawnTime)

    prevScore = score
    score = time.time() - startTime

    displayObstacle.displayMsg("Current Score is: " + str(round(score)), (0,100))
    displayObstacle.displayMsg("FPS: " + str(int(clock.get_fps())), (0,300)) 
    
    for i in displayObstacle.getObstacleList():
      i[0] -=  i[2].getSpeed()
      if i[3] == 1:
        displayObstacle.drawObstacle(i[0],i[1],i[2])
      else:
        displayObstacle.drawObstacle(i[0],i[1],i[2])
        displayObstacle.drawObstacle(i[0] + i[2].getWidth(), i[1], i[2])


      characterPosY = dino.rect.bottom

      isCollision = DetectCollision.DetectCollision(100,characterPosY,characterDimension,i[0],i[1],i[2])
      if isCollision == True:
        print("COLLISION OCCURED")

        displayObstacle.displayMsg('Game Over: Collison with obstacle', (0,0))
        pygame.display.update()
        time.sleep(2)
        game_intro()

        
      if i[0] < -100:
        displayObstacle.getRemoveObstacle(i)

    dino.update()
    
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
    # Moving Floor	
    #screen.blit(floor, (-26, 200))
    
    #character on screen
#    screen.blit(character, (100, 385))
    global floor_position
    floor_position -= 8
    draw_floor()
    if floor_position <= -520:
      floor_position = -26
    dino.blitme()
    #cactus / obstacle
#    position -= 8
#    screen.blit(cactus, (position, 375))
    blit_alpha(screen, clouds, (50, 100), 100)
    blit_alpha(screen, clouds2, (400, 200), 50)
    pygame.display.update()

game_intro()
#game_loop()
pygame.quit()
