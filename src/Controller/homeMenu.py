import pygame

#from gameController import *

def loadMainMenuImage():
    #Background main menu
    bg_menu = pygame.image.load('../images/menu.png')
    bg_menu = pygame.transform.scale(bg_menu, (500, 500))
    return bg_menu

# for the button on the main menu
def buttons_intro(screen, font):
  mouse_position = pygame.mouse.get_pos()
  mouse_clicked = pygame.mouse.get_pressed()

  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
  # the play button
  if 213 < mouse_position[0] and mouse_position[0] < 213+100 and 327 < mouse_position[1] and mouse_position[1] < 327+50:
    if mouse_clicked[0] == 1:
      return "Play"
  #pygame.draw.rect(screen, (255, 255, 255),(215,327,70,30))

  # the quit button
  if 372 < mouse_position[0] and mouse_position[0] < 372+100 and 327 < mouse_position[1] and mouse_position[1] < 327+50:
    if mouse_clicked[0] == 1:
      return "Quit"

  # text on buttons
  screen.blit(font.render('Play!', True, (0,0,0)), (223, 337))
  screen.blit(font.render('Quit!', True, (0,0,0)), (385, 337))
  
  return None

# controller for the main menu
def game_intro(screen, font):
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    bg_menu = loadMainMenuImage()
    screen.blit(bg_menu, (0, 0))
    action = buttons_intro(screen, font)

    if action == "Play" or action == "Quit":
      running = False
      return action

    pygame.display.update()

