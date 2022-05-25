import queue
import time
import random
import sys

def drawMap1():
    map = []###  1   2    3    4    5    6    7    8    9    10   11   12   13  14   15   16   17   18   19   20  
    map.append(["#", " ", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#", " ", " ", "#"])
    map.append(["#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#", "#", " ", " ", "#", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    return map

def drawMap2():
    map = []###  1   2    3    4    5    6    7    8    9    10   11   12   13  14   15   16   17   18   19   20  
    map.append(["#", "A", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"]) 
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", " ", " ", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    return map

    
def drawMap():
    map = []
    map.append(["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#"])
    map.append(["#","H", " ", "S", " ", " ", " ", "F", " "," ", " ", "S", " ", " ", " ", " ", "#"])
    map.append(["#"," ", "#", " ", "#", "#", "#", "#", "#"," ", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#"," ", "#", " ", " ", " ", " ", " ", "C"," ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#"," ", " ", "S", "#", "#", "#", "#", "#"," ", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#"," ", "#", " ", " ", " ", "M", " ", " "," ", "#", " ", " ", " ", "V", " ", "#"])
    map.append(["#"," ", "#", " ", "#", "#", "#", " ", "#","#", "#", " ", "#", "#", " ", "#", "#"])
    map.append(["#"," ", " ", "S", " ", " ", " ", " ", " "," ", " ", "S", " ", " ", " ", " ", "#"])
    map.append(["#","#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#", "#", "#", "#"])

    return map

def printMap(map, position):    
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in position:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def sensor(map, position):    
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (1, 4) in position:
                reroute(map, j, i)
        print()

def insertDog (map, c):
    map[1].insert(c, "D")
    del map[1][c +1]
    return map

def insertObstacle(map, c, d):
    del map[d][c]
    map[d].insert(c, "O")
    return map

def removeDog (map, c, ctemp):
    map[1].insert(c, ctemp)
    del map[1][c + 1]
    return map

def currPosition(path):
    position = set()
    j=0
    i=1
    for direction in path:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1
        position.add((j, i))
    return position       

def drive(map, path=""):
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x

    i = begin
    j = 0
    count = 0
    sleep = 1
    position = set()
    position.add((j, i))
    for direction in path:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        position.add((j, i))

        if (map[j][i] == "S"):
           sleep = 5

        if (map[j][i] == "O"):

            if(map[j+1][i]=="#" or map[j-1][i]=="#"):
                i = i - 1

            if(map[j][i+1]=="#" or map[j][i-1]=="#"):
                j = j - 1

            var1 = j
            var2 = i
            nodes = queue.Queue()
            nodes.put("")
            route = ""
            map  = drawMap()
            del map[xStart][yStart]


            map[xStart].insert(yStart , "A")
            del map[xStart][yStart + 1]

            map[x_coordinate].insert(y_coordinate , "D")
            del map[x_coordinate][y_coordinate + 1]
            insertObstacle(map, c, d)
            insertObstacle(map, e, f)
            insertObstacle(map, g, h)
            insertObstacle(map, y, z)
            insertObstacle(map, k, l)

            while not  reroute(map,route, var1, var2):
                print("Rerouting...",count)
                route = nodes.get()
                for jj in ["W", "E", "N", "S"]:
                    put = route + jj
                    if checkMoveValidity2(map, put, var1, var2):
                        nodes.put(put)
                count = count + 1
                position = currPosition(route)

        c = random.randint(0,15)
        ctemp = map[3][c]

        print("\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(S)
        sleep = 1
        count = count + 1

    print("Arrived at destination, Goodbye!\n")
    return

def drive3(map, path, varj, vari):

    i = vari
    j = varj
    count = 0
    count2 = 0
    sleep = 1
    position = set()
    position.add((j, i))
    for direction in path:
        count2 = count2 + 1
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        position.add((j, i))

        if (map[j][i] == "S"):
           sleep = 5

        if (map[j][i] == "O"):

            if(path[count2] == "E"):
                i = i - 1
            if(path[count2] == "W"):
                i = i + 1
            if(path[count2] == "S"):
                j = j - 1
            if(path[count2] == "N"):
                j = j + 1

            var1 = j
            var2 = i
            nodes = queue.Queue()
            nodes.put("")
            route = ""
            map  = drawMap()

            del map[var1][var2]
            map[var1].insert(var2 , "A")
           

            map[x_coordinate].insert(y_coordinate , "D")
            del map[x_coordinate][y_coordinate + 1]
            insertObstacle(map, c, d)
            insertObstacle(map, e, f)
            insertObstacle(map, g, h)
            insertObstacle(map, y, z)
            insertObstacle(map, k, l)

            while not  reroute(map,route, var1, var2):
                print("Rerouting...",count)
                route = nodes.get()
                print(route)
                for jj in ["W", "E", "N", "S"]:
                    put = route + jj
                    if checkMoveValidity2(map, put, var1, var2):
                        nodes.put(put)
                count = count + 1
                position = currPosition(route)
                print(position)

        c = random.randint(0,15)
        ctemp = map[3][c]

        print("\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(sleep)
        sleep = 1
        count = count + 1

    print("Arrived at destination, Goodbye!\n")
    return

def drive2(map, path, varj, vari):
    i = vari
    j = varj
    for x, position in enumerate(map[0]):
        if position == "O":
            begin = x
    sleep = 1
    count = 0
    position = set()
    position.add((j, i))
    for direction in path:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1
        position.add((j, i))

        if (map[j][i] == "S"): 
            sleep = 5
        print("\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(sleep)
        sleep = 1
        count = count + 1

    print("Arrived at destination, Goodbye!\n")
    sys.exit()


def reroute(map, directions, varj, vari):
    i = vari
    j = varj
    begin = i
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x
    
    i = begin
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1
    if map[j][i] == "D":
        print("The directions to your destination are: " + directions)
        drive2(map, directions, varj, vari)
        return True
    return False


def checkMoveValidity(map, directions):
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x

    i = begin
    j = 0
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "#"):
            return False

    return True

def checkMoveValidity3(map, directions, varj, vari):

    i = vari
    j = varj
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "#"):
            return False

    return True


def checkMoveValidity2(map, directions,varj,vari):
    i = vari
    j = varj
    begin = i
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x
    
    i = begin 
    j = j
    # time.sleep(1)
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "O" or map[j][i] == "#"):
            return False

    return True    


def checkMoveValidity3(map, directions,varj,vari):
    i = vari
    j = varj
    begin = i
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x
    
    i = begin 
    j = j
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "#"):
            return False

    return True    


def findDestination(map, directions):
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x

    i = begin
    j = 0
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

    if map[j][i] == "D":
        print("The directions to your destination are: " + directions)
        drive(map, directions)
        return True
    print()
    return False

def findDestination2(map, directions, varj, vari):

    i = vari
    j = varj
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

    if map[j][i] == "D":
        print("The directions to your destination are: " + directions)
        drive3(map, directions, varj, vari)
        return True
    print()
    return False



nodes = queue.Queue()
nodes.put("")
route = ""
map  = drawMap()
map2  = drawMap1()
count = 0
destination = ""
print("\n****************************************************************************\n")
print("\nBellow is a map of the available places \n")
printMap(map, (1,1))

print("\nC - Church \n")
print("F - Food Market \n")
print("M - Mall \n")
print("V - Vacation \n")

startPosition = input("\nPlease select a starting point by entering its corresponding letter \n")

if(startPosition == "F"):
    xStart = 1
    yStart = 7
elif(startPosition == "C"):
    xStart = 3
    yStart = 8
elif(startPosition == "M"):
    xStart = 5
    yStart = 6
elif(startPosition == "V"):
    xStart = 4
    yStart = 14
elif(startPosition == "H"):
    xStart = 1
    yStart = 1
else:
    xStart = int (input("Please enter x coordinate of start(from 0 - 7)"))
    yStart = int (input("Please enter y coordinate of start(from 0 - 15)"))

destination = input("\nPlease select a destination by entering its corresponding letter \n")

if(destination == "F"):
    x_coordinate = 1
    y_coordinate = 7
elif(destination == "C"):
    x_coordinate = 3
    y_coordinate = 8
elif(destination == "M"):
    x_coordinate = 5
    y_coordinate = 6
elif(destination == "V"):
    x_coordinate = 4
    y_coordinate = 14
elif(destination == "H"):
    x_coordinate = 1
    y_coordinate = 1
else:
    x_coordinate = int (input("Please enter x coordinate of destination(from 0 - 7)"))
    y_coordinate = int (input("Please enter y coordinate of destination(from 0 - 15)"))


map[x_coordinate].insert(y_coordinate , "D")
del map[x_coordinate][y_coordinate + 1]

map[xStart].insert(yStart , "A")
del map[xStart][yStart + 1]

c = random.randint(0,16)
d = random.randint(0,8)
e = random.randint(0,16)
f = random.randint(0,8)
g = random.randint(0,16)
h = random.randint(0,8)
y = random.randint(0,16)
z = random.randint(0,8)
k = random.randint(0,16)
l = random.randint(0,8)

insertObstacle(map, c, d)
insertObstacle(map, e, f)
insertObstacle(map, g, h)
insertObstacle(map, y, z)
insertObstacle(map, k, l)

while not findDestination2(map, route, xStart, yStart):
    
    print("Routing", count)

    route = nodes.get()
    print(route)

    for jj in ["W", "E", "N", "S"]:
        put = route + jj
        if checkMoveValidity3(map, put, xStart,yStart):
            nodes.put(put)
    count = count + 1
    print()
        