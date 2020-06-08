def ex1(matrix):
    m = len(matrix)
    if not m:
        return []
    n = len(matrix[0])
    if not n:
        return []

    # direction: 0: L to R, 1: U to D, 2: R to L, 3: D to U
    direction = 0

    # limit 2 sides 
    m1 = 0; m2 = m-1
    n1 = 0; n2 = n-1

    res = []
    while m1 <= m2 and n1 <= n2:
        if direction == 0:
            n_i = n1 
            while n_i <= n2:
                res.append(matrix[m1][n_i])
                n_i += 1
            m1 += 1

        elif direction == 1:
            m_i = m1 
            while m_i <= m2:
                res.append(matrix[m_i][n2])
                m_i += 1
            n2 -= 1

        elif direction == 2:
            n_i = n2
            while n_i >= n1:
                res.append(matrix[m2][n_i])
                n_i -= 1
            m2 -= 1

        elif direction == 3:
            m_i = m2
            while m_i >= m1:
                res.append(matrix[m_i][n1])
                m_i -= 1
            n1 += 1

        direction = (direction + 1) % 4

    return res

# res = ex([
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ])
# print(res)
