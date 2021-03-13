'''
В папке с модулем создать 5 подпамок названия которых состоят
из платформы на которой запущен интерпритатор и порядкового номера начиная с 1:
linux_1, linux_2, ... Платформа может быть другой.
'''

import sys, os

name = sys.platform

for i in range(1, 6):
	new_path = os.path.join(os.getcwd(), f'{name}_{i}')
	os.mkdir(new_path)
