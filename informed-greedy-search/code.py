QUEENS = 10

def find_queen(board, x):
    for i in range(10):
        if board[i][x] == 1:
            return [i, x]


def get_diagonal(board, queen):
    y = queen[0]
    x = queen[1]
    diagonals = []

    xleftup = x - 1
    yleftup = y - 1

    xleftdown = x - 1
    yleftdown = y + 1

    xrightup = x + 1
    yrightup = y - 1

    xrightdown = x + 1
    yrightdown = y + 1

    while yleftup >= 0 and xleftup >= 0:
        diagonals.append(board[yleftup][xleftup])
        yleftup -= 1
        xleftup -= 1

    while yleftdown <= 9 and xleftdown >= 0:
        diagonals.append(board[yleftdown][xleftdown])
        yleftdown += 1
        xleftdown -= 1

    while yrightup >= 0 and xrightup <= 9:
        diagonals.append(board[yrightup][xrightup])
        yrightup -= 1
        xrightup += 1

    while yrightdown <= 9 and xrightdown <=9:
        diagonals.append(board[yrightdown][xrightdown])
        yrightdown += 1
        xrightdown += 1

    return sum(diagonals)


def attack_number(board):

    total_attacks = 0

    for j in range(10):
        attacks = 0
        queen = find_queen(board, j)
        # row attack
        attacks += (sum(board[queen[0]]) - 1)
        # diagonal attack
        attacks +=  get_diagonal(board, queen)
        total_attacks += attacks

    return total_attacks


def find_next_step(board):

    width = 10
    boardstorage = []
    columnattacknumber = []
    curr_attacks = attack_number(board)
    testnumber = 0

    for i in range(width):
        indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        queen = find_queen(board, i)
        indexes.remove(queen[0])
        bestboard = [row[:] for row in board]

        for line in indexes:
            testnumber += 1
            newboard = [row[:] for row in board]
            newboard[queen[0]][queen[1]] = 0
            newboard[line][i] = 1
            new_attack_num = attack_number(newboard)
            if new_attack_num < curr_attacks:
                curr_attacks = new_attack_num
                bestboard = [row[:] for row in newboard]

        curr_attacks = attack_number(board)
        boardstorage.append(bestboard)
        columnattacknumber.append(attack_number(bestboard))

    lowestattacks = min(columnattacknumber)
    next_index = columnattacknumber.index(lowestattacks)
    next_step = boardstorage[next_index]

    return next_step, lowestattacks



def gradient_search(board):
    # put yor code here

    curr_board = [row[:] for row in board]
    new_board, new_attack_num = find_next_step(curr_board)

    while new_board != curr_board:
        curr_board = [row[:] for row in new_board]
        new_board, new_attack_num = find_next_step(curr_board)

    for i in range(10):
        for j in range(10):
            board[i][j] = 0

    for i in range(10):
        y, x = find_queen(new_board, i)
        board[y][x] = 1

  #  attack = attack_number(board)

    if new_attack_num == 0:
        return True
    else:
        return False

