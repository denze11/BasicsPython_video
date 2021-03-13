# набор чисел
numbers = [1, 5, 3, 5, 9, 7, 11]
# сортировка по возрастанию
print(sorted(numbers))
# сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Alex', 'Kate']
# сортировка по алфавиту
print(sorted(names))

# города и численность населения (цифры не настоящие)
cities = [('Москва', 1000), ('Лас-Вегас', 500), ('Антверпен', 2000)]
# такая сортировка сработает по алфавиту
print(sorted(cities))
# как отсортировать по численности населения?

def by_count(city):
	return city[1]

print(sorted(cities, key=by_count))

print(sorted(cities, key=lambda city: city[1]))
