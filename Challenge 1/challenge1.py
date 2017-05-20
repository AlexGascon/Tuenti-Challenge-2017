import math

fin = open('submitInput.txt')
fout = open('submitOutput.txt', 'w')

lines = fin.readlines()
cases = int(lines[0])

for i in range(1, cases+1):
	slices = lines[2*i]
	total_slices = sum([int(pizza_slices) for pizza_slices in slices.split(" ")])
	pizzas = int(math.ceil(total_slices/8.0))

	fout.write('Case #{}: {}\n'.format(i, pizzas))


