import common


def part_one_classifier(data_train, data_test):

	weights = [0, 0, 0]

	incorrect = 1

	while incorrect > 0:

		incorrect = 0

		for i in range(common.constants.TRAINING_SIZE):

			gx = data_train[i][0] * weights[0] + data_train[i][1] * weights[1] + weights[2]

			if gx >= 0:
				y = 1
			else:
				y = 0

			# if y != y*, adjust the weights by adding or subtracting
			if y != data_train[i][2]:

				incorrect += 1

				if y == 1:
					# for each weight, multiply (y* by feature)
					for j in range(2):
						weights[j] -= data_train[i][j]

					# bias term
					weights[2] -= 1

				else:
					# for each weight, multiply (y* by feature)
					for j in range(2):
						weights[j] += data_train[i][j]

					# bias term
					weights[2] += 1

	# predict test data
	for m in range(common.constants.TEST_SIZE):
		num = data_test[m][0] * weights[0] + data_test[m][1] * weights[1] + weights[2]
		if num >= 0:
			data_test[m][2] = 1
		else:
			data_test[m][2] = 0


def part_two_classifier(data_train, data_test):

	prediction = [None for i in range(9)]
	weights = [[0 for row in range(3)] for x in range(9)]
	learning = 0.01
	steps = 0
	percent_correct = 0
	incorrect = 0

	for i in range(9):
		weights[i][2] = 1.0

	while percent_correct < 0.99 and steps < 3500:

		percent_correct = 0
		incorrect = 0
		steps += 1

		for i in range(common.constants.TRAINING_SIZE):

			arg_max = float("-inf")
			arg_index = 0

			for j in range(9):

				prediction[j] = weights[j][0] * data_train[i][0] + weights[j][1] * data_train[i][1] + weights[j][2]

				if prediction[j] > arg_max:

					arg_max = prediction[j]
					arg_index = j

			# if classified incorrectly, adjust weights
			target = int(data_train[i][2])

			if arg_index != target:

				incorrect += 1

				for m in range(2):
					weights[arg_index][m] -= learning * data_train[i][m]
					weights[target][m] += learning * data_train[i][m]

				weights[arg_index][2] -= learning
				weights[target][2] += learning

		percent_correct = (common.constants.TRAINING_SIZE - incorrect) / common.constants.TRAINING_SIZE


	for i in range(common.constants.TEST_SIZE):

		arg_max = float("-inf")
		arg_index = 0

		for j in range(9):

			prediction[j] = weights[j][0] * data_test[i][0] + weights[j][1] * data_test[i][1] + weights[j][2]

			if arg_max < prediction[j]:

				arg_index = j
				arg_max = prediction[j]

		data_test[i][2] = arg_index

