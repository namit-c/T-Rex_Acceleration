sys.path.insert(1, '../Model')
from Powerups import *

class DisplayPowerups():
    def __init__(self, game_screen):
        if (game_screen is None):
            raise Exception("IllegalArguemntException")
        self.game_screen = game_screen
        self.powerups_displayed = []
    def generate_powerups(self, speed):
        new_powerups = Powerups(self.game_screen, 50, 50, speed)
        self.powerups_displayed.append(new_powerups)
    def draw_powerups(self, powerups):
        self.game_screen.blit(powerups.get_image(), powerups.get_image().get_rect())
    def update_powerups(self):
        for element in self.powerups_displayed:
            self.draw_powerups(element)
            element.update()