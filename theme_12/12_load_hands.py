# читам объект из файла

# откроем файл
with open('theme_12/person.dat', 'rb') as f:
	# теперь нам надо знать как мы записываем объект
	# прочитаем файл в список
	result = f.readlines()

# теперь воссоздаем исходный объект
person ={}
# первый элимент этого имени
person['name'] = result[0].decode('utf-8').replace('\n', '')
# далее идут телефоны
phones = []
for bphone in result[1:]:
	phones.append(bphone.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# полули исходный объект. Это было достаточно тяжело. А теперь он немного изменится?
print(person)
