co2=open('co2.txt','rb')
data=[]
for i in co2:
 a,b,c,d,e,f,g=i.split()
 if len(b)==1:
  data.append(a+'_0'+b+','+e)
 else:
  data.append(a+'_'+b+','+e)
f=open('co2','wb')
f.write("\n".join(data))
f.close()
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
data=pd.read_csv('co2')
data.columns=['year','co2']
plt.xlabel('year')
plt.ylabel('density')
plt.plot(data['year'],data['co2'],'k.')
plt.xticks(rotation='vertical',fontsize=8)
#plt.plot(data['year'],data['co2'],'k')
#plt.locator_params(axis='x',nbins=10)
fig=plt.figure(1)
fig.set_size_inches(100,50)
plt.savefig('co2.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()
