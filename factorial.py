def factorial(num):
	if num < 0:
		print("Negative doesn't work here son.")
	elif num == 0:
		product = 1
	else:
		for i in range(num, 0, -1):
			if i == num:
				product = i
			else:
				product *= i
	return product