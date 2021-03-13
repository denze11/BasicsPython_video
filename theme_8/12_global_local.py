global_var = 1


def my_f():
	global global_var
	# Локальная переменная
	local_var = 100
	print(local_var)
	# Глобальная переменная, объявленная в модуле
	print(global_var)
	# Но эту переменную сейчас нельзя изменить
	global_var = 999


my_f()
print(global_var)
# А тут недоступна локальная переменная
# print(local_var)

