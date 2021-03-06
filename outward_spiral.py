from itertools import cycle

def out_spiral(n):
    '''
    create a n*n matrix with outward clockwise spiral of integers starting at the center with 1 up to n*n
    '''
    if n%2==0:
        return 'ERROR: n must be odd'
    global x, y, direction, matrix
    matrix = [['x']* n for row in range(n)]
    # center of spiral, n must be odd
    x,y  = n//2, n//2
    matrix[x][y] = 1
    direction = (-1,0)  # north
    headings = cycle([(0,1),(1,0),(0,-1),(-1,0)]) # east,south,west,north
    
    def move(n):
        global x,y,matrix
        x += direction[0]
        y += direction[1]
        matrix[x][y] = n
             
    def turn_clockwise():
        global direction
        direction = next(headings)
        
    i = 2
    for j in range(n):
        for k in range(2):
            for l in range(j+1):
                if i > n*n:
                    break
                move(i)
                i += 1
            turn_clockwise()
    return matrix
