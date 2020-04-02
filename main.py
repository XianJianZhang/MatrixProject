import matrix

def main():
  print("Hello, welcome to matrix addition and subtraction!")
  matrix_operation(choice(), organize_input())

#Returns choice of operation by the user
def choice():
  choice_op = input("Enter your choice of operation: mult, add, sub: ")
  while choice_op != "sub" and choice_op != "add" and choice_op != "mult":
    choice_op = input("Enter your choice of operation: mult, add, sub: ")
  return choice_op

#Performs one of the 3 matrix operations, given two matrices
def matrix_operation(userChoice, matricesInfo):
  matrix1 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[2])
  matrix2 = matrix.Matrix(matricesInfo[0], matricesInfo[1], matricesInfo[3])
  if userChoice == "add":
    print(str(matrix1.getMatrix()) +
          " plus "+ str(matrix2.getMatrix()) + " is " + str(matrix.Matrix.addMatrix(matrix1, matrix2)))
  elif userChoice == "sub":
    print(str(matrix1.getMatrix()) +
          " subtracted by " + str(matrix2.getMatrix()) + " is " + str(matrix.Matrix.subMatrix(matrix1, matrix2)))
    pass
  else:
    pass

def organize_input():
  input1 = []
  input2 = []
  col = int(input("Enter row for the two matrices: "))
  row = int(input("Enter col for the two matrices: "))
  for x in range(col):
    for y in range(row):
      userInput = int(input("Enter one number: "))
      input1.append(userInput)
  for x in range(col):
    for y in range(row):
      userInput = int(input("Enter one number for the second matrix: "))
      input2.append(userInput)
  return (row, col,input1, input2)
main()