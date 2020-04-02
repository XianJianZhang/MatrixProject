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
    for x in range(self.row):
      row_list = []
      for y in range(self.col):
        index = ((x+1)*(y+1))-1
        row_list.append(self.input_num[index])
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
    new_matrix=[]
    for x in range(len(matrix1.col)):
      for y in range(len(matrix1.row)):
        matrix1[x][y]*matrix2[y][x]

