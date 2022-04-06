with open('QBMAX.INP', 'r') as fi:
          column, row = fi.readline().split()
          first = [0]*(int(row)+1)
          matrix = []
          end = [0]*(int(row)+1)
          n= fi.readlines()
          for i in n:
                      matrix.append((i.split()))
          for i in range(int(column)):
                    matrix[i][0] = int(matrix[i][0])
                    for j in range(int(row)-1):
                                        matrix[i][j+1] = int(matrix[i][j+1])
with open('QBMAX.OUT', 'w') as fo:
          #matrix.insert(0, first)
          #matrix.append(end)
          for i in range(int(column)):
                    print(str(matrix[i][0])+'dit cu may ')