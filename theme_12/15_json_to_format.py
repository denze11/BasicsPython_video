import json


friends = [
	{'name': 'Max', 'age': 23, 'phones': [123, 234]},
	{'name': 'Leo', 'age': 33}
]

# смотрим тип объекта
print(type(friends))

# преобразуем список друзей в json
json_friends = json.dumps(friends)

# печатаем что получилось
print(json_friends)
# проверяем тип
print(type(json_friends))

# обратно из json в объект
friends = json.loads(json_friends)

print(friends)
print(type(friends))
