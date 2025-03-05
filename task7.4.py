def common_elements():
	x = {num for num in range(100) if num % 3 == 0}
	y = {num for num in range(100) if num % 5 == 0}
	return x & y

print(common_elements())