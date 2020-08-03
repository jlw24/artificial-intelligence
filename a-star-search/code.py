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


def findDistance(y1, x1, y2, x2):
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance


def findParent(parent, indexY, indexX):
    return parent[indexY][indexX]


def pick_best_child(tiecoord):
    # input is list of indexes of minimum score and frontier coordinate list
    # output is index in frontier list to pop

    bestX = sorted(tiecoord, key=lambda x: (x[1], x[0]))

    return bestX[0]


def astar_search(map):
    found = False
    # PUT YOUR CODE HERE
    # access the map using "map[y][x]"
    # y between 0 and common.constants.MAP_HEIGHT-1
    # x between 0 and common.constants.MAP_WIDTH-1

    map_height = len(map)
    map_width = len(map[0])

    startY, startX = findStartIndex(map)
    endY, endX = findEndIndex(map)

    parent = [[None for i in range(map_width)] for j in range(map_height)]

    travel = [[None for i in range(map_width)] for j in range(map_height)]

    frontier = [[startY, startX]]

    travel[startY][startX] = 0

    while len(frontier) > 0:

        score = []
        minlist = []
        tiecoord = []

        for each in frontier:
            gn = travel[each[0]][each[1]]
            hn = findDistance(endY, endX, each[0], each[1])
            fn = gn + hn

            score.append(fn)

        for i in range(len(score)):
            if score[i] == min(score):
                minlist.append(i)
                tiecoord.append(frontier[i])

        if len(minlist) == 1:
            curr_idx = frontier.pop(minlist[0])
        else:
            curr_idx = frontier.pop(frontier.index(pick_best_child(tiecoord)))

        map[curr_idx[0]][curr_idx[1]] = 4  # mark node explored

        if curr_idx[0] == endY and curr_idx[1] == endX:

            found = True
            map[curr_idx[0]][curr_idx[1]] = 5

            # mark all nodes in path 5
            while curr_idx != [startY, startX]:
                parentY, parentX = findParent(parent, curr_idx[0], curr_idx[1])
                map[parentY][parentX] = 5
                curr_idx[0] = parentY
                curr_idx[1] = parentX

            break

        if (curr_idx[0] - 1 >= 0) and (
                map[curr_idx[0] - 1][curr_idx[1]] == 0 or map[curr_idx[0] - 1][curr_idx[1]] == 3):  # up
            frontier.append([curr_idx[0] - 1, curr_idx[1]])
            parent[curr_idx[0] - 1][curr_idx[1]] = [curr_idx[0], curr_idx[1]]
            travel[curr_idx[0] - 1][curr_idx[1]] = travel[curr_idx[0]][curr_idx[1]] + 1

        if (curr_idx[1] - 1 >= 0) and (
                map[curr_idx[0]][curr_idx[1] - 1] == 0 or map[curr_idx[0]][curr_idx[1] - 1] == 3):  # left
            frontier.append([curr_idx[0], curr_idx[1] - 1])
            parent[curr_idx[0]][curr_idx[1] - 1] = [curr_idx[0], curr_idx[1]]
            travel[curr_idx[0]][curr_idx[1] - 1] = travel[curr_idx[0]][curr_idx[1]] + 1

        if (curr_idx[0] + 1 < map_height) and (
                map[curr_idx[0] + 1][curr_idx[1]] == 0 or map[curr_idx[0] + 1][curr_idx[1]] == 3):  # down
            frontier.append([curr_idx[0] + 1, curr_idx[1]])
            parent[curr_idx[0] + 1][curr_idx[1]] = [curr_idx[0], curr_idx[1]]
            travel[curr_idx[0] + 1][curr_idx[1]] = travel[curr_idx[0]][curr_idx[1]] + 1

        if (curr_idx[1] + 1 < map_width) and (
                map[curr_idx[0]][curr_idx[1] + 1] == 0 or map[curr_idx[0]][curr_idx[1] + 1] == 3):  # right
            frontier.append([curr_idx[0], curr_idx[1] + 1])
            parent[curr_idx[0]][curr_idx[1] + 1] = [curr_idx[0], curr_idx[1]]
            travel[curr_idx[0]][curr_idx[1] + 1] = travel[curr_idx[0]][curr_idx[1]] + 1

    return found
