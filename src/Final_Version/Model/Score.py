"""@package docstring
Documentation for this module.
 
The player score class
Author: Dev^(enthusiases)
This class is responsible for the score of the player during the game session.
"""

from time import time

## This is a class used to keep track of the player's score
class Score():

    ## Defining constant for scaling the score
    SCALE_FACTOR = 5


    ## Constructor that initializes different fields required to track the 
    # player score. The start time is set to the time the constructor is called,
    # which also the time the game starts. The other parameters about the score 
    # (high score, current score, and previous score) are set to 0.
    def __init__(self):
        self.__high_score = 0
        self.__current_score = 0
        self.__previous_score = 0
        self.__start_time = time()
        
    ## Method that updates the current score
    # @return the current and previous score after the score has been updated
    def update_score():
        self.__previous_score = self.__current_score
        
        # Updating the current score based on current time and scale factor
        self.__current_score = round((time()-self.__start_time)*SCALE_FACTOR)

        # Updating the high score if the current score is greater
        if self.__current_score > self.__high_score:
            self.__high_score = self.__current_score

        return self.__current_score, self.__previous_score

    ## Method to retrieve the high score of the current game session
    # @return the high score of the current game session
    def get_score():
        return self.__high_score

    ########################################################################
    def get_start_time(self):
        return self.__start_time