def matrix():
    dimention = int(input('Please introduced the dimention: '))
    
    matrix = []

    for i in range(dimention):
        matrix.append([0]*dimention)

    n = 0
    for i in matrix:
        matrix[n][n] = 1
        print(matrix[n])
        n += 1

matrix()