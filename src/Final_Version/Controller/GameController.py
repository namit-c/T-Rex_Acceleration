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
import DisplayMenu
import PlaySound
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
        self.__sound_list = assets.load_sound()

        self.__load_character = assets.load_character()
        self.__character = Character.Character(self.__game_screen, self.__load_character[0])
      
        self.__obstacle_obj_list = list()
        for i in range(len(self.__obstacle_img)):
            width, height = self.__obstacle_img[i].get_size()
            self.__obstacle_obj_list.append(Obstacle.Obstacle(" ", width, height, 10, self.__obstacle_img[i]))

        self.__play_sound = PlaySound.PlaySound(self.__sound_list)
       
        # Defining Menu controller
        self.__menu_controller = MenuController.MenuController(self.__game_screen)
 

        # Load Menu
        self.__main_menu_img = assets.load_main_menu()
        self.__pause_menu_img = assets.load_pause_menu()
        self.__end_menu_img = assets.load_end_menu()
        # background music 

        #####---------------
        self.__floor = assets.load_floor()
        self.__floor_position = 0
        self.__background = assets.load_background()
        self.__score_count = Score.Score()
        self.__obstacle_pos_x = 800
        self.__obstacle_pos_y = 500

        self.__is_paused = False
    ## Method that checks the user input
    def check_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.__character.duck(self.__load_character[2], self.__load_character[1])
                    self.__play_sound.play_duck_sound()
                if event.key == pygame.K_UP:
                    self.__character.jump(self.__load_character[2],self.__load_character[1])
                    self.__play_sound.play_jump_sound()
                if event.key == pygame.K_p:
                    self.__is_paused = True
                    user_response = self.__menu_controller.pause_menu(self.__pause_menu_img)
                    if (user_response == "Resume"):
                        return user_response
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__character.stand(self.__load_character[2], self.__load_character[0])

    ## The method that controls the flow of the game
    def game_loop(self, clock):
        #pygame.init()
        
        #clock = pygame.time.Clock()
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
        self.__play_sound.play_bg_music()
        # The game loop
        while running: 
            clock.tick(45)

            # Drawing environment elements
            display_environment.draw_background(self.__background, bg_rgb)
            display_environment.draw_floor(self.__floor, self.__floor_position)
            if(time() - instruction_time <= 5):
                display_environment.draw_instruction(instructions)
            display_environment.draw_score(self.__score_count.get_current_score())

            # Drawing character
            display_character.draw_character()

            # Drawing obstacles
            obstacle_spawn_time = display_obstacles.generate_obstacle(self.__obstacle_pos_x, self.__obstacle_pos_y, self.__obstacle_obj_list, obstacle_spawn_time) 
            # Check user inputs
            user_response = self.check_user_input()
            obstacle_speed_list = None
            powerup_speed_list = None
            
            start_time = None
            if (user_response == "Resume"):
                start_time = time()
                obstacle_speed_list = list()
                for obstacle in display_obstacles.get_obstacle_list() :
                    obstacle_speed_list.append(obstacle.get_speed())
                    obstacle.set_speed(0)

                powerup_speed_list = list()
                for powerup in display_powerups.get_powerups_list():
                    powerup_speed_list.append(powerup.get_speed())
                    powerup.set_speed(0)
                
                current_time = time()
                while (current_time - start_time <= 5):
                    #self.__menu_controller.resume_menu()
                    display_environment.draw_background(self.__background, bg_rgb)
                    display_environment.draw_floor(self.__floor, self.__floor_position)

                    display_character.draw_character()
                    display_powerups.update_powerups()
                    display_obstacles.update_obstacle_display()

                    self.__menu_controller.resume_menu(5 - (current_time - start_time))

                    current_time = time()
                    pygame.display.update()
                
                current_obstacle_list = display_obstacles.get_obstacle_list()
                for i in range(len(current_obstacle_list)):
                    current_obstacle_list[i].set_speed(obstacle_speed_list[i])


                current_powerup_list = display_powerups.get_powerups_list()
                index = 0
                for element in current_powerup_list:
                    element.set_speed(powerup_speed_list[index])
                    index += 1


                self.__is_paused = False

                

            # Generate powerups
            display_powerups.generate_powerups(-10)

            # update objects
            current_score, prev_score = self.__score_count.update_score()
            update_environment.update_bg_colour(current_score, prev_score, bg_rgb)
            self.__character.update(self.__load_character[0])
            self.__floor_position = update_environment.update_floor(self.__floor_position, 10)
            display_powerups.update_powerups()
            display_obstacles.update_obstacle_display()

        
            # Detect collision (powerups)
            powerups_taken = DetectCollision.find_collision(self.__character, display_powerups.get_powerups_list())
            if powerups_taken:
                if powerups_taken.get_name() == 0:
                    self.__character.invincible(self.__load_character[2])
                elif powerups_taken.get_name() == 1:
                    self.__character.double_jump()
                elif powerups_taken.get_name() == 2:
                    self.__character.slo_mo()
                display_powerups.remove_powerups(powerups_taken)


            # Detect collison (obstacles)
            is_obstacle_collision = DetectCollision.find_collision_obstacle(self.__character, display_obstacles.get_obstacle_list())
            #print(is_obstacle_collision)
            if (is_obstacle_collision != None and not self.__character.is_invincible):
                running = False
                self.__menu_controller.end_menu(current_score, self.__score_count.get_score() ,self.__end_menu_img)
                self.__score_count.reset_score() 
            elif (is_obstacle_collision != None and self.__character.is_invincible): 
                display_obstacles.remove_obstacle(is_obstacle_collision)


            pygame.display.update()

    def main_menu(self, font):
        running = True
        while running:
            action = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        action = "Play"

            
            display_menu = DisplayMenu.DisplayMenu(self.__game_screen)
            display_menu.display_main_menu(self.__main_menu_img)
            self.__score_count.reset_score()
            if action == "Play" or action == "Quit":
              running = False
              return action

            pygame.display.update()
    
    def run_game(self):
        pygame.init()
                
        clock = pygame.time.Clock()

        font = pygame.font.Font("../assets/Acceleration-Reaction.ttf", 30)

        running = True

        while running:
            action = self.main_menu(font)

            if action == "Play":
                self.game_loop(clock)
            else:
                running = False


game = GameController()
game.run_game()
