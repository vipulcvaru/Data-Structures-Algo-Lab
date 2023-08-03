# Function to display the transpose of a matrix
def display_transpose(matrix):
    # Get the number of rows and columns of the input matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a new matrix to store the transpose
    transpose_matrix = [[0 for i in range(rows)] for j in range(cols)]

    # Compute the transpose by swapping rows and columns
    for i in range(rows):
        for j in range(cols):
            transpose_matrix[j][i] = matrix[i][j]

    # Print the transpose matrix
    print("Transpose matrix =")
    for i in range(cols):
        for j in range(rows):
            print(format(transpose_matrix[i][j], "<5"), end=" ")
        print()

# Get the dimensions of the matrices from the user
row1 = int(input("Enter number of rows in matrix 1: "))
col2 = int(input("Enter number of columns in matrix 2: "))
row_col = int(input("Enter the column number of matrix1 / row number of matrix2: "))

# Prompt the user to enter elements for matrix 1 and create the matrix using nested list comprehension
print("Enter elements for matrix 1:")
matrix1 = [[float(input()) for i in range(row_col)] for j in range(row1)]

# Print matrix 1
print("MATRIX 1 =")
for i in range(row1):
    for j in range(row_col):
        print(format(matrix1[i][j], "<5"), end=" ")
    print()

# Prompt the user to enter elements for matrix 2 and create the matrix using nested list comprehension
print("Enter elements for matrix 2:")
matrix2 = [[float(input()) for i in range(col2)] for j in range(row_col)]

# Print matrix 2
print("MATRIX 2 =")
for i in range(row_col):
    for j in range(col2):
        print(format(matrix2[i][j], "<5"), end=" ")
    print()

# Initialize the result matrix with zeros, with dimensions (row1, col2)
result = [[0 for i in range(col2)] for j in range(row1)]

# Perform matrix multiplication using nested loops
for i in range(row1):  # Iterate over rows of matrix 1
    for j in range(col2):  # Iterate over columns of matrix 2
        for k in range(row_col):  # Iterate over the common dimension (columns of matrix 1 / rows of matrix 2)
            # Calculate the product and update the result matrix
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

# Print the resulting product matrix
print("Product matrix =")
for i in range(row1):
    for j in range(col2):
        print(format(result[i][j], "<5"), end=" ")
    print()

# Display the transpose of matrix 1 using the custom function
display_transpose(matrix1)
