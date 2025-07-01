def transpose_matrix(matrix):

    res = []
    for i in range(len(matrix[0])):
        temp = []
        for j in range(len(matrix)):
            temp.append(matrix[j][i])
        res.append(temp)
    return res