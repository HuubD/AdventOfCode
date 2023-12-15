import re

# Check if the position is valid
def isValidPos(i, j, n, m):
    if (i < 0 or j < 0 or i > n - 1 or j > m - 1):
        return 0
    return 1

# Get the adjacent positions of the current position
def getAdjacent(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])

    # Boolean for checking if the current position is a number so the full number doesn't get duplicated
    isNumber = 0

    v = []

    if (isValidPos(i - 1, j - 1, n, m)):
        if(matrix[i - 1][j - 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i - 1, j - 1, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i - 1, j, n, m)):
        if(matrix[i - 1][j].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i - 1, j, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i - 1, j + 1, n, m)):
        if(matrix[i - 1][j + 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i - 1, j + 1, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i, j - 1, n, m)):
        if(matrix[i][j - 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i, j - 1, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i, j + 1, n, m)):
        if(matrix[i][j + 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i, j + 1, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i + 1, j - 1, n, m)):
        if(matrix[i + 1][j - 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i + 1, j - 1, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i + 1, j, n, m)):
        if(matrix[i + 1][j].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i + 1, j, n, m))
            isNumber = 1
        else:
            isNumber = 0
    if (isValidPos(i + 1, j + 1, n, m)):
        if(matrix[i + 1][j + 1].isdigit() and isNumber == 0):
            v.append(getNumber(matrix, i + 1, j + 1, n, m))
            isNumber = 1
        else:
            isNumber = 0

    return v

# Get the full number from the adjacent positions
def getNumber(matrix, i, j, n, m):
    v = []

    if (isValidPos(i, j - 1, n, m)):
        if not (matrix[i][j - 1].isdigit()):
            j += 1
        elif not (matrix[i][j + 1].isdigit()):
            j -= 1
            

    for x in range(j - 2, j + 2):
        if (isValidPos(i, x, n, m)):
            if (matrix[i][x].isdigit()):
                v.append(matrix[i][x])

    return v
    

matrix = []
specialChars = ['@', '_', '!', '#', '$', '%', '^', '&', '*', '(', ')', '<', '>', '?', '/', '|', '}', '{', '~', ':', '+', '-', '=']

result = 0

# Open file and and add each line to a matrix
with open('input.txt') as f:
    for line in f:
        lineArray = []
        for char in line:
            lineArray.append(char)

        matrix.append(lineArray)
        
    for row_index, row in enumerate(matrix):
        for char_index, char in enumerate(row):
            if any(char in specialChars for char in char):
                numbers = getAdjacent(matrix, row_index, char_index)
                for number in numbers:
                    wholeNumber = ''.join(number)

                    result += int(wholeNumber)
                        
print(result)
                        