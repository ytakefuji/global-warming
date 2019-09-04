# global-warming
solarplot.py (Python2) or solarplot_py3.py (Python3) is a program to plot total solar irradiance from 1610 to 2014.

solar.lean2015.ann1610-2014.txt should be downloaeded from NASA site:

https://data.giss.nasa.gov/modelforce/solar.irradiance/solar.lean2015.ann1610-2014.txt

<pre>
$ python2 solarplot.py
or
$ python3 solarplot_py3.py
</pre>

test.png is the result.
===========
# NOAA TSI
NOAA file is based on netCDF4.
In order to read .nc file, you can use netCDF4 library.
<pre>
$ pip install netCDF4
You have to download tsi_v02r01_yearly_s1610_e2018_c20190409.nc file:

https://www.ncei.noaa.gov/thredds/fileServer/cdr-total-solar-irradiance/yearly/tsi_v02r01_yearly_s1610_e2018_c20190409.nc

To generate TSI file (noaaTSI1610-2019)
$ python readNC.py|grep 136 >noaaTSI1610-2019

To generate year and TSI file(t.csv) 
$ python noaa.py

t.csv can be generated. 

To generate noaa.png, run the following command
$ python noaaplot.py
</pre>

noaa.png is finally generated.
=======
# 
