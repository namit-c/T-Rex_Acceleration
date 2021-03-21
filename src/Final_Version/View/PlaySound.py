"""@package docstring
Documentation for this module.
 
Play Sound class
Author: Dev^(enthusiases)
This class is responsible for playing the background music and different
sound effects.
"""

import pygame


##
# @file PlaySound.py
# @brief This class is responsible for maintaining several properties several audio queues in the 
#        game

class PlaySound:

    ## @brief Contructor for PlaySound
    #  @param background pygame.mixer.Sound
    #  @param jump pygame.mixer.sound
    #  @param duck pygame.mixer.sound
    #  @param collision pygame.mixer.sound
    #  @param powerup pygame.mixer.sound
    def __init__(self, background, jump, duck, collision, powerup):
        self.__bg_sound = background
        self.__jump_sound = jump
        self.__duck_sound = duck
        self.__collision_sound = collision
        self.__powerup_sound = powerup


    ## @brief Play the background music on repeat
    def play_bg_music(self):
        self.__bg_sound.play(-1)

    ## @brief Stop all audio in the queue
    def stop_music(self):
        pygame.mixer.music.stop()

    ## @brief Play the jump sound effect once
    def play_jump_sound(self):
        self.__jump_sound.play()

    ## @brief Play the duck sound effect once
    def play_duck_sound(self):
        self.__duck_sound.play()

    ## @brief Play the collision sound effect once
    def play_collision_sound(self):
        self.__collision_sound.play()
    
    ## @brief Play the powerup sound effect once
    def play_powerup_sound(self):
        self.__powerup_sound.play()



