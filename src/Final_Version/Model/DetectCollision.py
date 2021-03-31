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
#  @return if the character and element have collided then return true, otherwise return false 
def detect_collision(character, element):
    return character.get_rect().colliderect(element.get_rect())

## @brief Determine which obstacle the character has collide with
#  @param character pygame.sprite
#  @param element_list list of pygame.sprite
#  @return the specific element that first collides with the character, if there is no collisio then return None
def find_collision_obstacle(character, element_list):
    for element in element_list:
        is_collision = detect_collision(character, element)
        if (is_collision):
            return element
    return None 

## @brief Determine which powerup the character has collided with
#  @param character pygame.sprite
#  @param element_list list of pygame.sprite
#  @return the specific powerup that first collides with the character, if there is no collisio then return None
def find_collision_powerups(character, element_list):
    powerups_taken = pygame.sprite.spritecollideany(character, element_list)
    if powerups_taken:
        return powerups_taken
