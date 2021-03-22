import pygame

class LoadAssets():
    def load_floor(self):
        image = pygame.image.load('../assets/floor.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image
    
    def load_background(self):
        image = pygame.image.load('../assets/background.png')
        image = image
        if image is None:
            raise Exception("IllegalArgumentException")
        return image   

    def load_character(self):
        char_list = []
        image = pygame.image.load('../assets/character.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        image = pygame.image.load('../assets/character_jump.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        image = pygame.image.load('../assets/character_invinsible.jpg')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        return char_list 

    def load_all_obstacles(self):
        obstacle_list = []
        image = pygame.image.load('../assets/obstacle1.png')
        image = pygame.transform.scale(image, (70,100))
        if image is None:
            raise Exception("IllegalArgumentException")
        obstacle_list.append(image)
        image = pygame.image.load('../assets/obstacle2.png')
        image = pygame.transform.scale(image, (120,100))
        if image is None:
            raise Exception("IllegalArgumentException")
        obstacle_list.append(image)
        return obstacle_list                 

    def load_all_powerups(self):
        powerups_list = []
        image = pygame.image.load('../assets/powerups1.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerups2.jpg')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerups3.jpg')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerups4.jpg')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        return powerups_list 

    def load_main_menu(self):
        image = pygame.image.load('../assets/mainmenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  


    ## Method that loads the pause menu image and assigns it to a python variable
    # @return a variable containing the pause menu image 
    def load_pause_menu(self):
        image = pygame.image.load('../assets/pausemenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    ## Method that loads the end menu image and assigns it to a python variable
    # @return a variable containing the end menu image 
    def load_main_menu(self):
        image = pygame.image.load('../assets/endmenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    def load_sound(self):
        sound_list = []
        pygame.mixer.init()
        bg_sound = pygame.mixer.Sound('../assets/bg_music.wav') 
        if bg_sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(bg_sound)
        jump_sound = pygame.mixer.Sound('../assets/game_over.wav') #
        if jump_sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(jump_sound)
        duck_sound = pygame.mixer.Sound('../assets/jumping_2.wav')
        if duck_sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(duck_sound)
        collision_sound = pygame.mixer.Sound('../assets/jumping_2.wav')
        if collision_sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(collision_sound)
        powerup_sound = pygame.mixer.Sound('../assets/jumping_2.wav')
        if powerup_sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(powerup_sound)
        return sound_list    
