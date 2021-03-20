import pygame

class LoadAssets():
    def load_floor(self):
        image = pygame.image.load('../assets/floor.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image
    
    def load_background(self):
        image = pygame.image.load('../assets/background.png')
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
        image = pygame.image.load('../assets/character_invisible.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        char_list.append(image)
        return char_list 

    def load_all_obstacles(self):
        obstacle_list = []
        image = pygame.image.load('../assets/obstacle1.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        obstacle_list.append(image)
        image = pygame.image.load('../assets/obstacle2.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        obstacle_list.append(image)
        return obstacle_list                 

    def load_all_powerups(self):
        powerups_list = []
        image = pygame.image.load('../assets/powerup1.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerup2.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerup3.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        image = pygame.image.load('../assets/powerup4.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        powerups_list.append(image)
        return powerups_list 

    def load_main_menu(self):
        image = pygame.image.load('../assets/mainmenu.png')
        if image is None:
            raise Exception("IllegalArgumentException")
        return image  

    def load_sound(self):
        sound_list = []
        sound = pygame.mixer.music.load('../assets/sound1.mp3')
        if sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(sound)
        sound = pygame.mixer.music.load('../assets/sound2.mp3')
        if sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(sound)
        sound = pygame.mixer.music.load('../assets/sound3.mp3')
        if sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(sound)
        sound = pygame.mixer.music.load('../assets/sound4.mp3')
        if sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(sound)
        sound = pygame.mixer.music.load('../assets/sound5.mp3')
        if sound is None:
            raise Exception("IllegalArgumentException")
        sound_list.append(sound)
        return sound_list    