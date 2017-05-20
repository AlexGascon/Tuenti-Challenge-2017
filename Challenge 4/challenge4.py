def check_if_triangle(a, b, c):
    if (a + b) > c and (a + c) > b and (b + c) > a:
        return True

def min_perimeter(perimeters):
    if perimeters:
        if len(perimeters) > 1:
            return min(perimeters)
        else:
            return perimeters[0]
    else:
        return None

def check_triangles(sides):
    perimeters = []
    for i in range(0, len(sides)):
        for j in range(i+1, len(sides)-1):
            a, b, c = sides[i], sides[j], sides[j+1]
            if check_if_triangle(a, b, c):
                perimeter = a + b + c
                perimeters.append(perimeter)
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