"""@package docstring
Documentation for this module.
 
LoadAssets class
Author: Dev^(enthusiases)
This module is responsible for load all images and sounds needed for the game.
"""

import pygame

##
# @file LoadAssets.py
# @brief This is a module for loading assets involved with the game such as images and audio files.


## @brief Loads floor image
#  @return a pygame.iamge of the floor/platform image
#  @exception Exception IllegalArguementException
def load_floor():
    image = pygame.image.load('../assets/floor.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image

## @brief Loads background image
#  @return a pygame.iamge of the background image
#  @exception Exception IllegalArguementException    
def load_background():
    image = pygame.image.load('../assets/background.png')
    image = image
    if image is None:
        raise Exception("IllegalArgumentException")
    return image   

## @brief Loads character images 
#  @return a sequence of pygame.image of the charcter images performing different actions
#  @exception Exception IllegalArguementException
def load_character():
    char_list = []
    # Loading images for the running character
    image = [pygame.image.load('../assets/R1.png'), pygame.image.load('../assets/R2.png'), pygame.image.load('../assets/R3.png'),\
        pygame.image.load('../assets/R4.png'), pygame.image.load('../assets/R5.png'), pygame.image.load('../assets/R6.png'),\
            pygame.image.load('../assets/R7.png'), pygame.image.load('../assets/R8.png')]
    if image is None:
        raise Exception("IllegalArgumentException")
    char_list.append(image)
    image = pygame.image.load('../assets/character_jumping.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    char_list.append(image)
    image = pygame.image.load('../assets/duck.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    char_list.append(image)
    return char_list 

## @brief Loads images of all obstacles 
#  @return a sequence of pygame.image of all types of obstacles images
#  @exception Exception IllegalArguementException
def load_all_obstacles():
    obstacle_list = []
    image = pygame.image.load('../assets/obstacle1.png')
    image = pygame.transform.scale(image, (70,100))
    if image is None:
        raise Exception("IllegalArgumentException")
    obstacle_list.append(image)
    image = pygame.transform.scale(image, (56, 80))
    obstacle_list.append(image)
    image = pygame.image.load('../assets/obstacle2.png')
    image = pygame.transform.scale(image, (120,100))
    if image is None:
        raise Exception("IllegalArgumentException")
    obstacle_list.append(image)
    
    image = pygame.transform.scale(image, (96, 80))

    image = pygame.image.load('../assets/tumbleweed.png')
    image = pygame.transform.scale(image, (60,60))
    obstacle_list.append(image)
    return obstacle_list                 

## @brief Loads images of all powerups 
#  @return a sequence of pygame.image of all types of powerups images
#  @exception Exception IllegalArguementException
def load_all_powerups():
    powerups_list = []
    image = pygame.image.load('../assets/invicibility_powerup.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    powerups_list.append(image)
    image = pygame.image.load('../assets/double_jump_powerup.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    powerups_list.append(image)
    image = pygame.image.load('../assets/slo_mo.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    powerups_list.append(image)
    image = pygame.image.load('../assets/score_boost.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    powerups_list.append(image)
    return powerups_list 

## @brief Loads the image of main menu 
#  @return a pygame.image of the main menu image
#  @exception Exception IllegalArguementException
def load_main_menu():
    image = pygame.image.load('../assets/mainmenu.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image  

## @brief Loads the pause menu image
# @return pygame.image containing the pause menu image
#  @exception Exception IllegalArguementException
def load_pause_menu():
    image = pygame.image.load('../assets/pausemenu.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image  

## @brief Loads the end menu image
# @return pygame.image containing the end menu image 
#  @exception Exception IllegalArguementException 
def load_end_menu():
    image = pygame.image.load('../assets/endmenu.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image  

## @brief Loads the setting menu image
# @return pygame.image containing the setting menu image 
#  @exception Exception IllegalArguementException 
def load_settting_menu():
    image = pygame.image.load('../assets/setting_menu.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image  

## @brief Loads the instructions menu image
# @return pygame.image containing the instructions menu image 
#  @exception Exception IllegalArguementException 
def load_instruction_menu():
    image = pygame.image.load('../assets/instruction_screen.png')
    if image is None:
        raise Exception("IllegalArgumentException")
    return image  

## @brief Loads all sound effects 
#  @return a sequence of pygame.mixer containing different sound effects and background music
#  @exception Exception IllegalArguementException
def load_sound():
    sound_list = []
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound('../assets/bg_music.wav') 
    if bg_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(bg_sound)
    jump_sound = pygame.mixer.Sound('../assets/game_over.wav') 
    if jump_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(jump_sound)
    duck_sound = pygame.mixer.Sound('../assets/jump.wav')
    if duck_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(duck_sound)
    collision_sound = pygame.mixer.Sound('../assets/duck.wav')
    if collision_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(collision_sound)
    powerup_sound = pygame.mixer.Sound('../assets/obtain_powerups.wav')
    if powerup_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(powerup_sound)
    powerup_sound = pygame.mixer.Sound('../assets/breaking_obstacle.wav')
    if powerup_sound is None:
        raise Exception("IllegalArgumentException")
    sound_list.append(powerup_sound)
    return sound_list