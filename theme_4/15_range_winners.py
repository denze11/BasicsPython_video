winners = ['Max', 'Leo', 'Kate']

# Простой перебор
for winner in winners:
    print(winner)

# использовать range
for i in range(1, len(winners)+1):
    # print(i)
    #print(i, ':', winners[i - 1])
	print('{} : {}' .format(i, winners[i - 1]))
