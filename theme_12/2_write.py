# Открываем файл на запись
f = open('theme_12/first.txt', 'w')

f.write('Hello\n')
f.write('World\n')

f.writelines(['Hello\n', 'Python\n'])
