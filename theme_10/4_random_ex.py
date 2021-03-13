from random import randint, choice, sample, shuffle


# 1. загадать случайное число от 0 до 100
print(randint(0, 100))

# 2. выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))

# 3. выбрать 3-х победителей лотереи из списка players
print(sample(players, 3))

# 4. перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)
