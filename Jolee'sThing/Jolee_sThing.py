import random

#class <name>:
#   def __init__ (self, <arg>):
#   self.<arg> = <arg>


class Gridpoint:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

class Wall:
    def __init__ (self, startingPoint, length, direction):
        self.startingPoint = startingPoint
        self. length = length
        self.direction = direction
        #False = vertical, True = horizontal

randomXValue = random.randrange(1, 10) * 2
randomYValue = random.randrange(1, 10) * 2

randomGridpoint = Gridpoint(randomXValue, randomYValue)

#<VariableName> = <className>(<arg>)

newWallX = Wall(Gridpoint(0, randomYValue), 20, False)
newWallY = Wall(Gridpoint(randomXValue, 0), 20, True)

newMaze = [newWallX, newWallY]

if randomYValue % 2 == 0:
    newWallx
    

#for x in range(1, 20):
    #if x % 2 == 0:
   #     break
  #  else: 
  #      newMaze 
        
#for y in range(1, 20):
  #  if y % 2 == 0:
  #      break
  #  else:

    