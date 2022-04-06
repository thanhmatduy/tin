with open('DOANROI.INP','r') as fi:
          m=int(fi.readline())
          lst1=[]
          matrix=[]
          lst1=[]
          matrix = [list(map(int, fi.readline().split())) for i in range(m)]
with open('DOANROI.OUT','w') as fo:
          for i in range(len(matrix)):
                    for j in range(matrix[i][0],matrix[i][1]+1):
                              lst1.append(j)
                    lst1.append('|')
          print(lst1)