class Obstacle:
    # name: name of obstacle
    # width: width of image of obstacle
    # height: height of image of obstacle
    # imgPath: image path for obstacle
    def __init__(self, name, width, height, speed, imgPath):
        self.__name = name
        self.__width = width
        self.__height = height
        self.__speed = speed
        self.__img = imgPath

    def getWidth(self):
        return self.__width

    def setWidth(self, width):
        if (width < 0):
            print("Invalid Width")
        self.__width = width
    
    def getHeight(self):
        return self.__height
   
    def setHeight(self, height):
        if (height < 0):
            print("Invalid Height")
        self.__height = height
    
    def getSpeed(self):
        return self.__speed

    def setSpeed(self, newSpeed):
        if (newSpeed < 0):
            print("Invalid Speed: Should be greater than 0")
        self.__speed = newSpeed

    def getImg(self):
        return self.__img

    def setImg(self, img):
        try:  
            self.__img = img
        except FileNotFoundError:
            print("Wrong file or file path")

    
