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
        self.__obstacle_img = assets.load_all_obstacles()
        #self.__powerup_list = pygame.sprite.Group()
        
        self.__load_character = assets.load_character()
        self.__character = Character.Character(self.__game_screen, self.__load_character[0])
      
       
        #temp = Obstacle.Obstacle("asda", 5,5,1, pygame.image.load('../assets/background.png'))
        
        #self.__obstacle_obj_list = list()
        #for i in range(len(self.__obstacle_img)):
        #    width, height = self.__obstacle_img[i].get_size()
        #    self.__obstacle_obj_list.append(Obstacle.Obstacle(" ", width, height, 5, self.__obstacle_img[0]))

        #self.__obstacle_obj_list.append(temp)
        # background music 

        #####---------------
        self.__floor = assets.load_floor()
        self.__floor_position = 0
        self.__background = assets.load_background()
        self.__score_count = Score.Score()
        self.__obstacle_pos_x = 600
        self.__obstacle_pos_y = 370
    ## Method that checks the user input
    def check_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.__character.duck(self.__load_character[2], self.__load_character[1])
                if event.key == pygame.K_UP:
                    self.__character.jump(self.__load_character[2],self.__load_character[1])
                if event.key == pygame.K_p:
                    MenuController.pause_menu()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__character.stand(self.__load_character[2], self.__load_character[0])

    ## The method that controls the flow of the game
    def game_loop(self):
        pygame.init()
        clock = pygame.time.Clock()
        # font = pygame.font.SysFont(None, 30)
        running = True
        bg_rgb = [153, 255, 255]
        instruction_time = time()

        # Defining Variables for the view methods
        display_obstacles = DisplayObstacle.DisplayObstacle(self.__game_screen)
        display_character = DisplayCharacter.DisplayCharacter(self.__game_screen, self.__character)
        display_environment = DisplayEnvironment.DisplayEnvironment(self.__game_screen)
        display_powerups = DisplayPowerups.DisplayPowerups(self.__game_screen)
        display_character = DisplayCharacter.DisplayCharacter(self.__game_screen, self.__character)
        instructions = "To play: Jump is Up Arrow, Duck is Down Arrow"
        update_environment = UpdateEnvironment.UpdateEnvironment()

        obstacle_spawn_time = time()

        # The game loop
        while running: 
            clock.tick(45)

            # Drawing environment elements
            display_environment.draw_background(self.__background, bg_rgb)
            display_environment.draw_floor(self.__floor, self.__floor_position)
            if(time() - instruction_time <= 5):
                display_environment.draw_instruction(instructions)
            display_environment.draw_score(self.__score_count)

            # Drawing character
            display_character.draw_character()

            # Drawing obstacles
            #obstacleSpawnTime = display_obstacles.generate_obstacle(self.__obstacle_pos_x, self.__obstacle_pos_y, self.__obstacle_obj_list, obstacle_spawn_time) 
            # Check user inputs
            self.check_user_input()

            # Generate powerups
            display_powerups.generate_powerups(-5)

            # update objects
            self.__score_count.update_score()
            self.__character.update(self.__load_character[0])
            self.__floor_position = update_environment.update_floor(self.__floor_position, 5)
            display_powerups.update_powerups()
            #display_obstacles.update_obstacle_display()

            pygame.display.update()
        
            # Detect collision
            powerups_taken = DetectCollision.find_collision(self.__character, display_powerups.get_powerups_list())
            display_powerups.remove_powerups(powerups_taken)

game = GameController()
game.game_loop()
