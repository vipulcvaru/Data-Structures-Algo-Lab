# Take user input for the number of rows and columns in the matrices
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

# Matrix 1 input
print("Enter elements for matrix 1:")
matrix1 = [[float(input()) for i in range(column)] for j in range(row)]

# Print Matrix 1
print("MATRIX 1 =")
for i in range(row):
    for j in range(column):
        print(format(matrix1[i][j], "<3"), end=" ")
    print()

# Matrix 2 input
print("Enter elements for matrix 2:")
matrix2 = [[float(input()) for i in range(column)] for j in range(row)]

# Print Matrix 2
print("MATRIX 2 =")
for i in range(row):
    for j in range(column):
        print(format(matrix2[i][j], "<3"), end=" ")
    print()

# Initialize a matrix to store the result of addition
result = [[0 for i in range(column)] for j in range(row)]

# Perform matrix addition
for i in range(row):
    for j in range(column):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

# Print the addition result
print("Addition matrix =")
for i in range(row):
    for j in range(column):
        print(result[i][j], end=" ")
    print()

# Initialize a matrix to store the result of subtraction
result1 = [[0 for i in range(column)] for j in range(row)]

# Perform matrix subtraction
for i in range(row):
    for j in range(column):
        result1[i][j] = matrix1[i][j] - matrix2[i][j]

# Print the subtraction result
print("Subtraction matrix =")
for i in range(row):
    for j in range(column):
        print(result1[i][j], end=" ")
    print()
