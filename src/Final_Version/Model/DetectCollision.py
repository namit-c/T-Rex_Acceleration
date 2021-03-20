import pygame

def detect_collision(character, element): 
    return character.get_rect().colliderect(element.get_rect())

def find_collision(character, element_list):
    for element in element_list:
        if (detect_collision(character, element)):
            return element
    
    return None
