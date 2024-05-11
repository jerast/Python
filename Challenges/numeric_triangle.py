
# method 1 - Counter variable method
def triangle(levels):
    triangle = int( (levels * (levels + 1))/2 )
    numList = list(range(1, triangle + 1))
    counter = 0
    for lev in range(levels + 1):
        response = ""
        for i in range(lev):
            response = f'{response} {str(numList[counter])}'
            counter = counter + 1
        print(response.lstrip())
    print(numList)
triangle(5)


# method 2 - Iterable matrix method
def triangle_2(levels):
    array_a = []
    for lev in range(levels):
        array_b = []
        for num in range( int(lev*(lev+1)/2), int((lev*(lev+1)/2)) + lev + 1):
            array_b.append(num + 1)
        array_a.append(array_b)
    for row in array_a:
        print(*row, sep=' ')
    print(array_a)
triangle_2(5)