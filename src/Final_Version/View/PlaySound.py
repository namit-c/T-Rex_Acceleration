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
    def __init__(self, sound_list):
        self.__bg_sound = sound_list[0]
        self.__game_over = sound_list[1]
        self.__jump_sound = sound_list[2]
        self.__duck_sound = sound_list[3]
        self.__collision_sound = sound_list[5]
        self.__powerup_sound = sound_list[4]


        self.__SOUND_EFFECT_VOL = 0.25
        self.__BACKGROUND_VOL = 0.1

    def set_sound_effect(self, sound_setting):
        self.__SOUND_EFFECT_VOL = sound_setting

    def get_sound_effect(self):
        return self.__SOUND_EFFECT_VOL

    def set_background(self, sound_setting):
        self.__BACKGROUND_VOL = sound_setting

    def get_background(self):
        return self.__BACKGROUND_VOL

    ## @brief Play the background music on repeat
    def play_bg_music(self):
        self.__bg_sound.set_volume(self.__BACKGROUND_VOL)
        self.__bg_sound.play(-1)

    ## @brief Stop all audio in the queue
    def stop_music(self):
        pygame.mixer.music.stop()

    ## @brief Play the jump sound effect once
    def play_game_over_sound(self):
        self.__jump_sound.set_volume(self.__SOUND_EFFECT_VOL)
        self.__game_over.play()

    ## @brief Play the jump sound effect once
    def play_jump_sound(self):
        self.__jump_sound.set_volume(self.__SOUND_EFFECT_VOL)
        self.__jump_sound.play()

    ## @brief Play the duck sound effect once
    def play_duck_sound(self):
        self.__duck_sound.set_volume(self.__SOUND_EFFECT_VOL)

        self.__duck_sound.play()

    ## @brief Play the collision sound effect once
    def play_collision_sound(self):
        self.__collision_sound.set_volume(self.__SOUND_EFFECT_VOL)
        self.__collision_sound.play()
    
    ## @brief Play the powerup sound effect once
    def play_powerup_sound(self):
        self.__powerup_sound.set_volume(self.__SOUND_EFFECT_VOL)
        self.__powerup_sound.play()



