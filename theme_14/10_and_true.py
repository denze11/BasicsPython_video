import math


# Есть спиок чисел
numbers = [4, 1, 2, 3, -4, -2, 7, 16]

# Создать список из тех чисел которые имеют квадратный корень меньше 2 [1, 2, 3]

result = []
#Обычный способ
for number in numbers:
	if number > 0:
		sqrt = math.sqrt(number)
		# квадратный корень меньше 2
		if sqrt < 2:
			result.append(number)
print(result)

result = []
# через ленивый and
for number in numbers:
	if number > 0 and math.sqrt(number) < 2:
		result.append(number)

print(result)

#  через генератор
result = [number for number in numbers if number > 0 and math.sqrt(number) < 2]
print(result)
