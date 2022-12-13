| . | . |
| - | - |
| ![NASA](http://www.nasa.gov/sites/all/themes/custom/nasatwo/images/nasa-logo.svg) | ![NCCS](https://www.nccs.nasa.gov/sites/default/files/NCCS_Logo_0.png) |

# Fall 2021 Python Course Series: Hackathon
### Thursday, October 28, 2021
### 9:00 am – 3:30 pm

**Participants:**

- Mei Han (GSFC-612.0)
- Jules Kouatchou (GSFC-606.0)
- Dana R. Louie (GSFC-667.0)
- Xiaomei Lu (LARC-E304)
- Brian E. Magill (LARC-E304)
- Carlos Ordaz (CUNY/GISS)
- Xiaohua Pan (GSFC-610.2)
- Nazma I. Syeda (GSFC-662.0)
- Yujie Wang (GSFC-613.0)


## Objectives

The main objective of the Hackathon was to create a space where people of 
various programming, engineering, and science backgrounds, work together to 
write sample Python workflows to manipulate remote NASA data files on the cloud. 
We wanted to engage and encourage Python learners in using Data Science tools 
such as Pandas, Dask, Xarray, BeautifulSoup, etc.

We did not intend here to solve a Science/Engineering problem. 
We only wanted to write simple tools that can be used for prototyping and 
later be expended into Science/Engineering products. Each task was meant to 
address a specific need that would be beneficial to the Science/Engineering community. 
The expectation was not to complete all the tasks, but to engage participants 
so that they could ask questions, bring their own perspectives in finding solutions, etc.


The plan was to:

- Do web scraping to locate the the remotedata files of interest..
- Download or directly read (ideally) the remote files
- Carry out basic data analyses
- Perform interactive visualization.

## Project Description
In anticipation of the event, Python scripts were written. 
The scripts downloaded remote NASA files and manipulated data.
They worked well on local machine but needed to be modified to work
on cloud-based platforms, to avoid downloading files into disc and
to accelerate and simplify file access.

#### Script 1: 
This Python code reads AERONET data at a specific site. 
The process involves writing the data in a file before reading the file using Pandas. 
For a given site, we want to directly read the AERONET data from the remote server 
by avoiding the creation of a temporary file. 
Also want to use web scraping to provide a range of dates when the data are available. 

#### Script 2: 
The code accesses a remote MERRA2 file and downloads the data in a local netCD-4 file. 
We want to be able to access and manipulate the data without having to write the data on the disc. 
Alternatively, extract from the download file the fields we need, save then in a new file 
and remove the downloaded file. 


#### Script 3: 
This code first reads local AERONET data files at given sites. 
It carries out calculations to determine the time series aerosol optical depth (AOD). 
The code reads daily GEOS-5 model outputs to extract global AOD. 
It finally compares at each site, the AOD from observations (AERONET) and model (GEOS-5) 
by doing a time series plot. 
Here, we want directly access AERONET servers to read site data, read the 
daily model files at once (instead of one at the time), and improve the time series plots.

## Implmentation

We used the NASA Center for Climate Simulation (NCCS) 
[Science Data Managed Cloud Environment (SMCE)](https://astg.mysmce.com)
that was configured to have 32 cores and 128Gb of RAM.
All the three scripts were included in separate Jupyter notebook files that
were use on the SMCE.

The assignments of all the scripts were connected. 
We subdivided the work into small tasks.

**Task 1** 

- Script 3: Use the Xarray package to read the MERRA2 netCDF files and reproduce the plots. The x-axis of the plot should be dates instead of numbers.

**Task 2**

- Script 1: Modify the sample script to have a disc-less reading of AERONET remote data for any arbitrary station and any date range.

**Task 3**

- Script 3: Modify the script to include the reading of AERONET remote data for the selected sites and the specified date range. 

**Task 4**

- Script 2: Modify the sample script to read the remote data file without first downloading the data. Alternatively, if downloading cannot be avoided, use a system temporary location to store the data.

**Task 5**

- Script 3: Revisit the script to see if we can read remote MERRA2 files

### Accomplishments

In the process of preparing this Hackathon and during the event, 
we wrote Python codes to successfully do the following:

- Read remote AERONET data (from any site) without downloading any file on the local machine.
- For any abitrary AERONET site, do web scraping to extract the range of dates when the data are available.
- Download remote GEOS-5 MERRA2 data files without creating a configuartion file on the local machine.

In addition to the above, we did data analyses and visualizations to show how Python
can be sued in the cloud to manipulale NASA datasets.

All our accomplishments are contained in the following Jupyter notebook files:

- Read AERONET data: [read_aeronet_data.ipynb](read_aeronet_data.ipynb)
- Read MERRA2 data: [read_merra2_data.ipynb](read_merra2_data.ipynb)
- Compare observations and model outputs: [compare_merra2_aeronet.ipynb](compare_merra2_aeronet.ipynb)

#### Remarks

- Tasks 1-3 were completed.
- In Task 4, we could not figure out how to avoid downloadind the file (500 Mb). At least we were able to take from the filethe field we were interested in and save it in a new file (1 Mb).
- It is important to note thate if a configuration file is created on a local machine, we can read directy remote MERRA2 data files. It is not desirable to have such a file in a cloud platform.
- Task 5 could not be done because of the limitations in Task 4.

## Acknowledgements

This work was possible because of the dedication of Aaron Skolnik who worked in the background to make sure
that the NASA Center for Climate Simulation (NCCS) Science Data Managed Cloud Environment (SMCE) was available
to us before, during and after the event.
