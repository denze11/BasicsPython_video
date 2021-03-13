player_name = input('Введте имя игрока: ')
player = {
	'name': player_name,
	'health': 100,
	'damage': 50
}


enemy_name = input('Введите имя врана: ')
enemy = {
	'name': enemy_name,
	'health': 100,
	'damage': 50
}


def attack(unit, target):
	target['health'] -= unit['damage']


attack(player, enemy)
print(
	f'{player["name"]} ударил {enemy["name"]} и у {enemy["name"]} осталось {enemy["health"]}HP')
