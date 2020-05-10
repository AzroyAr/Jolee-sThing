import random

#Grid is 10x10

walls = []
holes = []

class gridPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#random.randrange(Start, Stop)

randomXValue = random.randrange(1, 9) * 2
randomYValue = random.randrange(1, 9) * 2

randomGridPoint = gridPoint(randomXValue, randomYValue)

for x in range(1, 20):
    newWall = gridPoint(x, randomGridPoint.y)
    walls.append(newWall)

for y in range(1, 20):
    newWall = gridPoint(randomGridPoint.x, y)
    walls.append(newWall)

#Repeated Code (Consider loops/methods)

randomXValue = random.randrange(1, 9) * 2
randomYValue = random.randrange(1, 9) * 2

randomGridPoint = gridPoint(randomXValue, randomYValue)

for x in range(randomYValue, 20):
    newWall = gridPoint(x, randomYValue)
    if gridPoint(x, randomYValue) in walls:
        break
    else:
        walls.append(newWall)

for y in range(randomXValue, 20):
    newWall = gridPoint(randomXValue, y)
    if newWall in walls:
        break
    else:      
        walls.append(newWall)



for z in walls:
    print(z.x, z.y)