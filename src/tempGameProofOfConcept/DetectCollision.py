def DetectCollision(characterPosX, characterPosY, character, obstaclePosX, obstaclePosY, obstacle):
    MARGIN_ERROR = 18 # error with image pixels
    collision = False

    print("Character:",characterPosX, characterPosY, "\tObstacle", obstaclePosX, obstaclePosY)
    if ( characterPosX + MARGIN_ERROR < (obstaclePosX + obstacle.getWidth() )
        and  (characterPosX + character[0]) >  obstaclePosX + MARGIN_ERROR
        and characterPosY + MARGIN_ERROR < (obstaclePosY) 
        and (characterPosY + character[1]) > obstaclePosY + MARGIN_ERROR):
        collision = True

    return collision

