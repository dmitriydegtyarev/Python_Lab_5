n = 7

# Заповнення матриці нулями (7 стовпців, 7 строк)
matrix = [[0] * n for zero in range(n)]

# Заповнення матриці за заданим шаблоном
for i in range(n):
    for j in range(n - i):
        matrix[i][j] = i + j + 1  # Корекція значень згідно з варіантом завдання

# Виведення матриці у форматованому вигляді
for row in matrix:
    print(" ".join(map(str, row)))