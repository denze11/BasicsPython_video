friends = ['Max', 'Leo', 'Kate']
print(friends)
print(type(friends))
friend = friends[0]
print(friend)
print(type(friend))

# как добавить возраст друга?
friend = {
    'name': 'Max',
    'age': 23
}

print(friend)
print(type(friend))

print(friend['age'])

friend['has_car'] = True

print(friend)

friend['has_car'] = False

print(friend)

del friend['age']

print(friend)

if 'age' in friend:
    print('Есть возраст')

if 'has_car' in friend:
    print('Есть машина')
