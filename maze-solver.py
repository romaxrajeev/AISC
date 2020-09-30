maze = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

def path_search(x, y):
    #Check if outside the maze
    if maze[x][y] == 2:
        print ('found at %d,%d' % (x, y))
        return True
    #Check for wall
    elif maze[x][y] == 1:
        print ('wall at %d,%d' % (x, y))
        return False
    #Check for already visited block
    elif maze[x][y] == 3:
        print ('visited at %d,%d' % (x, y))
        return False
    #Mark current block as visited
    print ('visiting %d,%d' % (x, y)) 
    maze[x][y] = 3
 
    #Check for status of all the neighbours, if a path exists in any of the directions, starting from right in clockwise direction
    if ((x < len(maze)-1 and path_search(x+1, y)) or (y > 0 and path_search(x, y-1)) or (x > 0 and path_search(x-1, y)) or (y < len(maze)-1 and path_search(x, y+1))):
        return True

    return False

path_search(0, 0)