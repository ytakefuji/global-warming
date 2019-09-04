import netCDF4
f=netCDF4.Dataset('tsi_v02r01_yearly_s1610_e2018_c20190409.nc')
print(f)
for i in f['TSI']:
 print(i)
