import json


friends = [
	{'name': 'Max', 'age': 23, 'phones': [123, 234]},
	{'name': 'Leo', 'age': 33}
]

# смотрим тип объекта
print(type(friends))

# откроем файл
with open('theme_12/friends.jon', 'w') as f:
	#преобразуем список друзей в json и сохраняем в файл
	json_friends = json.dump(friends, f)


# обратно из файла в объект
with open('theme_12/friends.jon', 'r') as f:
	friends = json.load(f)

print(friends)
print(type(friends))
