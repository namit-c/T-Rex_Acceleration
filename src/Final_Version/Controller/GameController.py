"""@package docstring
Documentation for this module.
 
Game Controller class
Author: Dev^(enthusiases)
This class is responsible for controlling the flow of the application. It calls 
view and model modules while handling the user input.
"""

import pygame
from time import *
import MenuController
import sys
sys.path.insert(1, '../Model/')      # For importing modules from the Model directory
import Character
import Obstacle
import Powerups
import DetectCollision
import UpdateEnvironment
import Score
sys.path.insert(1, '../View')      # For importing modules from the View directory
import DisplayObstacle
import DisplayPowerups
import DisplayEnvironment
import DisplayWindow
import DisplayCharacter
import PlaySound
import DisplayMenu
import LoadAssets


## This class is the controller class for the entire game
class GameController():

    ## Contructor to initialize the necessary state variables
    def __init__(self):
        screen = DisplayWindow.DisplayWindow()    # Making a DisplayWindow object
        assets = LoadAssets.LoadAssets()       # Making a LoadAssets object
        self.__game_screen = screen.get_game_screen()   # Assigning the game display
        self.__obstacle_list = []
        self.__powerup_list = []
        
        self.__character = Character(self.__game_screen, assets.load_character()[0])
        # background music 

        #####---------------
        self.__floor = assets.load_floor()
        self.__floor_position = 0
        self.__background = assets.load_background()
        self.__score_count = Score()

    ## Method that checks the user input
    def check_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.__character.duck()
                if event.key == pygame.K_UP:
                    self.__character.jump()
                if event.key == pygame.K_p:
                    MenuController.pause_menu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__character.stand()

    ## The method that controls the flow of the game
    def game_loop(self):
        pygame.init()
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 30)
        running = True
        bg_rgb = [153, 255, 255]

        # Defining Variables for the view methods
        display_obstacles = DisplayObstacle(self.__game_screen)
        display_character = DisplayCharacter(self.__game_screen, self.__character)
        display_environment = DisplayEnvironment(self.__game_screen)
        display_powerups = DisplayPowerups(self.__game_screen)
        instructions = "To play: Jump is Up Arrow, Duck is Down Arrow"
        
        # The game loop
        while running: 
            clock.tick(45)

            # Drawing environment elements
            display_environment.draw_background(self.__background, self.__game_screen)
            display_environment.draw_floor(self.__floor, self.__floor_position)
            if(time() - self.__score_count.get_start_time() <= 5):
                display_environment.draw_instruction(instructions) 
            display_environment.draw_score(self.__score_count)

game = GameController()
game.game_loop()