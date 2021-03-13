def greeting(say, *args):
	print(say, args)


greeting('Hello', 'Leo')


greeting('Hello', 'Leo', 'Max')
greeting('Hello', 'Leo', 'Max', 'Kate')


def get_person(**kwargs):
	for k, v in kwargs.items():
		print(k, v)


get_person(name='Leo', age=20, has_car=True)
