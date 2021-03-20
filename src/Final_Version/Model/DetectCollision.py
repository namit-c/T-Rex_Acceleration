"""@package docstring
Documentation for this module.
 
Obstacle class
Author: Dev^(enthusiases)
This class is responsible for maintaining several properties of the obstacle object
"""

import pygame

##
# @file DetectCollision.py
# @brief Reponsible for checking collisions between a character and other elements (i.e powerups, obstacles) 


## @brief Determine if a character has collided with an element
#  @param character pygame.sprite 
#  @param element pygame.sprite
#  @return return a boolean where if the character and element have collided then return True, otherwise return False 
def detect_collision(character, element): 
    return character.get_rect().colliderect(element.get_rect())

## @brief Determine which element the character has collided with
#  @param character pygame.sprite
#  @param element_list list of pygame.sprite
#  @return return the specific element that first collides with the character, if there is no collisio then return None
def find_collision(character, element_list):
    for element in element_list:
        if (detect_collision(character, element)):
            return element
    return None
