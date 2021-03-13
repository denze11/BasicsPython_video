import pickle


person = {'name': 'Max', 'phones': [123, 345], 'age': 20}

# открываем файл
with open('theme_12/person.dat', 'wb') as f:
	# сразу пишем объект целиком с помощью pickle
	pickle.dump(person, f)

print('Объект записан')
