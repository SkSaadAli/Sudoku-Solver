def Empty(grid):
    for i  in range(len(grid)):
        for j  in range(len(grid[0])):
            if(grid[i][j]==0):
                return (i,j)
    return None
def valid(grid, num ,pos):
    #checking the box
    box_x=pos[1]//3
    box_y=pos[0]//3
    for i in range(box_y*3,(box_y*3)+3):
        for j in range(box_x*3,(box_x*3)+3):
            if grid[i][j]==num and (i,j)!= pos:
                return False
    #checking rows
    for i in range(len(grid[0])):
        if grid[pos[0]][i]== num and pos[1]!=i:
            return False
    for i in range(len(grid[0])):
        if grid[i][pos[1]]== num and pos[0]!=i:
            return False
    return True
def suduko_solver(grid):
        pos= Empty(grid)
        if not pos:
            return True
        else:
            row,col=pos

        for k in range(1,10):
                if valid(grid,k,pos):
                    grid[row][col]=k
                    if suduko_solver(grid):
                        return True
                    grid[row][col]=0
        return False

def print_grid(grid):
    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")


grid=[[5,3,0,0,7,0,0,0,0],
      [6,0,0,1,9,5,0,0,0],
      [0,9,8,0,0,0,0,6,0],
      [8,0,0,0,6,0,0,0,3],
      [4,0,0,8,0,3,0,0,1],
      [7,0,0,0,2,0,0,0,6],
      [0,6,0,0,0,0,2,8,0],
      [0,0,0,4,1,9,0,0,5],
      [0,0,0,0,8,0,0,7,9]]
print_grid(grid)
print('  \n')
# sudokosolver(*grid)
suduko_solver(grid)
print_grid(grid)