pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# класический способ
result = {}
for pair in pairs:
	key = pair[0]
	val = pair[1]
	result[key] = val

print(result)

# через генератор словоря
result = {pair[0]: pair[1] for pair in pairs}
print(result)
