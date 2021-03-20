sys.path.insert(1, '../Model')
from Character import *

class DisplayCharacter():
    def __init__(self, window, character):
        self.game_screen = window
        self.game_character = character
    def draw_character(self):
        self.game_screen.blit(self.game_character.image, self.game_character.image.get_rect())
