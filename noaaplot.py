import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('t.csv')
df.columns=['year','watt']
plt.xlabel('year')
plt.ylabel('W/m^2')
plt.plot(df['year'],df['watt'],'ko')
fig=plt.figure(1)
fig.set_size_inches(10,3)
plt.savefig('noaa.png',dpi=fig.dpi,bbox_inches='tight')
plt.show()
plt.close()
