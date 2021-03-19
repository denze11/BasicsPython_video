import sys
from theme_16.core import create_file, create_folder, get_list, delete_file, copy_file, save_info, guess_the_number


command = sys.argv[1]
if command == 'list':
	get_list('theme_16')
elif command == 'create_file':
	try:
		name = sys.argv[2]
	except IndexError:
		print('Вы не указали путь до файла')
	else:
		create_file(name)
elif command == 'create_folder':
	try:
		name = sys.argv[2]
	except IndexError:
		print('Вы не указали путь до папки')
	else:
		create_folder(name)
elif command == 'delete':
	try:
		name = sys.argv[2]
	except IndexError:
		print('Вы не указали путь до папки или файла')
	else:
		delete_file(name)
elif command == 'copy':
	try:
		name = sys.argv[2]
	except IndexError:
		print('Вы не указали папку или файл для копирования')
	try:
		new_name = sys.argv[3]
	except IndexError:
		print('Вы не указали куда хотите скопировать папку или файл')
	else:
		copy_file(name, new_name)
elif command == 'help':
	print('list - список файлов и папок')
	print('create_file - создание файла')
	print('create_folder - создание папки')
	print('delete - удаление файла или папки')
	print('copy - копирование файла или папки')
elif command == 'guess':
	guess_the_number()
else:
	print('Неизвестная команда введите help чтобы увидеть доступные')
