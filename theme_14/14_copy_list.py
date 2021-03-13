a = [1, 2, 3]
# копия с помощью среза
b = a[:]
b[1] = 200
# список а не изменился
print(a)

# копия с помощью метода copy
b = a.copy()

b[1] = 200
# список а не изменился
print(a)

# Эти способ бы не будут работать если есть вложенные списки
a = [1, 2, [1, 2]]

b = a[:]

b[2][1] = 200
# список а сного меняется
print(a)

b = a.copy()

b[2][1] = 200
# список а снова меняется
print(a)
