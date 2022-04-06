with open('kituchung.inp','r') as fi:
          n = list(set(fi.readline()))
          m = list(set(fi.readline()))
          check=[]
with open('kituchung.out','w') as fo:
          for i in m:
                    if n.count(i)>0:
                              check.append(i)
          check.sort()
          fo.write(('\n'.join(check)))