import pygame
class Obstacle(pygame.sprite.Sprite):
    # name: name of obstacle
    # width: width of image of obstacle
    # height: height of image of obstacle
    # imgPath: image path for obstacle
    def _init_(self, name, width, height, speed, obstacle_img):
        super()._init_()
        self._name = name
        self._width = width
        self._height = height
        self._speed = speed
        self._img = obstacle_img
        self._rect = obstacle_.get_rect()

    def get_width(self):
        return self._width

    def set_width(self, width):
        if (width < 0):
            raise ValueError("Invalid Width: Should be greater than or equal to zero")
        self._width = width
    
    def get_height(self):
        return self._height
   
    def set_height(self, height):
        if (height < 0):
            raise ValueError("Invalid Height: Should be greater than or equal to zero")
        self._height = height
    
    def get_speed(self):
        return self._speed

    def set_speed(self, new_speed):
        if (new_speed < 0):
            raise ValueError("Invalid Speed: Should be greather than 0")
        self._speed = new_speed

    def get_img(self):
        return self._img

    def set_img(self, new_img):
        if (new_img == None):
            raise TypeError ("Invalid Pygame.img")
    def get_rect(self):
        return self.rect

    def set_rect(self, x, y):
        self.rect.left = x
        self.rect.bottom = y + self.get_height() 

