def greeting(who, say):
	print(say, who)


greeting('Leo', 'Hi')
# не верно
greeting('Hi', 'Leo')
greeting(say='Hi', who='Leo')
