import common


def maximizer(board, prune, alpha, beta):

	status = common.game_status(board)

	if (status != 0) or (is_complete(board) and status == 0):
		if status == 2:
			return -1
		else:
			return status
	else:
		v = float('-inf')
		for i in range(9):
			if board[i] == 0:
				board[i] = 1
				v = max(v, minimizer(board, prune, alpha, beta))
				board[i] = 0
				if prune:
					if v >= beta:
						return v
					alpha = max(alpha, v)
		return v


def minimizer(board, prune, alpha, beta):

	status = common.game_status(board)

	if (status != 0) or (is_complete(board) and status == 0):
		if status == 2:
			return -1
		else:
			return status
	else:
		v = float('inf')
		for i in range(9):
			if board[i] == 0:
				board[i] = 2
				v = min(v, maximizer(board, prune, alpha, beta))
				board[i] = 0
				if prune:
					if v <= alpha:
						return v
					beta = min(beta, v)
		return v


def minmax_tictactoe(board, turn):

	prune = False
	alpha = None
	beta = None

	if turn == common.constants.X:
		result = maximizer(board, prune, alpha, beta)
	else:
		result = minimizer(board, prune, alpha, beta)
	if result == -1:
		result = 2

	return result

	# result = maximizer(board, prune, alpha, beta) if turn == 1 else minimizer(board, prune, alpha, beta)
	#
	# return 2 if result == -1 else result

def abprun_tictactoe(board, turn):

	prune = True
	alpha = float('-inf')
	beta = float('inf')

	if turn == common.constants.X:
		result = maximizer(board, prune, alpha, beta)
	else:
		result = minimizer(board, prune, alpha, beta)

	if result == -1:
		result = 2

	return result


def is_complete(board):

	for each in board:
		if each == 0:
			return False

	return True
