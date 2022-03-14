#Jamison Talley
#Cutter 
#Chandler
#Aaron
#3-9-22
#matrix.py

#imports necesary modules
import stdio

#defines a function that uses a list of lists to hold matrices
#that are inputed by the user using the standard input module
#the function doesn't take an input, and outputs a list of 
#two matrices defined by the user
def get_matrices():
    matrix = []
    matrices = [[],[]]
    for i2 in range(2):
        i1 = 0
        stdio.write("\nEnter the value of matrix ")
        stdio.write(i2 + 1)
        cont_val = True
        while cont_val != "no":
            matrix.append([])
            stdio.write("\nEnter integers for row ")
            stdio.writeln(i1 + 1)
            while not stdio.isEmpty():
                matrix[i1] = stdio.readAllInts()
            i1 += 1
            stdio.writeln("Would you like to add another row? (yes or no)")
            while not stdio.isEmpty():
                cont_val = stdio.readString()
        matrices[i2] = matrix
        matrix = []
    return matrices

#takes one matrix as input, and returns a rectangular
#version of that matrix by filling any spaces left 
#by the user with 0's
def matrix_cleanup(matrix):
    matrix_out = matrix
    row_lengths = []
    m = len(matrix)
    for i2 in range(m):
        row_lengths.append(len(matrix[i2]))
    n = max(row_lengths)
    for i3 in range(m):
        places_filled = n - len(matrix[i3])
        for i4 in range(places_filled):
            matrix_out[i3].append(0)
    return matrix_out

#takes two matrices as input and checks to see if
#they can be multiplied by checking if the number of 
#columns in the first matrix equals the nuber of 
#rows in the second matrix
def multiply_check(matrix_1, matrix_2):
    n_1 = len(matrix_1[0])
    m_2 = len(matrix_2)
    if n_1 == m_2:
        return True
    else:
        return False

#defines a function that mutliplies two inputed matrices
#together using the rules of matrix mutliplication,
#and returns the matrix that is their product
def multiply_matrices(matrix_1, matrix_2):
    m = len(matrix_1)
    n = len(matrix_2[0])
    n_1 = len(matrix_1[0])
    matrix_out = []
    matrix_val = 0
    for i1 in range(m):
        matrix_out.append([])
    for i2 in range(m):
        for i3 in range(n):
            for i4 in range(n_1):
                matrix_val += (matrix_1[i2][i4] * matrix_2[i4][i3])
            matrix_out[i2].append(matrix_val)
            matrix_val = 0
    return matrix_out

#defines a function that displays the matrices in a neat manner
#using the standard output module
def display_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i1 in range(m):
        stdio.write("\n")
        for i2 in range(n):
            stdio.writef("%2.0f", matrix[i1][i2])
            stdio.write("  ")
    stdio.writeln("\n")

#defines the test function that uses all of the above
#functions when called
def main():
    matrices = get_matrices()
    matrices = [matrix_cleanup(matrices[0]), matrix_cleanup(matrices[1])]
    if multiply_check(matrices[0], matrices[1]) == True:
        stdio.writeln("These two matrices multiply to: ")
        display_matrix(multiply_matrices(matrices[0], matrices[1]))
    else:
        stdio.writeln("Those matrices cannot be multiplied.")

#runs the test function if the program is the file being ran
if __name__ == "__main__":
    main()

#our prompt was:
#2.1.18
#Compose a function multiply() that takes two square matrices 
#of the same dimension as arguments and returns their product 
#(another square matrix of that same dimension). 
#Extra credit: Make your program work whenever the number of
#columns in the first matrix is equal to the number of rows in the second matrix.
