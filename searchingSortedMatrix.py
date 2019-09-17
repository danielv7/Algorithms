#Searching a sorted 2D matrix

#Every row is sorted from left to right in increasing order, 
#with the first integer of each row being greater than the last integer of the previous row's last column

#For example given a matrix and traget value return True or False if target value is present in matrix:
#matrix = [[1, 2, 3, 4],
#          [5, 6, 7, 8],
#          [9, 10, 11, 12]
#          [13, 14, 15, 16]]
#Target Value: 12
#Function should return true because 12 is present in matrix


#Time Complixity O(log(n) Space O(1)
def searchSortedMatrix(matrix, targetValue):
  #Inital check for empty matrix
  if len(matrix) == 0:
    return False
  totalRows = len(matrix)
  totalCols = len(matrix[0])
  
  leftPoint = 0
  rightPoint = totalRows * TotalCols - 1
  while left <= right:
    middlePoint = (leftPoint + rightPoint) // 2
    middleValue = matix[middlPoint//totalCols][middlePoint%totalCols]
    if middleValue == targetValue:
      return True
    elif middleValue < targetValue:
      left = middlePoint + 1
    else:
      right = middlePoint - 1
  return False  
  
