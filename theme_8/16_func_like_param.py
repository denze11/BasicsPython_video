def f():
	print('hello from other f')


def to(f_param):
	# параметр будет функция
	# поэтому в теле функции to мы ее вызовем
	f_param()

# проверим
to(f)
