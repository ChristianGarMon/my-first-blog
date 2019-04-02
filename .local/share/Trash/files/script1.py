def hi(name = ''):
	if name == '':
		name = 'Aanonymous'
	print('Hi ' + name + '!')

metallica = ['James', 'Lars', 'Kirk', 'Robert', 'Cliff', 'Jason', 'Dave', 'Ron']

for name in metallica:
	hi(name)
	print('Next member')