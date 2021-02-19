import pygame
import time
import Obstacle
import DetectCollision
from random import randint

class DisplayObstacle:
    def __init__(self, gameWindow):
        self.__gameWindow = gameWindow
        self.__obstacleList = list()

    def getObstacleList(self):
        return self.__obstacleList

    def getRemoveObstacle(self, obstacle):
        self.__obstacleList.remove(obstacle)

    def drawObstacle(self, currentX, currentY, obstacle):
        obstacleImg = obstacle.getImg()
        
        # Scaling down the image to a fixed size
        obstacleImg =  pygame.transform.scale(obstacleImg, (obstacle.getWidth(), obstacle.getHeight()))
        
        obstacle.setImg(obstacleImg)
        self.__gameWindow.blit(obstacleImg, (currentX, currentY))

    def displayMsg(self, msg, msgPos):
       	pygame.font.init() # you have to call this at the start, 
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textSurface = myfont.render(msg, False, (0, 0, 0))
        self.__gameWindow.blit(textSurface,msgPos)


    def generateRandomObstacle(self, obstaclePosX, obstaclePosY, obstacle,obstacle_2, prevObstacleSpawnTime):
        randomNum = randint(1,2) 
       
        # If time is  
        if (time.time() - prevObstacleSpawnTime >= randint(3,5)):
            if (randomNum == 1): #Generate One obstacle
                self.drawObstacle(obstaclePosX, obstaclePosY, obstacle)
                self.__obstacleList.append([obstaclePosX, obstaclePosY, obstacle, 1])
            
            elif (randomNum == 2): #Generate Two obstacle side by side
                self.drawObstacle(obstaclePosX, obstaclePosY, obstacle_2)
                self.__obstacleList.append([obstaclePosX, obstaclePosY, obstacle_2, 2])
                
            prevObstacleSpawnTime = time.time()

        return prevObstacleSpawnTime
        
    def updateObstacleDisplay(self, dino, screen, obstaclePosX, score):
        for i in self.getObstacleList():
            i[0] -=  i[2].getSpeed()
            self.drawObstacle(i[0],i[1],i[2])

            i[2].setRect(i[0],i[1])

            isCollision = DetectCollision.DetectCollision(dino, i[2])
            if isCollision == True and dino.isInvincible == False:
                print("COLLISION OCCURED")
                
                i[0] = obstaclePosX 

                screen.fill((255,255,255))  #white background       
                self.displayMsg('Game Over: Collison with obstacle', (0,0))
                self.displayMsg('Final Score is: ' + str(round(score)), (0,50))
                
                width, height = pygame.display.get_surface().get_size()
                self.displayMsg('To head back to main menu, press any key', (0, height/2))
                pygame.display.update()
               
                return "Collision"
            elif isCollision == True and dino.isInvincible == True:
                self.getRemoveObstacle(i)

            if i[0] < -100:
                self.getRemoveObstacle(i)
            
    
         
    def testGameLoop(self, windowWidth, windowHeight, obstacle, obstacle_2, t_rex):
        obstaclePosX = windowWidth + 100 #Starting slightly outside the 
        obstaclePosY = windowHeight - 300 #Starting towards the bottom of Window as a fixed position

        self.__gameWindow.fill((255,255,255)) # White background
           
        score = 0

        startTime = time.time()
        obstacleSpawnTime = time.time()

        RGB = [255,255,255]
          
        gameExit = False
            
        prevScore = -1
        while not gameExit:
            for event in pygame.event.get():
               if event.type == pygame.QUIT:
                    gameExit = True
                    print("HIGHSCORE IS", score) 
                    pygame.quit()
                    quit()
          

            self.__gameWindow.fill((RGB[0], RGB[1], RGB[2])) # White background
            if (round(prevScore) != round(score) and round(score) % 5 == 0 and round(score) != 0):
                print("HERE")
                randomRGBChange = randint(1,3)
                if (randomRGBChange == 1):
                    RGB[0] = (RGB[0] + 50) % 255
                elif (randomRGBChange == 2):
                    RGB[1] = (RGB[1] + 50) % 255
                else:
                    RGB[2] = (RGB[2] + 50) % 255
                self.__gameWindow.fill((RGB[0], RGB[1], RGB[2])) # White background
            self.drawObstacle(100, 300, t_rex)

            obstacleSpawnTime = self.generateRandomObstacle(obstaclePosX, obstaclePosY, obstacle, obstacle_2 , obstacleSpawnTime)

            # For now, the score is based on time
            prevScore = score
            score = time.time() - startTime

            self.displayMsg("Current Score is: " + str(round(score)), (0,100))
            self.displayMsg("FPS: " + str(int(clock.get_fps())), (0,300))

            for i in self.__obstacleList:
                i[0] -=  i[2].getSpeed()
                if i[3] == 1:
                    self.drawObstacle(i[0],i[1],i[2])
                else:
                    self.drawObstacle(i[0],i[1],i[2])
                    self.drawObstacle(i[0] + i[2].getWidth(), i[1], i[2])

                isCollision = DetectCollision.DetectCollision(100,300,t_rex,i[0],i[1],i[2])
                if isCollision == True:
                    print("COLLISION OCCURED")
                    self.displayMsg('Game Over: Collison with obstacle', (0,0))
                
                if i[0] < -100:
                    self.__obstacleList.remove(i)


            pygame.display.update()
            clock.tick(60)


        
#pygame.init()
#DISPLAY_WIDTH = 800
#DISPLAY_HEIGHT = 600
#window = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
#clock = pygame.time.Clock()

#obstacle = Obstacle.Obstacle("Cactus", 120, 120, 10, '../../demoImages/cactus.png')
#obstacle_2 = Obstacle.Obstacle("Cactus", 240, 120, 10, '../../demoImages/cactus_2.png')  
#t_rex = Obstacle.Obstacle("T-Rex", 120, 120, 0, '../../demoImages/t-rex.png')
#displayObstacle = DisplayObstacle(window)

#displayObstacle.testGameLoop(DISPLAY_WIDTH, DISPLAY_HEIGHT, obstacle, obstacle_2, t_rex)

