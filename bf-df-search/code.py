import common

def findStartIndex(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 2:
                return [y, x]


def findEndIndex(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 3:
                return [y, x]


def findParent(parent, indexY, indexX):
    return parent[indexY][indexX]


def df_search(map):
    found = False
    # PUT YOUR CODE HERE
    map_height = len(map)
    map_width = len(map[0])

    parent = [[None for i in range(map_width)] for j in range(map_height)]

    startY, startX = findStartIndex(map)
    endY, endX = findEndIndex(map)

    frontier = [[startY, startX]]

    while len(frontier) > 0:

        currIdx = frontier.pop()  # pop stack last element

        map[currIdx[0]][currIdx[1]] = 4  # mark node explored

        # if goal is found, mark 5
        if currIdx[0] == endY and currIdx[1] == endX:
            found = True
            map[currIdx[0]][currIdx[1]] = 5

            # mark all nodes in path 5
            while currIdx != [startY, startX]:
                parentY, parentX = findParent(parent, currIdx[0], currIdx[1])
                map[parentY][parentX] = 5
                currIdx[0] = parentY
                currIdx[1] = parentX

            break

        # up, left, down, right because it's reversed
        # if child is either the goal or not explored. don't count walls and explored nodes.

        if (currIdx[0] - 1 >= 0) and (map[currIdx[0] - 1][currIdx[1]] == 0 or map[currIdx[0] - 1][currIdx[1]] == 3):  # up
            frontier.append([currIdx[0] - 1, currIdx[1]])
            parent[currIdx[0] - 1][currIdx[1]] = [currIdx[0], currIdx[1]]

        if (currIdx[1] - 1 >= 0) and (map[currIdx[0]][currIdx[1] - 1] == 0 or map[currIdx[0]][currIdx[1] - 1] == 3):  # left
            frontier.append([currIdx[0], currIdx[1] - 1])
            parent[currIdx[0]][currIdx[1] - 1] = [currIdx[0], currIdx[1]]

        if (currIdx[0] + 1 < map_height) and (map[currIdx[0] + 1][currIdx[1]] == 0 or map[currIdx[0] + 1][currIdx[1]] == 3):  # down
            frontier.append([currIdx[0] + 1, currIdx[1]])
            parent[currIdx[0] + 1][currIdx[1]] = [currIdx[0], currIdx[1]]

        if (currIdx[1] + 1 < map_width) and ( map[currIdx[0]][currIdx[1] + 1] == 0 or map[currIdx[0]][currIdx[1] + 1] == 3):  # right
            frontier.append([currIdx[0], currIdx[1] + 1])
            parent[currIdx[0]][currIdx[1] + 1] = [currIdx[0], currIdx[1]]

    return found


# First [y][x+1], then [y+1][x], then [y][x-1], and finally [y-1][x]
# access the map using "map[y][x]"
# y between 0 and common.constants.MAP_HEIGHT-1
# x between 0 and common.constants.MAP_WIDTH-1


def bf_search(map):
    found = False;
    # PUT YOUR CODE HERE
    map_height = len(map)
    map_width = len(map[0])

    # visited = [[0 for i in range(map_width)] for j in range(map_height)]

    parent = [[None for i in range(map_width)] for j in range(map_height)]

    startY, startX = findStartIndex(map)

    endY, endX = findEndIndex(map)

    frontier = [[startY, startX]]

    # while frontier is not empty, take a node out of the frontier stack, since it's DFS
    while len(frontier) > 0:

        currIdx = frontier.pop(0)  # pop queue head element

        map[currIdx[0]][currIdx[1]] = 4

        if currIdx[0] == endY and currIdx[1] == endX:
            found = True
            map[currIdx[0]][currIdx[1]] = 5

            while currIdx != [startY, startX]:
                parentY, parentX = findParent(parent, currIdx[0], currIdx[1])
                map[parentY][parentX] = 5
                currIdx[0] = parentY
                currIdx[1] = parentX

            break

        if (currIdx[1] + 1 < map_width) and (map[currIdx[0]][currIdx[1] + 1] == 0 or map[currIdx[0]][currIdx[1] + 1] == 3):  # right
            frontier.append([currIdx[0], currIdx[1] + 1])
            parent[currIdx[0]][currIdx[1] + 1] = [currIdx[0], currIdx[1]]

        if (currIdx[0] + 1 < map_height) and (map[currIdx[0] + 1][currIdx[1]] == 0 or map[currIdx[0] + 1][currIdx[1]] == 3):  # down
            frontier.append([currIdx[0] + 1, currIdx[1]])
            parent[currIdx[0] + 1][currIdx[1]] = [currIdx[0], currIdx[1]]

        if (currIdx[1] - 1 >= 0) and (map[currIdx[0]][currIdx[1] - 1] == 0 or map[currIdx[0]][currIdx[1] - 1] == 3):  # left
            frontier.append([currIdx[0], currIdx[1] - 1])
            parent[currIdx[0]][currIdx[1] - 1] = [currIdx[0], currIdx[1]]

        if (currIdx[0] - 1 >= 0) and (map[currIdx[0] - 1][currIdx[1]] == 0 or map[currIdx[0] - 1][currIdx[1]] == 3):  # up
            frontier.append([currIdx[0] - 1, currIdx[1]])
            parent[currIdx[0] - 1][currIdx[1]] = [currIdx[0], currIdx[1]]

    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1

    return found
