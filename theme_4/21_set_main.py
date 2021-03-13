# Семейная пара собирается в отпуск
# каждый из супругов собирает в поездку вещи
# Макс взял эти вещи:
max_things = {'Телефон', 'Бритва', 'Рубашка', 'Шорты'}
# Kate взяла эти вещи:
kate_things = {'Телефон', 'Шорты', 'Зонтик', 'Помада'}

# какие вещи взяли супруги?
print(max_things | kate_things)

# Найти вещи которые повторяются.
print(max_things & kate_things)

# Какие вещи не взял Max но взяла Kate?
print(max_things - kate_things)

# Какие вещи не взяла Kate но взял Max?
print(kate_things - max_things)
