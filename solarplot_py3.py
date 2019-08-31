df=open('solar.lean2015.ann1610-2014.txt','rb')
f=open('result','wb')
for i in df:
    if len(i.split())==3:
        year,watt,w=i.split()
        st=str(year)+','+str(watt)+'\n'
        f.write(st.encode('utf-8'))
f.close()
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('result')
df.columns=['year','watt']
plt.xlabel('year')
plt.ylabel('W/m^2')
dfy=[]
for i in df['year']:
 dfy.append(float(i.split("'")[1]))
dfw=[]
for i in df['watt']:
 dfw.append(float(i.split("'")[1]))

plt.plot(dfy,dfw,'ko')
fig=plt.figure(1)
fig.set_size_inches(10,3)
plt.savefig('test.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()
