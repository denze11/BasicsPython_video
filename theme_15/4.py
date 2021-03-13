import math


numbers = int(input('Введите число от 1 до 100: '))

def error_detect(item):
	if 0 < item < 100:
		try:
			if item == 13:
				raise ValueError('Введено не коректное число 13')
		except ValueError as e:
			return ('Программа завершила работу с ошибкой', e)
		else:
			return (f'Ваше число возведенное в корень: {item*item}')
	else:
		return ('Вы ввели число меньше 0 или больше 100')

print(error_detect(numbers))
