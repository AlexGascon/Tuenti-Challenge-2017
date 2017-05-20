import math

fin = open('submitInput.txt')
fout = open('submitOutput.txt', 'w')

lines = fin.readlines()
for i in range(1, int(lines[0]) + 1):
    line = lines[i]
    n = int(line)

    min_digits = int(math.ceil(math.log(n, 2)))

    fout.write('Case #{}: {}\n'.format(i, int(min_digits)))

fin.close()
fout.close()