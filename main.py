###  Maze Traversal Using Recursion  ###

#This is the maze where:
#'1' represents a WALL
#'0' represents a PATH (no obstacle)
#'S' represents STARTING POSITION
#'E' represents END POSITION
maze = [['1', '1', 'E', '0', '1', '0', '0', '0'],
        ['1', '0', '1', '0', '0', '0', '1', '0'],
        ['0', '1', '0', '1', '1', '0', '0', '0'],
        ['1', '1', '1', '0', '1', '0', '0', '0'],
        ['1', '0', '0', '0', '0', '0', '1', '0'],
        ['1', '1', '1', '1', '1', '1', '0', '0'],
        ['1', '1', '0', '0', '0', 'S', '0', '1'],
        ['0', '0', '0', '1', '1', '1', '1', '1']]

#Function to print the maze in terminal
def drawMaze(maze):
     for row, i in enumerate(maze):
          for col, j in enumerate(i):
               if col == len(i) - 1:
                    print(j)
               else:
                    print (j, end = ' ')
     print ('\n')

drawMaze(maze)

visited = [] #List of paths already visited
path = [] #Keep note of paths that should be taken to reach E

#Main function which takes as parameter the current position (row and column)
def findPath(row, col):

     found = False

     #Check if current position is within the limits of the dimension of the maze or if current position is not on an obstacle (1)
     if row >= len(maze) or row < 0 or col >= len(maze[0]) or col < 0 or maze[row][col] == '1':
          return False

     if maze[row][col] == '0' or maze[row][col] == 'S':
          path.append([row, col]) #Legal position/path

     if maze[row][col] == 'E':
          path.append([row, col])
          return True #End position has been found

     #Verify that the current position has not already been visited -- important because otherwise we would be faced with an infinite loop
     if [row, col] not in visited:
          visited.append([row, col])
          #Check if there are possible paths to the top, bottom, right or left
          found = findPath(row - 1, col) or findPath(row + 1, col) or findPath(row, col + 1) or findPath(row, col - 1)
          
     if found:
          return True

     #if we have found no possible position that we can go, then the current position cannot lead to the end point
     if len(path) > 0:
          path.pop() #remove the current position from the list
     return False


#Find the starting position
for row, i in enumerate (maze):
          for col, j in enumerate (i):
               if j == 'S':
                    start = [row, col]

findPath(start[0], start[1])

for i in path:
     maze[i[0]][i[1]] = 'W' #Mark each of the positions to be taken to get to the end with a 'W'

drawMaze(maze)
