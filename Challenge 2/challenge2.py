fin = open('submitInput.txt')
fout = open('submitOutput.txt', 'w')

lines = fin.readlines()
cases = int(lines[0])
for i in range(1, cases+1):
    fout.write('Case #{}:'.format(i))

    rolls = [int(roll) for roll in lines[2*i].split(" ")]

    score = 0

    j = 0
    num_rolls = 0
    while True:

        if rolls[j] == 10:
            score = score + rolls[j] + rolls[j+1] + rolls[j+2]
            j += 1
            num_rolls += 1

        elif (rolls[j] + rolls[j+1] == 10):
            score = score + rolls[j] + rolls[j+1] + rolls[j+2]
            j += 2
            num_rolls += 1

        else:
            score = score +  rolls[j] + rolls[j+1]
            j += 2
            num_rolls += 1

        fout.write(' {}'.format(score))

        if j >= len(rolls) or num_rolls == 10:
            break


    fout.write('\n')

fin.close()
fout.close()