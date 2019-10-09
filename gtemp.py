import pandas as pd
temp=pd.read_csv('GLB.Ts+dSST.csv')
t=temp.drop(['Year'],axis=1)
m=t.head(0)
data=[]
for j in range(1978,2020):
 for i in m:
  #print(j,i,temp[temp.Year==j][i].values)
  #data.append(str(temp[temp.Year==j][i]).split(' ')[4])
  a=str(temp[temp.Year==j][i].values)
  a=a.replace('[','').replace(']','').replace("'","")
  data.append((str(j)+i+','+a))
f=open('gtemp.csv','wb')
f.write("\n".join(data))
f.close()
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('gtemp.csv')
df.columns=['year','temp']
ax=plt.axes()
from matplotlib.ticker import MaxNLocator
locx=MaxNLocator(prune='both', nbins=10)
locy=MaxNLocator(prune='both', nbins=5)
ax.yaxis.set_major_locator(locy)
ax.xaxis.set_major_locator(locx)
plt.xlabel('year')
plt.ylabel('degree')
ax.plot(df['year'],df['temp'])
#ax.plot(df['year'],df['temp'],'k.')
fig=plt.figure(1)
fig.set_size_inches(10,5)
plt.savefig('temp.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()

