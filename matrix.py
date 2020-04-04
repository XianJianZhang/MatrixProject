class Matrix():
  def __init__(self, row, col, input_num):
    self.col = col
    self.row = row
    self.input_num = input_num
    self.matrix = Matrix.create_matrix(self)

  def __repr__(self):
    return Matrix.getMatrix()

  #Creates the actual matrix
  def create_matrix(self):
    empty_list = []
    counter = 0
    for x in range(self.row):
      row_list = []
      counter = -1
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
    return new_matrix

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
    return new_matrix

  #focusing on matrx multication
  def multMatrix(Matrix_object, Matrix_object2):
    matrix1 = Matrix_object.getMatrix()
    matrix2 = Matrix_object2.getMatrix()
    reformatted2 = []
    new_matrix=[]
    print(matrix1)
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
        print(empty_list)
        empty_list.append(element)
      new_matrix.append(empty_list)
    return(new_matrix)
matrix1 = Matrix(2,2,[1,2,3,4])
matrix2 = Matrix(2,2,[1,2,3,5])
print(Matrix.multMatrix(matrix1, matrix2))