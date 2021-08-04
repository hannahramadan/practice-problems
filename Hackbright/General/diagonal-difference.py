def diagonalDifference(matrix):
    sum1 = sum2 = 0
    
    for i in range(len(matrix)):
        sum1 += matrix[i][i]
        sum2 += matrix[i][-1-i]
    
    return abs(sum1-sum2)
    
