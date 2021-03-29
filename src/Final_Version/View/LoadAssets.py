"""@package docstring
Documentation for this module.
 
LoadAssets class
Author: Dev^(enthusiases)
This class is responsible for load all images and sounds needed for the game.
"""

import pygame

## This is a class for assets loading
class LoadAssets():

    ## @brief load floor image
    #  @return return a pygame.iamge
    #  @exception Exception IllegalArguementException
    def load_floor(self):
        image = pygame.image.load('../assets/floor.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image

    ## @brief load background image
    #  @return return a pygame.iamge
    #  @exception Exception IllegalArguementException    
    def load_background(self):
        image = pygame.image.load('../assets/background.png')
        image = image
        if image is None:
            raise Exception("IllegalArgumentException")
        return image   

    ## @brief load character images 
    #  @return return a sequency of pygame.image
    #  @exception Exception IllegalArguementException
    def load_character(self):
        char_list = []
        # Loading images for the running character
        image = [pygame.image.load('../assets/R1.png'), pygame.image.load('../assets/R2.png'), pygame.image.load('../assets/R3.png'),\
            pygame.image.load('../assets/R4.png'), pygame.image.load('../assets/R5.png'), pygame.image.load('../assets/R6.png'),\
                pygame.image.load('../assets/R7.png'), pygame.image.load('../assets/R8.png')]
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        image = pygame.image.load('../assets/character_jump.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        image = pygame.image.load('../assets/character.gif')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        return char_list 

    ## @brief load images of all obstacles 
    #  @return return a sequency of pygame.image
    #  @exception Exception IllegalArguementException
    def load_all_obstacles(self):
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

    ## @brief load images of all powerups 
    #  @return return a sequency of pygame.image
    #  @exception Exception IllegalArguementException
    def load_all_powerups(self):
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

    ## @brief load the image of main menu 
    #  @return return a pygame.image
    #  @exception Exception IllegalArguementException
    def load_main_menu(self):
        image = pygame.image.load('../assets/mainmenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  


    ## @brief load the pause menu image
    # @return pygame.image containing the pause menu image 
    #  @exception Exception IllegalArguementException
    def load_pause_menu(self):
        image = pygame.image.load('../assets/pausemenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    ## @brief load the end menu image
    # @return pygame.image containing the end menu image 
    #  @exception Exception IllegalArguementException 
    def load_end_menu(self):
        image = pygame.image.load('../assets/endmenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    ## @brief load the setting menu image
    # @return pygame.image containing the setting menu image 
    #  @exception Exception IllegalArguementException 
    def load_settting_menu(self):
        image = pygame.image.load('../assets/setting_menu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    ## @brief load all sound effects 
    #  @return return a sequency of pygame.mixer
    #  @exception Exception IllegalArguementException
    def load_sound(self):
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
