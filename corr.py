import pandas as pd
t=pd.read_csv('gtemp.csv')
co2=pd.read_csv('co2')
t.columns=['year','temp']
co2.columns=['year','co2']
t=t['temp']
co2=co2['co2']
print(len(t),len(co2))
import numpy as np
print(np.corrcoef(t,co2))
from scipy.stats.stats import pearsonr  
print(pearsonr(t,co2))
