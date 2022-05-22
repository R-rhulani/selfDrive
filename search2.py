import queue
import time
import random

def drawMap1():
    map = []###  1   2    3    4    5    6    7    8    9    10   11   12   13  14   15   16   17   18   19   20  
    map.append(["#", "A", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
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
    map.append(["#", " ", " ", "#", " ", " ", "#", " ", " ", " ", " ", " ", "#"])
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
    map.append(["#","A", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])
    map.append(["#"," ", " ", "D", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#"," ", "#", "#", "#", " ", "#", "#", "#", "#", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#"," ", " ", " ", " ", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#","#", "#", "#", "#", "#", "#", "#", "#", " ", "#", " ", "#", " ", " ", " ", "#"])
    map.append(["#"," ", "#", " ", "#", " ", " ", " ", " ", " ", "#", " ", "#", " ", " ", " ", "#"])
    map.append(["#"," ", "#", " ", "#", "#", "#", " ", "#", "#", "#", "#", "#", "#", " ", "#", "#"])
    map.append(["#"," ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#","#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"])

    return map

def printMap2(map, position): 
    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in position:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()

def printMap(map, position): 
    for j, row in enumerate(map):
        for i, col in enumerate(row):
                if (map[j][i]=="D"):
                    reroute(map, j, i)
                else: 
                    if (j, i) in position:    
                        print("+ ", end="")  
                    else:
                        print(col + " ", end="")
        print()


def insertDog (map, c):
    map[1].insert(3, 'D')
    del map[1][4]

    return map

def removeDog (map, c, ctemp):
    map[1].insert(3, ctemp)
    del map[1][4]
    return map

        

def drive(map, path=""):
    for x, position in enumerate(map[0]):
        if position == "A":
            begin = x

    i = begin
    j = 0
    position = set()
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


        # c = random.randint(0,5)
        c = 3
        ctemp = map[1][3]
        insertDog(map, 3)
        print("\n\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(1)
        removeDog(map, c, ctemp)


    for j, row in enumerate(map):
        for i, col in enumerate(row):
            if (j, i) in position:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


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


def reroute(map, j, i):

    directions = ""
    for direction in directions:
        if direction == "W":
            i = i - 1

        elif direction == "E":
            i = i + 1

        elif direction == "N":
            j = j - 1

        elif direction == "S":
            j = j + 1

    if map[j][i] == "B":
        print("The directions from A to B are: " + directions)
        drive(map, directions)
        return True

    return False



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

    if map[j][i] == "B":
        print("The directions from A to B are: " + directions)
        drive(map, directions)
        return True

    return False

nodes = queue.Queue()
nodes.put("")
route = ""
map  = drawMap()
map2  = drawMap1()
count = 0

x_coordinate = int (input("Please enter x coordinate (from 0 - 7)"))
y_coordinate = int (input("Please enter y coordinate (from 0 - 15)"))

map[x_coordinate].insert(y_coordinate , 'B')
del map[x_coordinate][y_coordinate + 1]


while not findDestination(map, route):

    print(count)
    route = nodes.get()
    print(route)
    # printMap(map, route)
    # time.sleep(1)
    for j in ["W", "E", "N", "S"]:
        put = route + j
        if checkMoveValidity(map, put):
            nodes.put(put)
    count = count + 1