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

##
# @file GameController.py
# @brief This class is the controller class for the entire game

class GameController():

    ## @brief Contructor that initializes the necessary state variables for the game
    #  @details Initializes all the state variables by calling appropriate classes and their methods. This
    #  includes game screen, images, game speed, music, and menu controller.
    def __init__(self):
        screen = DisplayWindow.DisplayWindow()    # Making a DisplayWindow object
        self.__game_screen = screen.get_game_screen()   # Assigning the game display
        self.__obstacle_img = LoadAssets.load_all_obstacles()
        #self.__powerup_list = pygame.sprite.Group()
        self.__sound_list = LoadAssets.load_sound()
        self.__game_speed = 10
        self.__load_character = LoadAssets.load_character()
        self.__character = Character.Character(self.__game_screen, self.__load_character[0])
      
        self.__obstacle_obj_list = list()
        for i in range(len(self.__obstacle_img)):
            width, height = self.__obstacle_img[i].get_size()
            self.__obstacle_obj_list.append(Obstacle.Obstacle("Obstacle-"+ str(i+1), width, height, self.__game_speed, self.__obstacle_img[i]))
        
        self.__play_sound = PlaySound.PlaySound(self.__sound_list)
         
        # Defining Menu controller
        self.__menu_controller = MenuController.MenuController(self.__game_screen)
 
        self.__pause_time = 0 

        # Load Menu
        self.__main_menu_img = LoadAssets.load_main_menu()
        self.__pause_menu_img = LoadAssets.load_pause_menu()
        self.__end_menu_img = LoadAssets.load_end_menu()
        self.__setting_menu_img = LoadAssets.load_settting_menu()
        self.__instruction_menu_img = LoadAssets.load_instruction_menu()
        # background music 

        self.__play_sound.play_bg_music()

        #####---------------
        self.__floor = LoadAssets.load_floor()
        self.__floor_position = 0
        self.__background = LoadAssets.load_background()
        self.__score_count = Score.Score()
        self.__obstacle_pos_x = 900
        self.__obstacle_pos_y = 500

        self.__is_paused = False

        self.__powerups_instruction = 0
    
    ## @brief Method that checks the user input
    #  @details Checks for the user input and decided the next action based on that input. This includes
    #  game controls, inputs reciveved from menu controller, and quitting the game. 
    #  @param game_start_time the time that current game started
    def check_user_input(self, game_start_time):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.__character.duck(self.__load_character[2])
                    if self.__character.get_ducking():
                        self.__play_sound.play_duck_sound()
                if event.key == pygame.K_UP:
                    if not self.__character.get_jumping() or (self.__character.get_double_jumping() and self.__character.get_limit() < 3):
                        self.__play_sound.play_jump_sound()
                    self.__character.jump(self.__load_character[1])
                if event.key == pygame.K_p:
                    self.__is_paused = True
                    self.__pause_time = time()
                    user_response = self.__menu_controller.pause_menu(self.__pause_menu_img)
                    if (user_response == "Resume"):
                        self.__pause_time = time() - self.__pause_time
                        return user_response
                    elif (user_response == "Quit"):
                        return user_response
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.__character.stand(self.__load_character[0])

    ## @brief The method that controls the flow of the game
    #  @details Makes variables for all the game elements to be displayed onto the screen. Contains
    #  a loop that continously updates the game screen based on the user input and the next state. Also 
    #  responsible for communicating with the View and Model modules to update the view and get next state. 
    #  @param game_start_time the time the current game started
    def game_loop(self, clock, game_start_time):
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
        instructions = "UP: Jump\n DOWN: Duck"
        update_environment = UpdateEnvironment.UpdateEnvironment()
        
        obstacle_spawn_time = time() 
        # The game loop
        while running: 
            clock.tick(45)

            # Drawing environment elements
            display_environment.draw_background(self.__background, bg_rgb)
            display_environment.draw_floor(self.__floor, self.__floor_position)
            if(time() - instruction_time <= 7):
                display_environment.draw_instruction(instructions)
            display_environment.draw_score(self.__score_count.get_current_score(), clock)

            if self.__character.is_powered() and time() - self.__powerups_instruction < 5:
                display_environment.draw_powerup(round(5 - time() + self.__powerups_instruction))
            # Drawing character
            display_character.draw_character()

            # Check user inputs
            user_response = self.check_user_input(game_start_time)
            
            start_time = None
            if (user_response == "Resume"):
                self.__is_resume = True
                start_time = time()
                for obstacle in display_obstacles.get_obstacle_list() :
                    obstacle.set_speed(0)
                
                for i in range(len(self.__obstacle_obj_list)):
                    self.__obstacle_obj_list[i].set_speed(0)

                powerup_speed_list = list()
                for powerup in display_powerups.get_powerups_list():
                    powerup_speed_list.append(powerup.get_speed())
                    powerup.set_speed(0)
                
                current_time = time()
                while (current_time - start_time <= 5):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_DOWN:
                                pass

                    display_environment.draw_background(self.__background, bg_rgb)
                    display_environment.draw_floor(self.__floor, self.__floor_position)

                    display_character.draw_character()
                    display_powerups.update_powerups(self.__obstacle_obj_list)
                    display_obstacles.update_obstacle_display()

                    self.__menu_controller.resume_menu(5 - (current_time - start_time))

                    current_time = time()
                    pygame.display.update()

                    if self.__character.is_powered() and time() - self.__powerups_instruction < 5:
                        display_environment.draw_powerup(round(5 - time() + self.__powerups_instruction))
 

                current_obstacle_list = display_obstacles.get_obstacle_list()
                for element in current_obstacle_list:
                    element.set_speed(self.__game_speed)

                for i in range(len(self.__obstacle_obj_list)):
                    self.__obstacle_obj_list[i].set_speed(self.__game_speed)

                current_powerup_list = display_powerups.get_powerups_list()
                for element in current_powerup_list:
                    element.set_speed(self.__game_speed)

                self.check_user_input(game_start_time)
                
                game_start_time += self.__pause_time + 5
                
                # Updating obstacle_spawn time to prevent another obstacle spawning immediately
                obstacle_spawn_time = time() 

                
            elif(user_response == "Quit"):
                running = False

            # Generate Obstacle
            
            if (self.__is_paused == False):
                obstacle_spawn_time = display_obstacles.generate_obstacle(self.__obstacle_pos_x, \
                    self.__obstacle_pos_y, self.__obstacle_obj_list, obstacle_spawn_time,display_powerups.get_powerups_list()) 
            
            # Generate powerups
            display_powerups.generate_powerups(-self.__game_speed, self.__obstacle_obj_list, obstacle_spawn_time)
            display_powerups.draw_powerups(display_powerups.get_powerups_list())
            # update objects
            current_score, prev_score = self.__score_count.update_score(game_start_time)
            update_environment.update_bg_colour(current_score, prev_score, bg_rgb)
            self.__character.update(self.__load_character[0])
            self.__floor_position = update_environment.update_floor(self.__floor_position, self.__game_speed)
            display_powerups.update_powerups(self.__obstacle_obj_list)
            display_obstacles.update_obstacle_display()

        
            # Detect collision (powerups)
            powerups_taken = DetectCollision.find_collision_powerups(self.__character, display_powerups.get_powerups_list())
            if powerups_taken:
                if powerups_taken.get_name() < 3:
                    self.__powerups_instruction = time()

                self.__play_sound.play_powerup_sound()
                if powerups_taken.get_name() == 0:
                    self.__character.invincible()
                elif powerups_taken.get_name() == 1:
                    self.__character.double_jump()
                elif powerups_taken.get_name() == 2:
                    self.__character.slo_mo()
                else:
                    self.__score_count.boost()
                display_powerups.remove_powerups(powerups_taken)


            # Detect collison (obstacles)
            is_obstacle_collision = DetectCollision.find_collision_obstacle(self.__character, display_obstacles.get_obstacle_list())
            #print(is_obstacle_collision)
            if (is_obstacle_collision != None and not self.__character.get_invincible()):
                running = False
                self.__play_sound.play_game_over_sound()
                self.__menu_controller.end_menu(current_score, self.__score_count.get_score() ,self.__end_menu_img)
                self.__score_count.reset_score()
                self.__game_speed = 10
                self.__character.reset(self.__load_character[0])
            elif (is_obstacle_collision != None and self.__character.get_invincible()): 
                display_obstacles.remove_obstacle(is_obstacle_collision)
                self.__play_sound.play_collision_sound()
            
            if (self.__is_paused == True):
                self.__pause_time = 0
                self.__is_paused = False

            self.increase_game_speed(display_powerups)
            pygame.display.update()

    ## @brief increases the game speed when the score reaches a specific value. It will also update the speed of all
    #  other obstacles and powerups.
    #  @param powerups a list of Powerups objects
    def increase_game_speed(self, powerups):
        score = self.__score_count.get_current_score()
        #if (score != 0 and score % 50 == 0 and self.__game_speed <= 15):
        if self.__character.get_slo_mo():
            self.__game_speed = 10
        else:
            self.__game_speed = 0.5*(score // 50) + 10

        for obstacle in self.__obstacle_obj_list:
            obstacle.set_speed(self.__game_speed)
        powerups.update_speed(-self.__game_speed)

    ## @brief handles the control flow for the main menu, handling all the events for selecting different 
    #  menus such as the setting menu, instruction menu. Also handles the event for the user wanting to start a game
    #  @param font takes into the system font to be used through most parts in game session
    #  @return return the string of the action of whether the user wants to play the game or quit 
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
                    elif event.key == pygame.K_q:
                        self.__play_sound.stop_music()
                        running = False
                    elif event.key == pygame.K_s:
                        self.__menu_controller.setting_menu(self.__play_sound, self.__setting_menu_img)
                    elif event.key == pygame.K_h:
                        self.__menu_controller.instruction_menu(self.__instruction_menu_img)


            display_menu = DisplayMenu.DisplayMenu(self.__game_screen)
            display_menu.display_main_menu(self.__main_menu_img)
            self.__score_count.reset_score()
            if action == "Play" or action == "Quit":
              running = False
              return action

            pygame.display.update()
    
    ## @brief handles the control flow of starting the actual game session or exiting the game application. Initializes 
    # the pygame library and sets various settings such as the clock and font for the game.
    def run_game(self):
        pygame.init()
                
        clock = pygame.time.Clock()

        font = pygame.font.Font("../assets/Acceleration-Reaction.ttf", 30)

        running = True

        while running:
            action = self.main_menu(font)

            if action == "Play":
                game_start_time = time()
                self.game_loop(clock, game_start_time)
            else:
                running = False

        
game = GameController()
game.run_game()
