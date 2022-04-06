with open('KITU.INP', 'r') as fi:
          n=fi.readline()
          count1=0
          count2=0
          lst_count=[]

with open('KITU.OUT', 'w') as fo:
          point= set(n)
          lst1=list(point)
          lst_count = [0] * len(lst1)
          print(lst1)
          print(lst_count)
