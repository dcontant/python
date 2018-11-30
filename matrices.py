def rot_90_clockwise(matrix):
    return [list(row) for row in zip(*reversed(matrix))]
    
def rot_90_counterclockwise(matrix):
    return  reversed([list(row) for row in zip(*matrix)])
    
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
    
    
def neg_matrix(matrix):
    return [[-1 * col for col in row] for row in matrix]
    
    
def is_skew_symetric(matrix):
    return neg_matrix(matrix) == transpose(matrix)
    
# determinant,   from: https://stackoverflow.com/questions/3819500/code-to-solve-determinant-using-python-without-using-scipy-linalg-det    

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant
