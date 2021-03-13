global_var = 2


def my_f():
	result = global_var ** 5
	print(result)


def my_change_f():
	global global_var
	global_var = 'Какая то строка'	


my_change_f()
my_f()
