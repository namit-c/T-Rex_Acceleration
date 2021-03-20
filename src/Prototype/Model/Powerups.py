import pygame

class Powerups(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen 
        self.image = pygame.transform.scale(pygame.image.load('../images/Power.png'), (50, 50))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.left = self.screen_rect.left + 500
        self.rect.bottom = self.screen_rect.bottom - 80
        self.movement = [-10,0]
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.rect = self.rect.move(self.movement) 
