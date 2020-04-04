class Matrix():
  def __init__(self, row, col, input_num):
    self.col = col
    self.row = row
    self.input_num = input_num
    self.matrix = Matrix.create_matrix(self)

  def __str__(self):
    border = ""
    for x in range(len(self.matrix)):
      border += "-"
    formatted = ""
    for x in range(len(self.matrix)):
      formatted += "\n" + str(self.matrix[x])
    formatted = str(formatted)
    return "\n"+border+str(formatted)
  #Creates the actual matrix
  def create_matrix(self):
    empty_list = []
    counter = -1
    for x in range(self.row):
      row_list = []
      for y in range(self.col):
        counter += 1
        row_list.append(self.input_num[counter])
      empty_list.append(row_list)
    return (empty_list)

  def getMatrix(self):
    return(self.matrix)

  def addMatrix(Matrix_object, Matrix_object2):
    matrix1 = Matrix_object.getMatrix()
    matrix2 = Matrix_object2.getMatrix()
    new_matrix=[]
    for x in range(len(matrix1)):
      row_matrix = []
      for y in range(len(matrix1[x])):
        point = matrix1[x][y]+ matrix2[x][y]
        row_matrix.append(point)
      new_matrix.append(row_matrix)
    matrix3 = Matrix(Matrix_object.row, Matrix_object.col, Matrix.toList(new_matrix))
    return matrix3

  def subMatrix(Matrix_object, Matrix_object2):
    matrix1 = Matrix_object.getMatrix()
    matrix2 = Matrix_object2.getMatrix()
    new_matrix = []
    for x in range(len(matrix1)):
      row_matrix = []
      for y in range(len(matrix1[x])):
        point = matrix1[x][y] - matrix2[x][y]
        row_matrix.append(point)
      new_matrix.append(row_matrix)
    matrix3 = Matrix(Matrix_object.row, Matrix_object.col, Matrix.toList(new_matrix))
    return matrix3

  #focusing on matrx multication
  def multMatrix(Matrix_object, Matrix_object2):
    matrix1 = Matrix_object.getMatrix()
    matrix2 = Matrix_object2.getMatrix()
    reformatted2 = []
    new_matrix=[]
    for y in range(Matrix_object2.col):
      col = []
      for a in range(Matrix_object2.row):
        col.append(matrix2[a][y])
      reformatted2.append(col)
    for x in range(Matrix_object.row):
      empty_list = []
      for y in range(len(reformatted2)):
        element = 0
        for z in range(len(reformatted2[0])):
          element += matrix1[x][z] * reformatted2[y][z]
        empty_list.append(element)
      new_matrix.append(empty_list)
    matrix3 = Matrix(Matrix_object.row, Matrix_object2.col, Matrix.toList(new_matrix))
    return matrix3

  def toList(matrixFormat):
    returnList = []
    for x in range(len(matrixFormat)):
      for y in range(len(matrixFormat[0])):
        returnList.append(matrixFormat[x][y])
    return returnList

# matrix1 = Matrix(2,2,[2,2,2,2])
# matrix2 = Matrix(2,2,[2,3,3,2])
# print(Matrix.addMatrix(matrix1, matrix2))