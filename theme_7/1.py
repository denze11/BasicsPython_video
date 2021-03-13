import random

user_number = None
number_one = 1
number_two = 100

while user_number != '=':
	pc_number = random.randint(number_one, number_two)
	print(pc_number)
	user_number = input('Введите значение >, < или =: ')
	if user_number == '>':
		print('Число больше')
		number_one = pc_number +1
	elif user_number == '<':
		print('Число меньше')
		number_two = pc_number - 1

print('Число угадано!')
