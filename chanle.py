with open('chanle.inp','r') as fi:
          l= int(fi.readline())
          lst1= list(map(int, fi.readline().split()))
          check = []
          count=0
with open('chanle.out','w') as fo:
          for i in range(len(lst1)-1):
                    lst2 = []
                    if lst1[i] % 2 == 0 and lst1[i+1] % 2 != 0:
                              lst2.append(lst1[i])
                              lst2.append(lst1[i+1])
                              check.append(lst2)
                              count+=1
                    if lst1[i] % 2 != 0 and lst1[i+1] % 2 == 0:
                              lst2.append(lst1[i])
                              lst2.append(lst1[i+1])
                              check.append(lst2)
                              count+=1
          if count == 0:
                    fo.write('-1')
          else:
                    fo.write(str(sum(max(check))))

