df=open('solar.lean2015.ann1610-2014.txt','rb')
a=[]
for i in df:
    if len(i.split())==3:
        year,watt,w=i.split()
        a.append(year+','+watt)
f=open('result','wb')
f.write("\n".join(a))
f.close()

import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('result')
df.columns=['year','watt']
plt.xlabel('year')
plt.ylabel('W/m^2')
plt.plot(df['year'],df['watt'],'ko')
fig=plt.figure(1)
fig.set_size_inches(10,3)
plt.savefig('test.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()
