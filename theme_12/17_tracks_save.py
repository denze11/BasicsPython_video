import json


favorite_tracks = [
	{'name': 'Вечная Любовь', 'artist': 'Агата Кристи'},
	{'name': 'Angel', 'artist': 'Massive Attack'},
	{'name': 'Jamming', 'artist': 'Bob Marley'}
]

with open('theme_12/tracks.json', 'w', encoding='utf-8') as f:
	json.dump(favorite_tracks, f)

print('Выполнено')
