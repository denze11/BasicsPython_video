player_name = input('Введте имя игрока: ')
player = {
	'name': player_name,
	'health': 100,
	'damage': 50,
	'armor': 1.2
}


enemy_name = input('Введите имя врана: ')
enemy = {
	'name': enemy_name,
	'health': 100,
	'damage': 50,
	'armor': 1
}


def get_damage(damage, armor):
	return damage / armor


def attack(unit, target):
	damage = get_damage(unit['damage'], target['armor'])
	target['health'] -= damage


attack(enemy, player)
print(f'{enemy["name"]} ударил {player["name"]} и у {player["name"]} осталось {player["health"]}HP')
