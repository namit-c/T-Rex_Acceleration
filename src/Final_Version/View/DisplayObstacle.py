"""@package docstring
Documentation for this module.
 
Obstacle class
Author: Dev^(enthusiases)
This class is responsible for maintaining several properties of the obstacle object
"""

##
# @file DisplayObstacle.py
# @brief This class is responsible for maintaining all obstacles that are displayed 

import pygame
import time
import Obstacle
import DetectCollision
from random import randint

class DisplayObstacle:
    ## @brief Constructor for DisplayObstacle
    #  @param game_window pygame.display
    def __init__(self, game_window):
        self.__game_screen = game_window
        self.__obstacleList = list()

    ## @brief get the list of obstacles
    #  @return returns the list of obstacles
    def get_obstacle_list(self):
        return self.__obstacleList

    ## @brief remove a obstacle from the obstacle list
    #  @param obstacle obstacle type
    def remove_obstacle(self, obstacle):
        self.__obstacleList.remove(obstacle)
    
    ## @brief drawing the obstacle onto the screen at a specific location
    #  @param current_x x position for obstacle to be drawn at
    #  @param current_y y position for obstacle to be drawn at
    #  @param obstacle Obstacle object
    def draw_obstacle(self, current_x, current_y, obstacle):
        obstacleImg = obstacle.getImg()
        
        # Scaling down the image to a fixed size
        obstacleImg =  pygame.transform.scale(obstacleImg, (obstacle.get_width(), obstacle.get_height()))
        
        obstacle.setImg(obstacleImg)
        self.__game_screen.blit(obstacleImg, (current_x, current_y))

    ## @brief display a message(string) to draw on screen 
    #  @param msg String
    #  @param msg_pos a tuple of (x,y) position to be drawn on screen
    def display_msg(self, msg, msg_pos):
       	pygame.font.init() # you have to call this at the start, 
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = my_font.render(msg, False, (0, 0, 0))
        self.__game_screen.blit(text_surface,msg_pos)

    
    ## @brief generate an obstacle from a random list of obstacles to be drawn on the screen (drawing them randomly at times
    #         from 3 and 5 seconds)
    #  @param obstacle_pos_x x position to draw obstacle on screen
    #  @param obstacle_pos_y y position to draw obstacle on screen
    #  @param obstacle_list list of obstacle objects
    #  @param prev_obstacle_spawn_time Keeping track of when the last obstacle was generated
    def generate_obstacle(self, obstacle_pos_x, obstacle_pos_y, obstacle_list, prev_obstacle_spawn_time):
        random_index = randint(0, len(obstacle_list)) 
      
        # If the current time from when the last obstacle was spawned someone between 3 and 5 second
        if (time.time() - prev_obstacle_spawn_time >= randint(3,5)):
            self.draw_obstacle(obstacle_pos_x, obstacle_pos_y, obstacle_list[random_index])
            
            self.__obstacleList.append(obstacle_list[random_index])
            
            prev_obstacle_spawn_time = time.time()

        return prev_obstacle_spawn_time
       
    ## @brief update all obstacle objects on the screen to be drawn to there new position. If an obstacle X position is less than
    #         -100 pixels, then remove the current obstacle from the obstacle list.
    def update_obstacle_display(self):
        for obstacle in self.get_obstacle_list():
            
            obstacle_pos = obstacle.get_pos() #returns [x,y] 
            x = obstacle_pos[0]
            x -= obstacle.get_speed()

            y = obstacle_pos[1] # y position of obstacle doesn't change

            
            # updating the current position of the obstacle and drawing the obstacle at new position
            obstacle.set_rect(x, y)
            self.draw_obstacle(x,y, obstacle)

            
            # if obstacle is well beyond the screen window, then remove from obstacle_list
            if x < -100:
                self.remove_obstacle(obstacle)
            
    
         