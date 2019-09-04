import numpy as np
d=open('noaaTSI1610-2019','rb')
L=[[]]
for i in d:
 L.append(str(i).split("'")[1].replace('\\n','\n'))
L=np.array(L)
year=[[]]
for i in range(1610,2019):
 year.append(i)
year=np.array(year)
new=[]
for i in range(1,410):
 new.append(str(year[i])+','+str(L[i]))
np.savetxt('t.csv',new,delimiter=',',fmt='%s')
