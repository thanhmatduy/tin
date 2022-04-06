with open('INCSEQ.INP','r') as fi:
          l = int(fi.readline())
          lst1= list(map(int, fi.readline().split()))
          check_index = [1]*l
with open('INCSEQ.OUT','w') as fo:
          for i in range(len(lst1)):
                    for j in range(i,len(lst1)):
                              