# coding=utf-8
import io

is_test = False
if is_test:
    filenames = ('testInput.txt', 'testOutput.txt')
else:
    filenames = ('submitInput.txt', 'submitOutput.txt')

fin = io.open(filenames[0], mode='r', encoding='utf-16')
fout = open(filenames[1], 'w')

numcases = fin.readline()
i = 0
for line in fin:
    try:
        normalized_line = int(line)
        value = "%x" % int(normalized_line)
        error = False
    except ValueError:
        error = True

    if not error:
        fout.write('Case #{}: {}\n'.format(i + 1, value))
    else:
        fout.write('Case #{}: {}\n'.format(i + 1, 'N/A'))

    i += 1

fin.close()
fout.close()
