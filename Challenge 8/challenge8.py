# coding=utf-8
"""
CHALLENGE 8 - Uni code to rule them all

We need to process lots of data. As a big problem with data is how you recollect it, one of the most important steps is
cleaning and normalizing it.
In this case, we need to clean integers, just integers. We asked our data collectors to only use integers with decimal
notation. We thought this would give us clean data… but that’s not the case, there are invalid numbers, and a lot of
valid numbers with strange characters.
Please, help us to clean this data.


INPUT
The first line will contain an integer C, the number of cases for our problem.
Each case consists of a line with some characters. Some of them will be valid numbers. A number is valid if all its
characters are decimal digits (Nd), and there are no other characters or spaces inside the number. Only one number is
allowed per line. Spaces (Zs) are allowed at the beginning and end of each line.


OUTPUT
For each case, a line starting with "Case #x: " followed by the the number in hexadecimal format or, if the number is
not valid, the string “N/A”. Every line is followed by a new line character.


LIMITS
    0 ≤ Number ≤ 104097 - 1
    1 ≤ Number of lines ≤ 250


SAMPLE INPUT
11
12345
  12345
  12345  a
   789꧔
123 45
1234abc
٨8٩
۵ ۷
٦ମ2
O５
०５


SAMPLE OUTPUT
Case #1: 3039
Case #2: 3039
Case #3: N/A
Case #4: 1ed6
Case #5: N/A
Case #6: N/A
Case #7: 379
Case #8: N/A
Case #9: N/A
Case #10: N/A
Case #11: 5
"""

import io

is_test = False
if is_test:
    filenames = ('testInput.txt', 'testOutput.txt')
else:
    filenames = ('submitInput.txt', 'submitOutput.txt')

# The good part is that Python makes this challenge EXTREMELY easy. We just need to be careful with a few details.
# The first thing to be careful about is the encoding used when reading the input. We'll use utf-16, because using less
# bits will result in information loss
fin = io.open(filenames[0], mode='r', encoding='utf-16')
fout = open(filenames[1], 'w')

numcases = fin.readline()
i = 0
for line in fin:

    # Then, we just need to call the int() method on the read line and be prepared to catch ValueError, the exception
    # that indicates that the conversion isn't possible.
    # int() takes care by itself of choosing the correct encoding when converting, so we don't need to do worry about
    # anything else!
    try:
        normalized_line = int(line)
        value = "%x" % int(normalized_line)
        error = False
        # Small detail: if the integer is very big, Python will append an "L" at the end. We need to get rid of it
        # before printing the result in the output file
        if value[-1] == "L":
            value = value[:-1]

    except ValueError:
        error = True

    if not error:
        fout.write('Case #{}: {}\n'.format(i + 1, value))
    else:
        fout.write('Case #{}: {}\n'.format(i + 1, 'N/A'))

    i += 1

fin.close()
fout.close()
