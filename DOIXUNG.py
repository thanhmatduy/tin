with open('DOIXUNG.INP','r') as fi:
          n = fi.readline().split()
          lst1 = list(' '.join(n))
          check=[0]*len(lst1[0])
          count=0
with open('DOIXUNG.OUT','w') as fo:
          def check_symmetric(s):
                    for i in range(len(s)//2):
                              if s[i] != s[-i-1]:
                                        return False
                    return True
          print(check_symmetric(lst1))