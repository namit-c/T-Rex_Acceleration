"""@package docstring
Documentation for this module.
 
The player score class
Author: Dev^(enthusiases)
This class is responsible for the score of the player during the game session.
"""

from time import time

##
# @file Score.py
# @brief This is a class used to keep track of the player's score

class Score():

    ## @brief Constructor that initializes different fields required to track the 
    # player score. The start time is set to the time the constructor is called,
    # which also the time the game starts. The other parameters about the score 
    # (high score, current score, and previous score) are set to 0.
    def __init__(self):
        self.__high_score = 0
        self.__current_score = 0
        self.__previous_score = 0
        self.__SCALE_FACTOR = 5
        self.__BOOST = 0
        
        # Constant for the score boost
        self.__SCORE_BOOST_VAL = 100

    ## @brief Method that updates the current score
    # @param start_time the time the current game starts
    # @return the current and previous score after the score has been updated
    def update_score(self, start_time):
        self.__previous_score = self.__current_score
        
        # Updating the current score based on current time and scale factor
        self.__current_score = round((time()-start_time) * self.__SCALE_FACTOR  + self.__BOOST*self.__SCORE_BOOST_VAL)

        # Updating the high score if the current score is greater
        if self.__current_score > self.__high_score:
            self.__high_score = self.__current_score

        return self.__current_score, self.__previous_score

    ## @brief Method to retrieve the high score of the current game session
    # @return the high score of the current game session
    def get_score(self):
        return self.__high_score
    
    ## @brief Method to retrieve the current score of the game
    # @return the current score of the game
    def get_current_score(self):
        return self.__current_score

    ## @brief Method to change the current score and score boost to 0 for the next game
    def reset_score(self):
        self.__current_score = 0
        self.__BOOST = 0

    ## @brief Method to indicate the score boost powerup is acquired
    def boost(self):
        self.__BOOST += 1