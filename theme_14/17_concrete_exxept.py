number = int(input('Введите число: '))

try:
	result = 100 / number
except ZeroDivisionError:
	print('На 0 делить нельзя!')
except Exception:
	print('Неизвестная ошибка')

print('Конец')
