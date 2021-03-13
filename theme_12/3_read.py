# Открываем файл на чтение - файл не существует
f = open('theme_12/first.txt', 'r')

#print(f.read())

'''for line in f:
	print(line.replace('\n', ''))'''

print(f.readlines())
