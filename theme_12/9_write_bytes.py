# открываем файл для записи байтов
with open('theme_12/bytes.txt', 'wb') as f:
	# пишим строку байт
	f.write(b'Hello bytes')

# читаем как текст
with open('theme_12/bytes.txt', 'r', encoding='ascii') as f:
	# пишем строку байт
	print(f.read())

# открываем файл для записи байтов
with open('theme_12/bytes.txt', 'wb') as f:
	# пишем строку байт
	str = 'Привет мир'
	f.write(str.encode('utf-8'))

# читаем как текст с кодировкой utf-8
with open('theme_12/bytes.txt', 'r', encoding='utf-8') as f:
	# пишем строку байта
	print(f.read())
