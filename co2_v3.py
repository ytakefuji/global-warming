co2=open('co2_v2.txt','r',encoding='utf-8')
data=[]
for i in co2:
 a,b,c,d,e,f,g=i.split()
 data.append(a+'_'+b+','+e)
f=open('co2_v2','w',encoding='utf-8')
f.write("\n".join(data))
f.close()

import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_csv('co2_v2')
data.columns=['year','co2']
plt.xlabel('year')
plt.ylabel('density')
plt.xticks(rotation='vertical',fontsize=6)
plt.plot(data['year'],data['co2'],'k.')
fig=plt.figure(1)
fig.set_size_inches(10,5)
plt.savefig('co2_v2.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()
