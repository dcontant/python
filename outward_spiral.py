from itertools import cycle

def out_spiral(n):
    '''
    create a n*n matrix with outward spiraling integer, clockwise, n must be odd
    '''
    if n%0:
      return 'n must be odd'
    global x,y,current, direction, headings,matrix
    matrix = [['x']* n for row in range(n)]
    # center of spiral, n must be odd
    x,y  = n//2, n//2
    matrix[x][y] = 1
    direction = (-1,0)  # north
    headings = cycle([(0,1),(1,0),(0,-1),(-1,0)])
    
    def move(num):
        global x,y,matrix
        x += direction[0]
        y += direction[1]
        try:
            matrix[x][y] = num
        except IndexError:
            print('error',x,y)
            pp(matrix)
             
    def turn_clockwise():
        global direction
        direction = next(headings)
        
    i = 2
    while True:
        for j in range(n):
            for k in range(2):
                for l in range(j+1):
                    move(i)
                    i += 1
                    if i > n*n:
                        break
                turn_clockwise()
                if i > n*n:
                    break
            if i > n*n:
                break
        if i > n*n:
            break
    return matrix
