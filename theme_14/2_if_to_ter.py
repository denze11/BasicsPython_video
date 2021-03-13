# слово -> СлОвО

word = 'привет'

result = []

for i in range(len(word)):
	letter = word[i]
	letter = letter.lower() if i % 2 != 0 else letter.upper()
	result.append(letter)

result = ''.join(result)
print(result)
