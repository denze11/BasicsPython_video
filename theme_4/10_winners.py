# Пользователь вводит кол-во участников соревнований по python
# Пользователь вводит участников и их места в зависимости от кол-ва
# 1. Вывод имени участников по алфавиту
# 2. Получить 3-х победителей и поздравить их
# 3. Победители: ... Поздравляем!

print('СОРЕВНОВАНИЯ ПО PYTHON')
number_of_participants = int(input('Введите количество участников: '))
number = 1
participants = []
while True:
    if number <= number_of_participants:
        participant = input('Кто занял {} место: ' .format(number_of_participants))
        participants.append(participant)
        number_of_participants -= 1
    else:
        break
print('В соревнованиях участвовали: {}' .format(sorted(participants)))
participants.reverse()
top3 = participants[:3]
print('Победители: {}, {}, {}.' .format(top3[0], top3[1], top3[2]))
