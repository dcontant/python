# Sudoku, recursion, backtacking. from YT video Computerphile

import numpy as np

def possible(row, col, n):
  # return True if n is a valid candidate for cell at grid[row][col]
  global grid
  for i in range(9):
    if grid[row][i]==n or grid[i][col]==n:
      return False
  row = (row//3)*3
  col = (col//3)*3
  for i in range(3):
    for j in range(3):
      if grid[row+i][col+j] == n:
        return False
  return True
      

def solve():
  global grid
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        for n in range(1,10):
          if possible(row, col, n):
            grid[row][col] = n
            solve()
            grid[row][col] = 0 # no possible candidate for grid[row][col]
        return
  print(np.matrix(grid))
  return
  
grid= [[0, 0, 0, 0, 0, 0, 5, 0, 0],
       [0, 7, 1, 6, 8, 0, 0, 0, 0],
       [0, 0, 0, 2, 5, 0, 8, 0, 3],
       [0, 0, 9, 0, 0, 8, 4, 0, 0],
       [0, 0, 2, 0, 1, 0, 3, 0, 0],
       [0, 8, 0, 5, 0, 0, 0, 2, 0],
       [4, 0, 5, 8, 3, 0, 0, 0, 0],
       [0, 0, 0, 4, 9, 0, 1, 3, 0],
       [0, 0, 8, 0, 0, 0, 0, 0, 0]]  
  

solve()   
