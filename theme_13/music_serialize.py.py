'''Создать модуль music_serialize.py. В этом модуле определить словарь для вашей любимой музыкальной группы, например:

my_favourite_group = {
	‘name’: ‘Г.М.О.’,
	‘tracks’: [‘Последний месяц осени’, ‘Шапито’],
    ‘Albums’: [{‘name’: ‘Делать панк-рок’, ‘year’: 2016},
    {‘name’: ‘Шапито’, ‘year’: 2014}]
}
С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал. Записать результаты в файлы group.json, group.pickle соответственно. В файле group.json указать кодировку utf-8.'''

import json
import pickle


my_favourite_group = {
	'name': 'Г.М.О.',
    'tracks': ['Последний месяц осени', 'Шапито'],
    'Albums': [
		{'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
	]
}

j_group = json.dumps(my_favourite_group)
print(j_group)

p_group = pickle.dumps(my_favourite_group)

with open('theme_13/group.json', 'w', encoding='utf-8') as f:
	#преобразуем список друзей в json и сохраняем в файл
	json_friends = json.dump(my_favourite_group, f)

print('Объект json записан')

with open('theme_13/group.pickle', 'wb') as f:
	# сразу пишем объект целиком с помощью pickle
	pickle.dump(my_favourite_group, f)

print('Объект pickle записан')
