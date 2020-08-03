import common
import math

def detect_slope_intercept(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# set line.m and line.b
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	line=common.Line()
	line.m=0
	line.b=0

	space = common.init_space(2000, 2000)

	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if image[y][x] == 0:
				for each in range(2000):
					# scaling to get from xy to mb scale
					m = (each / 100) - 10
					b = -m * x + y
					if 1000 > b > -1000:
						space[each][int(b) + 100] += 1

	maxi = float("-inf")
	for y in range(2000):
		for x in range(2000):
			if space[y][x] > maxi:
				maxi = space[y][x]
				# scale m according to y, so divide by 100, 20 vs 2000, and then -10 for x axis adjustment.
				line.m = (y / 100) - 10
				line.b = x - 100

	return line


def detect_circles(image):
	# PUT YOUR CODE HERE
	# access the image using "image[y][x]"
	# where 0 <= y < common.constants.WIDTH and 0 <= x < common.constants.HEIGHT 
	# to create an auxiliar bidimentional structure 
	# you can use "space=common.init_space(heigh, width)"

	radius = 30
	space = common.init_space(200, 200)
	count = 0

	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if image[y][x] == 0:
				for a in range(200):
					if (x - a)**2 < radius**2:
						b = y - math.sqrt(radius**2 - (x - a)**2)
						if 0 < b < 200:
							space[int(a)][int(b)] += 1

	for y in range(common.constants.HEIGHT):
		for x in range(common.constants.WIDTH):
			if space[y][x] > 45:
				count += 1

	return count
