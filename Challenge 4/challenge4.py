# coding=utf-8
"""
CHALLENGE 4 - Help Pythagoras Junior

Pythagoras Junior is not a great mathematician like his great great great grandfather. When he gets a list of numbers,
he finds it hard to match 3 numbers and create a triangle out of them.
You need to help Pythagoras Junior to identify which is the smallest possible triangle given a list of side lengths.
We define the smallest triangle as the one with the minimum perimeter.


INPUT
The first line will contain an integer C, the number of cases for our problem.
Each case consists of a line starting with an integer N, the number of sides, followed by N integers, each indicating
the length of a side. All the integers are separated by spaces.


OUTPUT
For each case, a line starting with "Case #x: " followed by the perimeter of the smallest triangle or, if it's not
possible to form a valid triangle, "IMPOSSIBLE". Every line is followed by a new line character.


EXAMPLES
Case 1:
6 13 9 1 13 17 6

Case 2:
7 110 40 10 1 20 60 3

In Case 1, the answer is 27, as the triangle with the smallest perimeter is (13, 13, 1).
In Case 2, the answer is IMPOSSIBLE. You cannot create a valid triangle from any three of the given numbers.


LIMITS
    3 ≤ N ≤ 105
    1 ≤ Lengths ≤ 232


SAMPLE INPUT
2
6 13 9 1 13 17 6
7 110 40 10 1 20 60 3


SAMPLE OUTPUT
Case #1: 27
Case #2: IMPOSSIBLE
"""

def check_if_triangle(a, b, c):
    """
    Checks if we can create a triangle with the given sides.

    The parameters represent the length of each of the sizes of the hypothetical triangle.
    Returns True or False depending on if we can create a triangle or not.

    To check if we can create a triangle with the given sides, we need that the sum of any pair of sides is greater than
    the remaining one.
    """
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True
    else:
        return False

def min_perimeter(perimeters):
    """
    Gets a list of numbers and returns the smallest one.

    We use it to find the minimum perimeter in a list of possible triangle perimeters
    """
    if perimeters:
        if len(perimeters) > 1:
            return min(perimeters)
        else:
            # We can't execute min in a one-element array
            return perimeters[0]
    else:
        return None

def check_triangles(sides):
    """
    Gets a *sorted* list of sides and returns the perimeter of the smallest triangle we can form with them.
    """
    perimeters = []
    for i in range(0, len(sides)):
        for j in range(i+1, len(sides)-1):
            # A VERY important part of the calculations is that the longest side must be the sucessor of the second
            # longest, as we're searching for the smallest triangle. If we needed a longest side, then we wouldn't have
            # the smallest possible triangle.
            # This assumption allows us to reduce the problem complexity from O(^3) to O(n^2)
            a, b, c = sides[i], sides[j], sides[j+1]
            if check_if_triangle(a, b, c):
                perimeter = a + b + c
                perimeters.append(perimeter)
                # As the sides array is sorted, if we keep iterating we'll only get bigger triangles. Therefore, we can
                # advance to the next iteration of the outer loop.
                break

    return min_perimeter(perimeters)


#filenames = ('testInput.txt', 'testOutput.txt')
filenames = ('submitInput.txt', 'submitOutput.txt')
fin = open(filenames[0])
fout = open(filenames[1], 'w')


case = 1
lines = fin.readlines()[1:]
for nums in lines:
    sides = [int(num) for num in nums.split(" ")[1:]]

    sides.sort()
    perimeter = check_triangles(sides)

    if perimeter:
        fout.write('Case #{}: {}\n'.format(case, perimeter))
    else:
        fout.write('Case #{}: {}\n'.format(case, 'IMPOSSIBLE'))

    case += 1


fin.close()
fout.close()