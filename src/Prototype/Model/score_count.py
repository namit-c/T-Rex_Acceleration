import time
from random import *

def checkScore(score, prevScore, screen, RGB):
    if (round(prevScore) != round(score) and round(score) % 50 == 0 and round(score) != 0):
        randomRGBChange = randint(1,3)
        if (randomRGBChange == 1):
            RGB[0] = (RGB[0] + 50) % 255
        elif (randomRGBChange == 2):
            RGB[1] = (RGB[1] + 50) % 255
        else:
            RGB[2] = (RGB[2] + 50) % 255
        screen.fill((RGB[0], RGB[1], RGB[2]))

def updateScore(score, prevScore, startTime):
    prevScore = round(score)
    score = round((time.time() - startTime)*10)

    return score, prevScore