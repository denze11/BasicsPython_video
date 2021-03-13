# Мы можем импортировать
# import math

# Но не можем импортировать наш модуль например С:
# import mymodule

# Как питон находит модуль
import sys


print(sys.path)
print(type(sys.path))

for p in sys.path:
	print(p)

sys.path.append('/home/denze1')
import mymodule
