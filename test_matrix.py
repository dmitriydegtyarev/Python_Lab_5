n = 7

matrix = [[0] * n for zero in range(n)]

for i in range(n):
    # print (i)
    for j in range(n - i):
        # print(j)
        matrix[i][j] = i + j + 1
        print (matrix)