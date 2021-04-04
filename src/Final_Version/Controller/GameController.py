"""@package docstring
Documentation for this module.
 
Game Controller class
Author: Dev^(enthusiases)
This class is responsible for controlling the flow of the application. It calls 
view and model modules while handling the user input.
"""

import pygame
from time import *
import sys
sys.path.insert(1,'../Controller/')
import MenuController
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
    INIT_SPEED = 10
    MAX_SPEED = 30
    OBS_START_X = 900
    OBS_START_Y = 505
    INIT_BG = [153, 255, 255]
    FONTSIZE = 30
    FPS = 60 
    POWERUPS_TIME = 5
    RESUME_TIME = 5
    SPEED_FACTOR = 0.5
    SCORE_SPEED = 50

    ## @brief Contructor that initializes the necessary state variables for the game
    #  @details Initializes all the state variables by calling appropriate classes and their methods. This
    #  includes game screen, images, game speed, music, and menu controller.
    def __init__(self):
        screen = DisplayWindow.DisplayWindow()    # Making a DisplayWindow object
        self.__game_screen = screen.get_game_screen()   # Assigning the game display
        self.__obstacle_img = LoadAssets.load_all_obstacles()
        self.__sound_list = LoadAssets.load_sound()
        self.__game_speed = GameController.INIT_SPEED
        self.__load_character = LoadAssets.load_character()
        self.__character = Character.Character(self.__game_screen, self.__load_character[0])
        self.__obstacle_obj_list = list()
        for i in range(len(self.__obstacle_img)):
            width, height = self.__obstacle_img[i].get_size()
            self.__obstacle_obj_list.append(Obstacle.Obstacle("Obstacle-"+ str(i+1), width, height, self.__game_speed, self.__obstacle_img[i]))
        self.__powerup_img = LoadAssets.load_all_powerups()
        for i in range(len(self.__powerup_img)):
            self.__powerup_img[i] = pygame.transform.scale(self.__powerup_img[i],(40,40))
        
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
        self.__floor = LoadAssets.load_floor()
        self.__floor_position = 0
        self.__background = LoadAssets.load_background()
        self.__score_count = Score.Score()
        self.__user_input_time = 0
    
    ## @brief Method that checks the user input
    #  @details Checks for the user input and decided the next action based on that input. This includes
    #  game controls, inputs reciveved from menu controller, and quitting the game. 
    #  @param game_start_time the time that current game started
    def check_user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.__character.duck(self.__load_character[2])
                    if self.__character.get_ducking():
                        self.__play_sound.play_duck_sound()

                    ### self.__user_input_time = time() - self.__user_input_time
                    ### print("RESPONSE TIME", self.__user_input_time)

                if event.key == pygame.K_UP:
                    if not self.__character.get_jumping() or (self.__character.get_double_jumping() and self.__character.get_limit() <= 2):
                        self.__play_sound.play_jump_sound()
                    self.__character.jump(self.__load_character[1])
                    ### self.__user_input_time = time() - self.__user_input_time
                    ### print("RESPONSE TIME", self.__user_input_time)
                
                if event.key == pygame.K_p:
                    self.__pause_time = time()
                    self.__character.pause()
                    user_response = self.__menu_controller.pause_menu(self.__pause_menu_img)
                    if (user_response == "Resume"):
                        self.__pause_time = time() - self.__pause_time

                        self.__character.resume()
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
        running = True
        bg_rgb = GameController.INIT_BG
        # Defining Variables for the view methods
        display_obstacles = DisplayObstacle.DisplayObstacle(self.__game_screen)
        display_character = DisplayCharacter.DisplayCharacter(self.__game_screen, self.__character)
        display_environment = DisplayEnvironment.DisplayEnvironment(self.__game_screen)
        display_powerups = DisplayPowerups.DisplayPowerups(self.__game_screen)
        display_character = DisplayCharacter.DisplayCharacter(self.__game_screen, self.__character)
        update_environment = UpdateEnvironment.UpdateEnvironment()
        obstacle_spawn_time = time() 
        # The game loop
        while running: 
            clock.tick(GameController.FPS)
            # Drawing environment elements
            display_environment.draw_background(self.__background, bg_rgb)
            display_environment.draw_floor(self.__floor, self.__floor_position)
            display_environment.draw_score(self.__score_count.get_current_score(), self.__score_count.get_score(), clock)
            if self.__character.is_powered() and self.__character.get_power_time() < GameController.POWERUPS_TIME:
                display_environment.draw_powerup(round(GameController.POWERUPS_TIME - self.__character.get_power_time()))
                x,y = self.__character.get_rect().left, self.__character.get_rect().bottom
                x += 25
                y -= 125
                if self.__character.get_invincible() == True:
                    self.__game_screen.blit(self.__powerup_img[0], (x,y))
                elif self.__character.get_double_jumping() == True:
                    self.__game_screen.blit(self.__powerup_img[1],(x,y)) 
                elif self.__character.get_slo_mo() == True:
                    self.__game_screen.blit(self.__powerup_img[2],(x,y)) 


            # Drawing character
            display_character.draw_character()

            # Check user inputs
            self.__user_input_time = time()
            user_response = self.check_user_input()
            ### self.__user_input_time = time() - self.__user_input_time
            ### print("RESPONSE TIME:", self.__user_input_time)
            
            #start_time = None
            if (user_response == "Resume"):
                game_start_time, obstacle_spawn_time = self.resume_game(display_obstacles, display_environment, display_powerups, display_character, bg_rgb, game_start_time)
                
            elif(user_response == "Quit"):
                running = False

            # Generate Obstacle
            obstacle_spawn_time = display_obstacles.generate_obstacle(GameController.OBS_START_X, \
                    GameController.OBS_START_Y, self.__obstacle_obj_list, obstacle_spawn_time,display_powerups.get_powerups_list()) 
            
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
            self.detect_powerups_collision(display_powerups, display_obstacles)

            # Detect collison (obstacles)
            running = self.detect_obstacles_collision(running, current_score, display_obstacles)

            self.increase_game_speed(display_powerups, display_obstacles)
            pygame.display.update()

    ## @brief increases the game speed when the score reaches a specific value. It will also update the speed of all
    #  other obstacles and powerups.
    #  @param powerups a list of Powerups objects
    def increase_game_speed(self, powerups, obstacles):
        score = self.__score_count.get_current_score()
        if(self.__game_speed < GameController.MAX_SPEED):
            if self.__character.get_slo_mo():
                self.__game_speed = GameController.INIT_SPEED 
            else:
                self.__game_speed = GameController.SPEED_FACTOR * (score // GameController.SCORE_SPEED) + GameController.INIT_SPEED

        obstacles.update_speed(self.__game_speed)
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
    
    ## @brief Handles the control flow of starting the actual game session or exiting the game application. Initializes 
    # the pygame library and sets various settings such as the clock and font for the game.
    def run_game(self):
        pygame.init()
                
        clock = pygame.time.Clock()

        font = pygame.font.Font("../assets/Acceleration-Reaction.ttf", GameController.FONTSIZE)

        running = True

        while running:
            action = self.main_menu(font)

            if action == "Play":
                game_start_time = time()
                self.game_loop(clock, game_start_time)
            else:
                running = False

    ## @brief Handles the control flow of pausing the game and resuming the game
    #  @param d_obstacels a class that take responsible for showing and maintaining obstacles
    #  @param d_environment a class that take responsible for showing background, instructions and score
    #  @param d_powerups a class that take responsible for showing and maintaining powerups
    #  @param bg_rgb the initial color of the background
    #  @param game_start_time the last start time from pausing
    #  @return the new start time from pausing and obstacle spawn time
    def resume_game(self, d_obstacles, d_environment, d_powerups, d_character, bg_rgb, game_start_time):
        self.__is_resume = True
        start_time = time()
        d_obstacles.update_speed(0)
        for i in range(len(self.__obstacle_obj_list)):
            self.__obstacle_obj_list[i].set_speed(0)
        d_powerups.update_speed(0)
        
        current_time = time()
        while (current_time - start_time <= GameController.RESUME_TIME):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        pass
            d_environment.draw_background(self.__background, bg_rgb)
            d_environment.draw_floor(self.__floor, self.__floor_position)
            d_character.draw_character()
            d_powerups.update_powerups(self.__obstacle_obj_list)
            d_obstacles.update_obstacle_display()
            self.__menu_controller.resume_menu(GameController.RESUME_TIME - (current_time - start_time))
            current_time = time()
            pygame.display.update()
        for i in range(len(self.__obstacle_obj_list)):
            self.__obstacle_obj_list[i].set_speed(self.__game_speed)
        d_obstacles.update_speed(self.__game_speed)
        d_powerups.update_speed(self.__game_speed)

        self.check_user_input()
        game_start_time += self.__pause_time + GameController.RESUME_TIME
        # Updating obstacle_spawn time to prevent another obstacle spawning immediately
        obstacle_spawn_time = time() 
        return game_start_time, obstacle_spawn_time

    ## @brief Handles the collision with powerups and sound effects of the collsion
    #  @param d_powerups a class that take responsible for showing and maintaining powerups
    #  @param d_obstacles a class that take responsible for showing and maintaining obstacles
    def detect_powerups_collision(self, d_powerups, d_obstacles):
        powerups_taken = DetectCollision.find_collision_powerups(self.__character, d_powerups.get_powerups_list())
        if powerups_taken:
            self.__play_sound.play_powerup_sound()
            if powerups_taken.get_name() == 0:
                self.__character.invincible()
            elif powerups_taken.get_name() == 1:
                self.__character.double_jump()
            elif powerups_taken.get_name() == 2:
                self.__character.slo_mo()
                self.increase_game_speed(d_powerups, d_obstacles)
            else:
                self.__score_count.boost()
            d_powerups.remove_powerups(powerups_taken)

    ## @brief Handles the collision with obstacles and sound effects of the collision
    #  @param running the current boolean running state of the game
    #  @param current_score the current_score the user has achieved so far
    #  @param d_obstacles a class that take responsible for showing and maintaining obstacles
    def detect_obstacles_collision(self, running, current_score, d_obstacles):
        is_obstacle_collision = DetectCollision.find_collision_obstacle(self.__character, d_obstacles.get_obstacle_list()) 
        if(is_obstacle_collision != None and not self.__character.get_invincible()):
            running = False
            self.__play_sound.play_game_over_sound()
            self.__menu_controller.end_menu(current_score, self.__score_count.get_score() ,self.__end_menu_img)
            self.__score_count.reset_score()
            self.__game_speed = GameController.INIT_SPEED
            self.__character.reset(self.__load_character[0])
        elif (is_obstacle_collision != None and self.__character.get_invincible()): 
            d_obstacles.remove_obstacle(is_obstacle_collision)
            self.__play_sound.play_collision_sound()    
        return running

game = GameController()
game.run_game()
