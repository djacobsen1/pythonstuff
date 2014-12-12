def fibonacci(x, y, counter):
	z = x + y
	print "{} and {} = {}".format(x, y, z)
	if counter < 10:
		counter = counter + 1
		fibonacci(y, z, counter)
fibonacci(0, 1, 1)