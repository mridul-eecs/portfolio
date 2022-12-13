#!/usr/bin/env python

"""
   This script allows us to read remote MERRA2 data files using
   the NASA EarthData credential.

   We use here the urllib module.

   It is assumed that the user has a valid username and password at EarthData:

        https://urs.earthdata.nasa.gov

   It might also be necessary to link GES DISC with your EarthData account:

        https://disc.gsfc.nasa.gov/earthdata-login
"""

import urllib.request as urllib
import getpass

earthdata_url = "https://urs.earthdata.nasa.gov"

# Remote MERRA-2 file information
file_url = "https://goldsmr4.gesdisc.eosdis.nasa.gov/opendap/MERRA2/M2T1NXAER.5.12.4/2020/01/"
remote_fname = "MERRA2_400.tavg1_2d_aer_Nx.20200131.nc4.nc4"
local_fname = remote_fname[:-4]

# Obtain the user's credential in the EarthData website
username = input("Provide your EarthData userid: ")
password = getpass.getpass("Provide your EarthData password: ")

# Create an object for redirecting server
redirectHandler = urllib.HTTPRedirectHandler()

# Create special opener with support for Cookies
cookieProcessor = urllib.HTTPCookieProcessor()

# Create the password manager and load with the credentials 
passwordManager = urllib.HTTPPasswordMgrWithDefaultRealm()
passwordManager.add_password(None, earthdata_url, username, password)
authHandler = urllib.HTTPBasicAuthHandler(passwordManager)

# Open a connection to the EarthData server
opener = urllib.build_opener(redirectHandler, cookieProcessor, authHandler)
urllib.install_opener(opener)

# Read the remote file
response = urllib.urlopen(file_url+remote_fname)
data_obj = response.read()

# Write the content of the remote file in a local file
with open(local_fname, "wb") as fid:
    fid.write(data_obj)


