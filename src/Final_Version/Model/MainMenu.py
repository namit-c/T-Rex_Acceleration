"""@package docstring
Documentation for this module.
 
Main Menu sound class
Author: Dev^(enthusiases)
This class is responsible for tracking the different game sound volumes. 
"""

##
# @file MainMenu.py
# @brief This is a class used to store the different game sound volumes


def MainMenu():

    ## Defining constant for the maximum volumes
    MAX_VOLUME = 100

    ## @brief Constructor that initializes different sound volumes
    def __init__(self):
        self.__background_music_volume = MAX_VOLUME
        self.__sound_effects_volume = MAX_VOLUME

    ## @brief Method that updates the volume of the game sounds
    # @param new_background_volume : an integer that represents the new value of 
    # the background music volume
    # @param new_sound_effects_volume : an integer that represents the new value
    # of the sound effects volume
    def change_volume(new_background_volume, new_sound_effects_volume):
        self.__background_music_volume = new_background_volume
        self.__sound_effects_volume = new_sound_effects_volume
    
    ## @brief Method that returns the current volume levels of the sounds
    # @return the volume of the background music and sound effects
    def get_volumes():
        return self.__background_music_volume, self.__sound_effects_volume
