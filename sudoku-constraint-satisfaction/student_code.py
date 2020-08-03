import common


class variables:
	counter = 0


def sudoku_backtracking(sudoku):

	variables.counter = 0
	backtrack_recur(sudoku)
	return variables.counter


def backtrack_recur(sudoku):

	variables.counter += 1

	if is_complete(sudoku):
		return True

	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				for v in range(1, 10):
					if common.can_yx_be_z(sudoku, i, j, v):
						sudoku[i][j] = v
						if backtrack_recur(sudoku):
							return True
						sudoku[i][j] = 0
				return False


def sudoku_forwardchecking(sudoku):

	variables.counter = 0

	domain = [[[0 for v in range(9)] for j in range(9)] for i in range(9)]

	for i in range(9):
		for j in range(9):
			for v in range(1, 10):
				if common.can_yx_be_z(sudoku, i, j, v):
					domain[i][j][v-1] = 1
				else:
					domain[i][j][v-1] = 0

	forward_recur(sudoku, domain)

	return variables.counter


def forward_recur(sudoku, domain):

	variables.counter += 1
	# print(variables.counter)

	if is_complete(sudoku):
		return True

	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				for v in range(1, 10):
					if common.can_yx_be_z(sudoku, i, j, v):
						old_domain = [[j[:] for j in i] for i in domain]
						sudoku[i][j] = v
						if update_domain(domain, sudoku, i, j, v):
							if forward_recur(sudoku, domain):
								return True
						sudoku[i][j] = 0
						domain = [[j[:] for j in i] for i in old_domain]
				return False


def update_domain(domain, sudoku, row, col, v):
	pairsbefore = []
	for x in range(9):
		pairsbefore.append([row, x])
		pairsbefore.append([x, col])

	if row < 3:
		eachy = [0, 1, 2]
	elif 3 <= row < 6:
		eachy = [3, 4, 5]
	else:
		eachy = [6, 7, 8]

	if col < 3:
		eachx = [0, 1, 2]
	elif 3 <= col < 6:
		eachx = [3, 4, 5]
	else:
		eachx = [6, 7, 8]

	for boxy in eachy:
		for boxx in eachx:
			pairsbefore.append([boxy, boxx])

	pairs = []

	for each in pairsbefore:
		if each not in pairs:
			pairs.append(each)

	if [row, col] in pairs:
		pairs.remove([row, col])

	for each in pairs:
		if sudoku[each[0]][each[1]] == 0:
			domain[each[0]][each[1]][v-1] = 0
			if sum(domain[each[0]][each[1]]) == 0:
				return False
	return True


def is_complete(sudoku):
	for i in range(9):
		for j in range(9):
			if sudoku[i][j] == 0:
				return False
	return True


