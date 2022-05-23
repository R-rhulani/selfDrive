import queue
import time
import random
import sys

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
    map.append(["#","A", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#","#", "#", "#", "#", "#"])
    map.append(["#"," ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "#"])
    map.append(["#"," ", "#", " ", "#", "#", "#", "#", "#"," ", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#"," ", "#", " ", " ", " ", " ", " ", " "," ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#"," ", " ", " ", "#", "#", "#", "#", "#"," ", "#", " ", "#", "#", "#", "#", "#"])
    map.append(["#"," ", "#", " ", " ", " ", " ", " ", " "," ", "#", " ", " ", " ", " ", " ", "#"])
    map.append(["#"," ", "#", " ", "#", "#", "#", " ", "#","#", "#", " ", "#", "#", " ", "#", "#"])
    map.append(["#"," ", " ", " ", " ", " ", " ", " ", " "," ", " ", " ", " ", " ", " ", " ", "#"])
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
        print("map[",j,"][",i,"] Lalalalalala")

        if (map[j][i] == "O"):
            if(map[j+1][i]=="#" or map[j-1][i]=="#"):
                i = i - 1

            if(map[j][i+1]=="#" or map[j][i-1]=="#"):
                j = j - 1

            var1 = j
            var2 = i
            print("Lalalalalala")
            nodes = queue.Queue()
            nodes.put("")
            route = ""
            map  = drawMap()
            del map[0][1]
            del map[j][i]
            map[0].insert(1, "#")
            map[j].insert(i, "A")
            map[x_coordinate].insert(y_coordinate , "B")
            del map[x_coordinate][y_coordinate + 1]
            insertObstacle(map, c, d)
            insertObstacle(map, e, f)
            insertObstacle(map, g, h)
            insertObstacle(map, y, z)
            insertObstacle(map, k, l)
            # insertBlocker()
            # while not findDestination(map, route):
            while not  reroute(map,route, var1, var2):
                print("Rerouting",count)
                route = nodes.get()
                print(route)
                # printMap(map,route)
                # printMap(map, route)
                # time.sleep(1)
                for jj in ["W", "E", "N", "S"]:
                    put = route + jj
                    if checkMoveValidity2(map, put, var1, var2):
                        nodes.put(put)
                count = count + 1
                position = currPosition(route)
                print(position)


        c = random.randint(0,15)
        ctemp = map[3][c]

        # if (count == 3 ):
        # insertDog(map, c)
        # sensor(map, position)

        print("\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(1)
        count = count + 1

        # removeDog(map, c, ctemp)
        # map[3].insert(c, ctemp)
        # del map[3][c + 1]

    # for j, row in enumerate(map):
    #     for i, col in enumerate(row):
    #         if (j, i) in position:
    #             print("+ ", end="")
    #         else:
    #             print(col + " ", end="")
    print("Arrived at destination, Goodbye!")
    return

def drive2(map, path, varj, vari):
    i = vari
    j = varj
    for x, position in enumerate(map[0]):
        print("map[",j,"][",i,"]")
        print(map[j][i], "ha ha ha ha drive 2")
        if position == "O":
            begin = x
    
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

        print("\n\n\n")
        printMap(map,position)
        print("\n")
        time.sleep(1)
        count = count + 1

        # removeDog(map, c, ctemp)
        # map[3].insert(c, ctemp)
        # del map[3][c + 1]

    # for j, row in enumerate(map):
    #     for i, col in enumerate(row):
    #         if (j, i) in position:
    #             print("+ ", end="")
    #         else:
    #             print(col + " ", end="")
    print("Arrived at destination, Goodbye!")
    sys.exit()


def reroute(map, directions, varj, vari):
    i = vari
    j = varj
    begin = i
    print("enumerate(map[", i,"] ana j is ",j,)
    for x, position in enumerate(map[0]):
        print(position, "ha ha ha ha check reroute")
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
    print("j = ",j," and i = ",i)
    if map[j][i] == "B":
        print("The directions from A to B are: " + directions)
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


def checkMoveValidity2(map, directions,varj,vari):
    i = vari
    j = varj
    begin = i
    for x, position in enumerate(map[0]):
        print(position, "ha ha ha ha check validity 2")
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
        print("if not(0 <= ", i,"< ",len(map[0])," and 0 <= ", j," < ",len(map ),")")
        if not(0 <= i < len(map[0]) and 0 <= j < len(map)):
            return False
        elif (map[j][i] == "O" or map[j][i] == "#"):
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

    if map[j][i] == "B":
        print("The directions from A to B are: " + directions)
        drive(map, directions)
        return True
    print()
    return False

nodes = queue.Queue()
nodes.put("")
route = ""
map  = drawMap()
map2  = drawMap1()
count = 0

x_coordinate = int (input("Please enter x coordinate of destination(from 0 - 7)"))
y_coordinate = int (input("Please enter y coordinate of destination(from 0 - 15)"))

map[x_coordinate].insert(y_coordinate , "B")
del map[x_coordinate][y_coordinate + 1]
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

while not findDestination(map, route):
    
    print("Routing", count)

    route = nodes.get()
    print(route)

    for jj in ["W", "E", "N", "S"]:
        put = route + jj
        if checkMoveValidity(map, put):
            nodes.put(put)
    count = count + 1
    print()
        