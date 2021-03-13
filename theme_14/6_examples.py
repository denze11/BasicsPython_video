# 1. Создать список из случайных чисел от 1 до 100
import random


numbers = [random.randint(1, 100) for i in range(10)]
print(numbers)

# 2. Создать список квадратов чисел
numbers = [1, 2, 3, -4]

numbers = [number**2 for number in numbers]
print(numbers)

# 3. Создать список имен на буква А
names = ['Руслан', 'Дмитрий', 'Алексей', 'Андрей']

names = [name for name in names if name.startswith('Х')]
print(names)
