#Finding shortest path in 2D matrix using Breadth First Search.
def findingShortestPath(matrix):
  pass

#Finding a shotest path 1's to end point 9 with out 0's
def findShortestPath(numRows, numCols, matrix):
    
    startingRow, startingCol = [0,0] #Initial starting position
    rowQueue, colQueue = [[],[]] #Intialing two queues with positons
    moveCount = 0
    nodesLeftInLayer = 1
    nodesInNextLayer = 0
    reachedEnd = False
    visited = [[False for x in row ] for row in matrix]
    
    rowQueue.append(startingRow)
    colQueue.append(startingCol)
    visited[startingRow][startingCol] = True
    while len(rowQueue) > 0: #OR len(cq) > 0
        r = rowQueue.pop(0)
        c = colQueue.pop(0)
        if matrix[r][c] == 9:
            reachedEnd = True
            break
        _,_, nodesInNextLayer = explore_neighbours(r,c,visited,matrix,rowQueue,colQueue,nodesInNextLayer)
        nodesLeftInLayer  -= 1
        print("Node Left in Layer:",nodesLeftInLayer)
        if nodesLeftInLayer == 0:
            nodesLeftInLayer = nodesInNextLayer
            nodesInNextLayer = 0
            moveCount += 1
            print("Nodes left in layer: ",nodesLeftInLayer)
            print("Move Count Numer: ",moveCount)
    if reachedEnd:
        return moveCount
    return -1

def explore_neighbours(r,c,visited,matrix,rowQueue,colQueue,nodesInNextLayer):
    R = 4
    C = 4
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    for i in range(0,4):
        rr = r + dr[i]
        cc = c + dc[i]
        #Skip out of matrix locations
        if rr < 0 or cc < 0: 
            continue
        if rr >= R or cc >= C:
            continue 
        #Skip visited locations or blaocked cells
        if visited[rr][cc]:
            continue
        if matrix[rr][cc] == 0:
            continue
    
        rowQueue.append(rr)
        colQueue.append(cc)
        visited[rr][cc] = True
        nodesInNextLayer += 1
        print("Row Queue",rowQueue)
        print("Col Queue",colQueue)
        print("Nodes in next Layer:",nodesInNextLayer)
    return rowQueue,colQueue, nodesInNextLayer

    
    #########################
    #for row in visited:
        #print(row)
    
    
def displayMatrix(matrix):
    for row in matrix:
        print(row)
                
matrix = [[1, 1, 1, 1],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [1, 1, 9, 1]]

findShortestPath(4,4,matrix)
displayMatrix(matrix)
