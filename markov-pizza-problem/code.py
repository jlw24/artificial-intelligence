import common

curr = [[None for i in range(6)] for j in range(6)]
# south, west, north, east in terms of coordinates
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]


def drone_action(policies, values, y, x, battery_drop_cost, discount):

	# value modification

	# initialize max q
	q_max = float("-inf")

	# for each available action from 1-9, on and off
	for act in range(1, 9):

		q = 0

		# loop through different moves, from S, W, N, E
		for d in range(4):

			# storing the coordinate of next state
			movey = y + directions[d][0]
			movex = x + directions[d][1]

			# find the probability of the move
			probability = find_probability(act, y, x, movey, movex)

			# determine if ON or OFF power zoom
			if 1 <= act <= 4:
				reward = -battery_drop_cost
			if 5 <= act <= 8:
				reward = -2 * battery_drop_cost

			# determine if drone bounces off the map or not
			if 6 > movex >= 0 and 6 > movey >= 0:
				q += probability * (reward + discount * curr[movey][movex])

			# if it does bounce off
			else:
				if movex > 5:
					q += probability * (reward + discount * curr[movey][movex - 1])

				if movey > 5:
					q += probability * (reward + discount * curr[movey - 1][movex])

				if movex < 0:
					q += probability * (reward + discount * curr[movey][movex + 1])

				if movey < 0:
					q += probability * (reward + discount * curr[movey + 1][movex])

		# after seeing each action S, W, N, E
		# ensures that OFF zoom goes first in that order
		# chance the policy for that square to be action between 1-9

		if q > q_max:
			q_max = q
			policies[y][x] = act

		values[y][x] = q_max


def drone_flight_planner(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount):
	# PUT YOUR CODE HERE
	# access the map using "map[y][x]"
	# access the policies using "policies[y][x]"
	# access the values using "values[y][x]"
	# y between 0 and 5
	# x between 0 and 5
	# function must return the value of the cell corresponding to the starting position of the drone
	# return 100000000

	# return flight_plan(map, policies, values, delivery_fee, battery_drop_cost, dronerepair_cost, discount)
	# find the exits which is pizza delivery and rival, values and policies updated
	# exit_search(map, policies, values, delivery_fee, dronerepair_cost)

	for y in range(6):
		for x in range(6):

			if map[y][x] == common.constants.CUSTOMER:
				values[y][x] = delivery_fee
				policies[y][x] = common.constants.EXIT

			if map[y][x] == common.constants.RIVAL:
				values[y][x] = -dronerepair_cost
				policies[y][x] = common.constants.EXIT

	# start with converged is false, since it has not converged
	converged = False

	# keep looping while values do not converge yet
	while not converged:

		# old value is kept, at first iteration curr is blank
		old = [row[:] for row in curr]

		# curr is set to the values before any action is taken
		for y in range(6):
			for x in range(6):
				curr[y][x] = values[y][x]

		# for each square, if it is not a customer or rival, then drone should take action
		for y in range(6):
			for x in range(6):
				if map[y][x] != common.constants.CUSTOMER and map[y][x] != common.constants.RIVAL:
					drone_action(policies, values, y, x, battery_drop_cost, discount)

		# if the values do not change, then they converged, exit while loop
		if curr == old:
			converged = True

	# return the expected utility of the drone from the pizza shop box
	value = 0
	for y in range(6):
		for x in range(6):
			# if it's pizza shop
			if map[y][x] == 1:
				value = values[y][x]
	return value


# look for probability depending on the movement of the drone with wind
def find_probability(act, y, x, movey, movex):

	if act == common.constants.SOFF:
		if movey == y + 1:
			probability = 0.7
		if movey == y - 1:
			probability = 0
		if movex == x + 1 or movex == x - 1:
			probability = 0.15
		return probability
		
	elif act == common.constants.SON:
		if movey == y + 1:
			probability = 0.8
		if movey == y - 1:
			probability = 0
		if movex == x + 1 or movex == x - 1:
			probability = 0.1
		return probability

	elif act == common.constants.EOFF:
		if movex == x + 1:
			probability = 0.7
		if movex == x - 1:
			probability = 0
		if movey == y + 1 or movey == y - 1:
			probability = 0.15
		return probability
		
	elif act == common.constants.EON:
		if movex == x + 1:
			probability = 0.8
		if movex == x - 1:
			probability = 0
		if movey == y + 1 or movey == y - 1:
			probability = 0.1
		return probability
		
	elif act == common.constants.NOFF:
		if movey == y - 1:
			probability = 0.7
		if movey == y + 1:
			probability = 0
		if movex == x + 1 or movex == x - 1:
			probability = 0.15
		return probability
		
	elif act == common.constants.NON:
		if movey == y - 1:
			probability = 0.8
		if movey == y + 1:
			probability = 0
		if movex == x + 1 or movex == x - 1:
			probability = 0.1
		return probability

	elif act == common.constants.WOFF:
		if movex == x - 1:
			probability = 0.7
		if movex == x + 1:
			probability = 0
		if movey == y + 1 or movey == y - 1:
			probability = 0.15
		return probability

	# WON
	else:
		if movex == x - 1:
			probability = 0.8
		if movex == x + 1:
			probability = 0
		if movey == y + 1 or movey == y - 1:
			probability = 0.1
		return probability
