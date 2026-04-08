class Robot:

    DIRSTRINGS = ["North", "East", "South", "West"]

    def __init__(self, width: int, height: int):
        self.__width = width
        self.__height = height
        self.__x = 0
        self.__y = 0
        self.__dir = 1
        self.__M = ((self.__width - 1) + (self.__height - 1)) * 2

    def step(self, num: int) -> None:

        # walk around perimeter
        # reduce by perimeter size
        num = num % self.__M

        # edge case - don't turn at the end when facing along the wall at a corner
        if num == 0:
            # 0, 0: facing east: should face south
            if (self.__x, self.__y) == (0, 0) and self.__dir == 1:
                self.__dir = 2
            if (self.__x, self.__y) == (self.__width-1, 0) and self.__dir == 0:
                self.__dir = 1
            if (self.__x, self.__y) == (self.__width-1, self.__height-1) and self.__dir == 3:
                self.__dir = 0
            if (self.__x, self.__y) == (0, self.__height-1) and self.__dir == 2:
                self.__dir = 3

        while num > 0:

            if self.__dir == 0: # north
                if self.__y + num > self.__height - 1:
                    num -= self.__height - 1 - self.__y
                    self.__y = self.__height - 1
                else:
                    self.__y += num
                    break

            elif self.__dir == 1: # east
                if self.__x + num > self.__width - 1:
                    num -= self.__width - 1 - self.__x
                    self.__x = self.__width - 1
                else:
                    self.__x += num
                    break

            elif self.__dir == 2: # south
                if self.__y - num < 0:
                    num -= self.__y
                    self.__y = 0
                else:
                    self.__y -= num
                    break

            else: # west
                if self.__x - num < 0:
                    num -= self.__x
                    self.__x = 0
                else:
                    self.__x -= num
                    break

            # change direction 
            self.__dir = (self.__dir - 1) % 4


    def getPos(self) -> List[int]:
        return [self.__x, self.__y]
        

    def getDir(self) -> str:
        return self.DIRSTRINGS[self.__dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()