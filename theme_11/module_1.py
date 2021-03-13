'''Создайте модуль (модуль - программа на Python, т.е. файл с расширением .py). В нем создайте функцию создающую директории от dir_1 до dir_9 в папке из которой запущен данный код. Затем создайте вторую функцию удаляющую эти папки. Проверьте работу функций в этом же модуле.'''

import os


def new_folder():
	for i in range(1, 10):
		new_path = f'theme_11/my_folder_{i}'
		os.mkdir(new_path)

def del_folder():
	for i in range(1, 10):
		new_path = f'theme_11/my_folder_{i}'
		os.rmdir(new_path)
