person = {'name': 'Max', 'phones': [123, 345]}

# откроем файл
with open('theme_12/person.dat', 'wb') as f:
	# например запишем объект в файл построчно
	# сначало возьмем имя
	name = person['name']
	# добавим перенос строки переведем в байты и запишем
	f.write(f'{name}\n' .encode('utf-8'))
	# получим телефон
	phones = person['phones']
	# запишим 1 телефон в новую строку
	for phone in phones:
		f.write(f'{phone}\n' .encode('utf-8'))

print('Объект записан')
