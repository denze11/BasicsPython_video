'''Создать модуль music_deserialize.py. В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию. И получить объект: словарь из предыдущего задания.'''

import json
import pickle


with open('theme_13/group.json', 'r', encoding='utf-8') as f:
	#преобразуем список друзей в json и сохраняем в файл
	my_favourite_group = json.load(f)

print(my_favourite_group)

with open('theme_13/group.pickle', 'rb') as f:
	# сразу пишем объект целиком с помощью pickle
	my_favourite_group = pickle.load(f)

print(my_favourite_group)
