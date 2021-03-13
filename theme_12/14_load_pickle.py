import pickle


# открываем файл
with open('theme_12/person.dat', 'rb') as f:
	#сразу читаем объект из файла с помощью pickle
	person = pickle.load(f)

print(person)
