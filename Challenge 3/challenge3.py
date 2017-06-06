# coding=utf-8

"""
CHALLENGE 3 - Board games
You can't lie to us, we know you love board games... you absolutely love them, and we also know that you are tired of
the typical point counting method.

We need a cool system for counting points for our brand new board game, and we think we could use cards to do it. For
example, a score of 10 could be represented with the set of cards 7 and 3. But those fancy printed cards don't come
cheap and that's why we need you!

We want to know how many cards we need to print, given a maximum possible score. We don't want our board game to have
repeated cards, so you need to tell us the size of the smallest set of cards that, for any number from 1 to P, we can
find a subset of those cards whose sum equals that number, being P the maximum score of the game.


INPUT
The first line will contain an integer C, the number of cases for our problem.
Each case consists of a line with the integer P, the maximum points you need to be able to count.


OUTPUT
For each case, a line starting with "Case #x: " followed by the size of the minimum set of cards needed for the score P.
Examples

Case 1:
1

Case 2:
6

Case 3:
3

In Case 1, we need a card with 1.
In Case 2, we can count up to 6 with only 3 cards, for example 1, 2 and 3.
In Case 3, we need the cards 1 and 2.


LIMITS
    1 ≤ C ≤ 104
    1 ≤ P ≤ 109


SAMPLE INPUT
3
1
6
3


SAMPLE OUTPUT
Case #1: 1
Case #2: 3
Case #3: 2
"""


import math

fin = open('submitInput.txt')
fout = open('submitOutput.txt', 'w')

lines = fin.readlines()
for i in range(1, int(lines[0]) + 1):

    line = lines[i]
    n = int(line)

    """
    This problem is easier than it seems. We just have to take into account that being able to use each number just once
    is what happens when you represent numbers in binary: you can choose to use or not to use each bit, but you can't 
    repeat them. 

    Therefore, to know the minimum amount of cards necessary to represent all the numbers up to a certain one, we just
    need to know the amount of binary digits necessary to represent it
    """
    min_digits = int(math.ceil(math.log(n, 2)))

    fout.write('Case #{}: {}\n'.format(i, int(min_digits)))

fin.close()
fout.close()