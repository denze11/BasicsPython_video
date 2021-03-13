f = open('theme_12/first.txt', 'r')

for line in f:
	print(line.replace('\n', ''))

f.close()

with open('theme_12/first.txt', 'r') as f:
	for line in f:
		print(line.replace('\n', ''))

print('end')
