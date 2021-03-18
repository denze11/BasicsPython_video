# Функция для создания файла
import os
import shutil
import datetime


def create_file(name, text=None):
	with open(name, 'w', encoding='utf-8') as f:
		save_info(f'Файл {name} был создан')
		if text:
			f.write(text)
			save_info(f'Файл с текстом внутри {name}')


def create_folder(name):
	try:
		os.mkdir(name)
		save_info(f'Папка {name} была создана')
	except FileExistsError:
		print('Такая папка уже есть')


def get_list(path, folders_only=False):
	result = os.listdir(path)
	if folders_only:
		result = [f for f in result if os.path.isdir(f)]
	print(result)


def delete_file(name):
	try:
		if os.path.isdir(name):
			os.rmdir(name)
			save_info(f'Папка {name} была удалена')
		else:
			os.remove(name)
			save_info(f'Файл {name} был удален')
	except FileNotFoundError:
		print('Нет такого файлап или папки')


def copy_file(name, new_name):
	if os.path.isdir(name):
		try:
			shutil.copytree(name, new_name)
			save_info(f'Папка {name} была скопирована в {new_name}')
		except FileExistsError:
			print('Такой файл уже есть')
	else:
		shutil.copy(name, new_name)
		save_info(f'Файл {name} был скопирован в {new_name}')


def save_info(message):
	current_time = datetime.datetime.now()
	result = f'{current_time} - {message}'
	with open('theme_16/log.txt', 'a', encoding='utf-8') as f:
		f.write(result + '\n')


if __name__ == '__main__':
	create_file('theme_16/text.dat')
	create_file('theme_16/text.dat', text='some text')
	create_folder('theme_16/new_f')
	get_list('/home/denze1/Projects/Ucheba/GeekBrains/BasicsPython_video/theme_14')
	get_list('theme_16', True)
	delete_file('theme_16/new_f1')
	delete_file('theme_16/text.dat')
	create_file('theme_16/text.dat')
	copy_file('theme_16/new_f', 'theme_16/new_2')
	copy_file('theme_16/text.dat', 'theme_16/text2.dat')
	save_info('abc')
