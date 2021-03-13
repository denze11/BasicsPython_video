import math


if 2 > 1 or math.sqrt(-1):
	print('Ошибки не будет т.к. первое условие истина')

# Первая истина
print(0 or [] or 8 or 5)

# Последняя лож
print(0 or [] or () or {} or 0)
