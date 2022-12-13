#!/usr/bin/env python

"""
   This code attempts to do the following:
    - Read the AERONET daily AOD data for 2010 on a couple of sites (Alta_Floresta, Anmyon, 
      Beijing, Capo_Verde, Fresno, GSFC, Ilorin, Kanpur, Lille, Mongu).
    - Interpolates the 440 and 675 nm AOD to a commonly used wavelength of 550 nm 
      (although there are many wavelengths of AOD in AERONET, most available ones are 440, 675, 870, 1020 nm).
    - Read GEOS-5 (Icarusr6r6) model outputs and extract the values of AOT at the selected sites.
    - Plot the time series of the AOD at each location from AERONET and GEOS-5.

   This script was tested on discover:
       /discover/nobackup/jkouatch/LearningPython/Code614/compare_GEOS_AERONET_general.py
 
   Author: Jules Kouatchou
"""

#-------------
# Load modules
#-------------
import sys
import os
import glob
import math
import numpy as np
import netCDF4 as nc4
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
import pandas as pd
import datetime as dttime

def calc_rows_columns(n, nColumns=None):
    """
      Takes a number n and decomposes it into nrows and ncols
      so that n = nrows*ncols.

      Required input:
        - n: a positive integer

      Returned value:
        - nrows,ncols: integers given by n = nrows*ncols
    """

    if (nColumns == None):
       a = math.sqrt(n)
       nrows = int(math.ceil(a))

       while True:
          if ((n % nrows) == 0):
             ncols = int(n / nrows)
             break
          else:
             nrows = nrows + 1
    else:
        nrows = int(n / nColumns)
        if (nrows*nColumns < n):
           nrows = nrows + 1
        ncols = nColumns

    return nrows, ncols

def get_index(ref_array, my_value):
    """
      Function for extracting the index of a Numpy array (ref_array)
      which value is closest to a given number.

      Input parameters:
        - ref_array: reference Numpy array
        - my_value:  floating point number

      Returned value:
        - An integer corresponding to the index
    """
    return np.abs(ref_array - my_value).argmin()


def read_aeronet_file(filename):
    """
      Read AERONET data file.
    """
    dateparse = lambda x: dttime.datetime.strptime(x, '%d:%m:%Y %H:%M:%S')
    df = pd.read_csv(filename, skiprows=6, na_values=-999,
                     parse_dates={'datetime': [0, 1]},
                     date_parser=dateparse, index_col=0, squeeze=True)
    return df

old_cols = ['Day_of_Year', 'AOD_675nm', 'AOD_440nm',
            '440-675_Angstrom_Exponent']

new_cols = ['DoY', 'A675', 'A440', 'Alpha']

aeronet_dir = '/discover/nobackup/projects/gocart/mchin/data/aeronet/daily'

YEAR = 2010

list_sites = ['Alta_Floresta', 'Anmyon', 'Beijing', 'Capo_Verde',
              'Fresno',        'GSFC',   'Ilorin',  'Kanpur',
              'Lille', 'Mongu']

num_sites = len(list_sites)

site_lat = list()
site_lon = list()
site_data = list()
site_DoY = list()

#------------------------------
# Read AERONET Data files
#------------------------------
for k in range(num_sites):
    fname = aeronet_dir + os.sep + '19930101_20210102_'+list_sites[k]+'.lev20'

    if not os.path.isfile(fname):
       print("The file {} does not exist".format(fname))
       sys.exit()

    print("\t Read AERONET data for {} {}/{}".format(list_sites[k], k+1, num_sites))
    df = read_aeronet_file(fname)
    site_lat.append(df['Site_Latitude(Degrees)'][0])
    site_lon.append(df['Site_Longitude(Degrees)'][0])

    df2 = df[df.index.year == YEAR][old_cols]
    df2.columns = new_cols
    A550 = df2['A675']*(675.0/550.0)**df2['Alpha']
    site_data.append(A550)
    site_DoY.append(df2['DoY'])

# Free up memory
df = None
df2= None
A550 = None

#----------------------
# Read GEOS Daily files
#----------------------
geos_dir = '/discover/nobackup/projects/gocart/mchin/data/Icarusr6r6/tavg2d_aer_x/daily'
list_geos_files = glob.glob(geos_dir + os.sep + 'Icarusr6r6.tavg2d_aer_x.'+str(YEAR)+'*')

num_files = len(list_geos_files)

ilat = list()
ilon = list()

first_read = 1
idx = -1
for geos_file in list_geos_files:
    idx += 1
    print("\t  {}/{}: {}".format(idx+1, num_files, os.path.basename(geos_file)))
    with nc4.Dataset(geos_file, 'r') as fid:
         if first_read:
            first_read = 0
            lat = fid.variables['lat'][:]
            lon = fid.variables['lon'][:]

            for k in range(num_sites):
                ilat.append(get_index(lat, site_lat[k]))
                ilon.append(get_index(lon, site_lon[k]))

            geos_data = np.zeros((num_sites, num_files))

         AOT_550 = fid.variables['TOTEXTTAU'][0]
         for k in range(num_sites):
             geos_data[k, idx] = AOT_550[ilat[k],ilon[k]]

#--------------------
# Do time series plots
#--------------------
nrows, ncols = calc_rows_columns(num_sites)

fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(15,12))

xvals = np.arange(1, num_files+1)

k = 0
for row in range(nrows):
    for col in range(ncols):
        axes[row, col].plot(site_DoY[k], site_data[k], label='AERONET', color='black')
        axes[row, col].plot(xvals, geos_data[k], label='GEOS', color='red')
        axes[row, col].set_title(list_sites[k])
        axes[row, col].legend()
        k += 1

plt.tight_layout()
plt.show()

