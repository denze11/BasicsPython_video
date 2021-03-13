'''3: Создайте модуль main.py. Из модулей реализованных в заданиях 1 и 2 сделайте импорт в main.py всех функций. Вызовите каждую функцию в main.py и проверьте что все работает как надо.'''

from module_1 import new_folder, del_folder
from module_2 import my_random


new_folder()
del_folder()
my_random([1, 2, 3, 4])
