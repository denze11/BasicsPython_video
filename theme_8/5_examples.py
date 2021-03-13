# Функция простой разделитель

def get_sep(sep, sep_len):
	return sep * sep_len


# меняем знак разделителя
print(get_sep('*', 100))
print(get_sep('-', 100))

# меняем знак и длину разделителя
print(get_sep('-', 50))

# используем разделитель в тексте
sep = get_sep('-', 50)
text = 'Hello {} Func {}' .format(sep, sep)

print(text)
