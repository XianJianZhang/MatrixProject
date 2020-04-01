def main():
  print("Hello, welcome to matrix addition and subtraction!")
  matrix_operation(choice())

#Returns choice of operation by the user
def choice():
  choice_op = input("Enter your choice of operation: mult, add, sub: ")
  while choice_op != "sub" and choice_op != "add" and choice_op != "mult":
    choice_op = input("Enter your choice of operation: mult, add, sub: ")
  return choice_op

#Performs one of the 3 matrix operations, given two matrices
def matrix_operation(userChoice):
  col = 0
  row = 0
  input1 = []
  input2 = []
  if userChoice == "add":
    col = int(input("Enter row for the two matrices: "))
    row = int(input("Enter col for the two matrices: "))
    for x in range(col-1):
      for y in range(row-1):
        try:
    return input1
  elif userChoice == "sub":
    pass
  else:
    pass

main()