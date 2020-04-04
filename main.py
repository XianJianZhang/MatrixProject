import matrix

def main():
  print("Hello, welcome to matrix addition and subtraction!")
  userChoice = choice()
  matrix_operation(userChoice, organize_input(userChoice))

#Returns choice of operation by the user
def choice():
  choice_op = input("Enter your choice of operation: mult, add, sub: ")
  while choice_op != "sub" and choice_op != "add" and choice_op != "mult":
    choice_op = input("Enter your choice of operation: mult, add, sub: ")
  return choice_op

#Performs one of the 3 matrix operations, given two matrices
def matrix_operation(userChoice, matricesInfo):
  if userChoice == "add":
    matrix1 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[2])
    matrix2 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[3])
    print(str(matrix1) +
          " plus "+ str(matrix2) + " is " + str(matrix.Matrix.addMatrix(matrix1, matrix2)))
  elif userChoice == "sub":
    matrix1 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[2])
    matrix2 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[3])
    print(str(matrix1) +
          " subtracted by " + str(matrix2) + " is " + str(matrix.Matrix.subMatrix(matrix1, matrix2)))
  else:
    matrix1 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[2])
    matrix2 = matrix.Matrix(matricesInfo[1], matricesInfo[4], matricesInfo[3])
    print(str(matrix1) +
          " multiplied by " + str(matrix2) + " is " + str(matrix.Matrix.multMatrix(matrix1, matrix2)))

def organize_input(choice):
  input1 = []
  input2 = []
  row = int(input("Enter row for the two matrices: "))
  col = int(input("Enter col for the two matrices: "))
  if choice != "mult":
    col2 = col
  elif choice == "mult":
    col2 = int(input("Enter number of col for the second matrices (row must be same, so we won't ask you that: "))
  for x in range(row):
    for y in range(col):
      userInput = int(input("Enter one number: "))
      input1.append(userInput)
  for x in range(row):
    for y in range(col2):
      userInput = int(input("Enter one number for the second matrix: "))
      input2.append(userInput)
  return (row, col,input1, input2, col2)
main()
