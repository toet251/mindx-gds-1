def ex1(matrix):
    n = len(matrix)
    if n == 0:
        return matrix

    min_n = 0
    while min_n <= n-1-min_n:
        max_n = n-1-min_n
        
        for i in range(min_n, max_n):
            temp = matrix[min_n][i]
            matrix[min_n][i] = matrix[n-1-i][min_n]
            matrix[n-1-i][min_n] = matrix[max_n][n-1-i]
            matrix[max_n][n-1-i] = matrix[i][max_n]
            matrix[i][max_n] = temp 
        min_n += 1

    return matrix
