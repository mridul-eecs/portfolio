"""
   This code attempts to read AERONET data at one specific site.
   The following steps are used:

      1- Set the parameters as provided in:

             https://aeronet.gsfc.nasa.gov/print_web_data_help_v3.html

      2- Use Requests to access the page where the data are located.
      3- Use BeautifulSoup to parse the webpage containing the data.
      4- Dump the content of the data in a CSV file.
      5- Use Pandas to read the CSV file into a Pandas DataFrame

   Author: Jules Kouatchou
"""

import sys
import requests as reqs
from bs4 import BeautifulSoup as bso
import pandas as pd
import datetime
 
base_url = "https://aeronet.gsfc.nasa.gov/cgi-bin/print_web_data_v3"

# Site information and data settings
#-----------------------------------
site_name = "Cart_Site"
beg_year = 2000; beg_month = 6; beg_day=1
end_year = 2000; end_month = 6; end_day=14
payload = {
    "site": site_name,
    "year": beg_year,
    "month": beg_month,
    "day": beg_day,
    "year2": end_year,
    "month2": end_month,
    "day2": end_day,
    "AOD10": 1,
    "AVG": 10
}
 
response = reqs.get(base_url, params=payload)
 
if response.status_code != 200:
   print(f" The url: ")
   print(f"    --> {response.url} ")
   print(f" Is not reachable. Please check your settings.")
   sys.exit()

# Pass the content of the webpage to Beautiful Soup
mysoup = bso(response.text, 'html5lib')

# Write the content of the page in a temporary CSV file
#------------------------------------------------------
tmp_csv_file = "mycsvfile.csv"
with open(tmp_csv_file, 'w') as fid:
    fid.write(mysoup.getText())
   
# Use Pandas to read the temporary CSV file
#-------------------------------------------
dateparse = lambda x: datetime.datetime.strptime(x, '%d:%m:%Y %H:%M:%S')
df = pd.read_csv(tmp_csv_file, skiprows=6, na_values=-999,
             parse_dates={'datetime': [1, 2]},
             date_parser=dateparse, index_col=0,
             squeeze=True)


