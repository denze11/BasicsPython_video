friend_name = 'Max'
friends = ['Max', 'Leo', 'Kate']
roles = ('admin', 'guest', 'user')

if 'Max' in friends:
    print('Уменя есть этот друг')

if 'M' in friend_name:
    print('Буква M есть в имени друга')

# While
i = 0
while i < len(friends):
    friend = friends[i]
    print(friend)
    i += 1

# for
for friend in friends:
    print(friend)

for letter in friend_name:
    print(letter)

for role in roles:
    print(role)

print('end')
