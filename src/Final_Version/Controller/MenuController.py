"""@package docstring
Documentation for this module.
 
Menu Controller class
Author: Dev^(enthusiases)
This class is responsible for controlling the flow on the menus. It calls 
view and model modules while handling the user input.
"""
import pygame

class MenuController:
    def __init__(self, window):
        self.__game_screen = window

    
    def end_menu(self, score):
        screen.fill((255,255,255))  #white background       
        self.displayMsg('Game Over: Collison with obstacle', (0,0))
        self.displayMsg('Final Score is: ' + str(round(score)), (0,50))
        
        width, height = pygame.display.get_surface().get_size()
        self.displayMsg('To head back to main menu, press any key', (0, height/2))
        pygame.display.update()

        wait()



    def wait(self,screen, font):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.KEYDOWN:
                  return
                            # This runs on any key press.

