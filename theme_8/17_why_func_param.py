def my_filter(numbers, function):
	result = []
	for number in numbers:
		if function(number):
			result.append(number)
	return result		


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

print(my_filter(numbers, lambda number: number % 2 == 0))


# если нужны нечетные числа
print(my_filter(numbers, lambda number: number % 2 != 0))


# если нужны числа > 4
print(my_filter(numbers, lambda number: number > 4))
