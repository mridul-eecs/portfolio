| . | . |
| - | - |
| ![NASA](http://www.nasa.gov/sites/all/themes/custom/nasatwo/images/nasa-logo.svg) | ![NCCS](https://www.nccs.nasa.gov/sites/default/files/NCCS_Logo_0.png) |

# Spring 2022 Python Course Series

We provide a set of classes focusing on data visualization with Python.
Data visualization is the graphical representation (line plot, pie chart, histogram, contour plot, map, etc.) of information and data.
Data visualization tools provide an accessible way to see and understand trends, 
outliers, and, insights,  patterns in data.
The tools offer us the ability to see at a glance what matters. 
They are essential to analyze massive amounts of information and make data-driven decisions.
In this series of presentations, we will introduce a few Python packages to visualize geospatial data.
We will learn how to do simple 2D static plots as well as interactive time series maps.

We are particularly interested in:

- **Matplotlib**: One of the most known Python library for data visualization. It is mainly used for 2D static plots.
- **GeoPandas**: Enables the use and manipulation of geospatial data. It provides support for geographic data to Pandas objects.
- **Cartopy/Xarray**: Cartopy is designed for geospatial data processing in order to produce maps and other geospatial data analyses. Xarray handles labeled multi-dimensional arrays and performs advanced analytics and visualization. The two packages can be combined to manipulate and visualize geospatial data.
- **HoloViews**: Conveys the message that data is trying to tell rather than focusing on how to do visualizations. Produces interactive plots.
- **GeoViews**: Facilitates the exploration and visualization of any data that includes geographic locations. 

We will also provide two tutorials on internally built packages (by Code 606 staff) that rely on the above tools:

- eViz
- iViz

The packages can be used to visualize outputs from models such GEOS-5, modelE, LIS and WRF.

## Requirements

To take any of the course, you are expected to be familiar with Python and to have knowledge of Numpy and Pandas.
You can refer to the following materials (Jupyter notebook files) to learn about those topics:

- [Introduction to Numpy](https://git.mysmce.com/astg/training/py_materials/-/blob/master/numpy/introduction_numpy.ipynb)
- [Introduction to Pandas](https://git.mysmce.com/astg/training/py_materials/-/blob/master/pandas/introduction_pandas.ipynb)

You are also expected to have a Google Mail (gmail) account that will be needed to access either Google Colab or the NASA Center for Climate Simulation (NCCS) Science Data Managed Cloud Environment (SMCE: [https://astg.mysmce.com](https://astg.mysmce.com)). In case SMCE is used, we will ask you to provide (once) your gmail userid.



## List of Courses

### Matplotlib

Matplotlib is one of the most popular Python packages used for data visualization. It is a cross-platform library for making 2D plots from data in arrays. It can be used in python scripts, shell, web application servers and other graphical user interface toolkits. In this course, we will present the anatomy of a Matplotlib figure and show to produce various 2D plots with Matplotlib.

- **Prerequisites**: Familiarity with Python, Numpy.
- **Date**: Tuesday, February 8, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-ITM
- **Registration Link**: [GSFC-600-ITM](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dREGISTRATION%26scheduleID%3d131886%26fromSF%3dY&company=NASAHCM03)


### Introduction to GeoPandas

GeoPandas is a Python open-sourced library that extends the features of Pandas with the ability to read, analyze, and visualize geospatial data. It combines the capabilities of Pandas and Shapely, providing geospatial operations in Pandas and a high-level interface to multiple geometries to Shapely. In this course, we will introduce the basic data structure of GeoPandas (GeoSeries and GeoDataFrame), show a simple example on how to create such a data structure. We will then learn how to read various csv files (containing geospatial information) and create different types of maps.

- **Prerequisites**: Numpy, Pandas, Matplotlib.
- **Date**: Tuesday, February 15, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-GEOP
- **Registration Link**: [GSFC-600-GEOP](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dREGISTRATION%26scheduleID%3d131887%26fromSF%3dY&company=NASAHCM03) 


### Xarray and Cartopy for Data Visualization

Xarray is an open-source library providing high-level, easy-to-use data structures and analysis tools for working with multidimensional labeled datasets and arrays in Python. Xarray combines the convenience of labeled data structures inspired by Pandas with the multi-dimensional arrays of NumPy and parallel out-of-core computation from Dask to provide an intuitive, powerful and scalable platform for scientific analysis. Xarray introduces labels in the form of dimensions, coordinates and attributes on top of raw Numpy-like arrays. It is particularly tailored to working with netCDF files. 
Cartopy is a Python package designed for geospatial data processing to produce maps and other geospatial data analyses.
In this course, we will show how to use Xarray and Cartopy to visualize geospatial data. We will also combine Xarray and Hvplot
to produce interactive and live plots.

- **Prerequisites**: Numpy, Pandas, Matplotlib.
- **Date**: Tuesday, February 22, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-XCDV
- **Registration Link**: [GSFC-600-XCDV](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dSCHEDULED%5fOFFERING%5fDETAILS%26scheduleID%3d131891%26fromSF%3dY&company=NASAHCM03)


### Interactive Visualization with HoloViews

HoloViews is an open-source Python library designed to make data analysis and visualization seamless and simple. It helps users understand their data better, by letting them work seamlessly with both the data and its graphical representation. HoloViews focuses on bundling users’ data together with the appropriate metadata to support both analysis and visualization, making users’ raw data and its visualization equally accessible at all times. In this course, we will learn how to create various plots (line plot, scatter plot, histogram, etc.) with HoloViews.

- **Prerequisites**: Numpy, Pandas, Matplotlib.
- **Date**: Tuesday, March 1, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-IVH
- **Registration Link**: [GSFC-600-IVH](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dSCHEDULED%5fOFFERING%5fDETAILS%26scheduleID%3d131888%26fromSF%3dY&company=NASAHCM03)


### Introduction to GeoViews

GeoViews is a Python library that facilitates the exploration and visualization of geographical, meteorological, and oceanographic datasets. GeoViews is built on the HoloViews library for building flexible visualizations of multidimensional data.
It adds a family of geographic plot types based on the Cartopy, plotted using either Matplotlib (static maps) or Bokeh (interactive maps).
In this course, we will first explore ways to plot a collection of points (represented by their latitudes and longitudes) on a map.
We will then learn how to plot model outputs data on maps.

- **Prerequisites**: Numpy, Pandas, Cartopy, HoloViews
- **Date**: Tuesday, March 8, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-GEOV
- **Registration Link**: [GSFC-600-GEOV](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dSCHEDULED%5fOFFERING%5fDETAILS%26scheduleID%3d131885%26fromSF%3dY&company=NASAHCM03)

## List of Tutorials

### eViz Tutorial

eViz is a Python framework that provides an easy-to-use text-based interface to generate a variety of plots for diagnosing Earth system model output.  The framework leverages a Python stack that includes Matplotlib, Xarray and Cartopy to produce static images such as horizontal and zonal mean plots as well as time series, polar and Hovmoller plots. All the inputs, system settings and image specifications are fully configured in a couple of YAML files. In this tutorial we will discuss how to deploy the framework on a computing system using Python virtual environments. We will also show how to set up the YAML files to perform various plotting tasks and in particular, we will setup eViz to visualize sample GEOS model and MERRA2 output.

- **Date**: Friday, ~~March 18~~ May 13, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-eViz
- **Registration Link**: [GSFC-600-eViz](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dREGISTRATION%26scheduleID%3d131889%26fromSF%3dY&company=NASAHCM03)

#### Obtaining the Materials

1) **Install Docker**

Mac: [https://docs.docker.com/desktop/mac/install/](https://docs.docker.com/desktop/mac/install/)

Windows: [https://docs.docker.com/desktop/windows/install/](https://docs.docker.com/desktop/windows/install/)

2) **Make sure you have access to NASA OneDrive**

You need to be withing the NASA firewall (VPN):

[https://nasa.sharepoint.com/sites/OneDriveSupport/SitePages/Collabor.aspx](https://nasa.sharepoint.com/sites/OneDriveSupport/SitePages/Collabor.aspx)

3) **Download Docker Image**

Download the file (more than 11 Gb)):

[https://nasa-my.sharepoint.com/:u:/g/personal/vvalenti_ndc_nasa_gov/EekjCMcHSUFLpxFiDKvXorUBKdGKNq2GWpTWhFMykwjW8Q?e=QTpxzg](https://nasa-my.sharepoint.com/:u:/g/personal/vvalenti_ndc_nasa_gov/EekjCMcHSUFLpxFiDKvXorUBKdGKNq2GWpTWhFMykwjW8Q?e=QTpxzg)

You will get the file `eviz.tar`.

4) **Run the Docker**

The following instructions are for Mac users.

4.1) Load tarball into docker

You first need to run the `Docker app`, a little whale icon will appear on the right side of the menubar atop your screen. 
It'll take a few minutes to get running, and `Docker` may ask your permission to use services on your computer. 

Open a new terminal and make sure that the `docker` command is available:

     which docker

The issue the command:

     docker load --input FULL_PATH/eviz.tar

and the following will appear on your screen (terminal):

     bf8cedc62fb3: Loading layer [==================================================>]  75.14MB/75.14MB
     3aee53e23b12: Loading layer [==================================================>]  338.9MB/338.9MB
     dcdbd75973be: Loading layer [==================================================>]  3.072kB/3.072kB
     234e2efd9aff: Loading layer [==================================================>]  9.216kB/9.216kB
     b6704fd8749f: Loading layer [==================================================>]  2.545GB/2.545GB
     de6487419841: Loading layer [==================================================>]  12.29kB/12.29kB
     3b6cefdf590e: Loading layer [==================================================>]  6.656kB/6.656kB
     3fb4b95983c5: Loading layer [==================================================>]  38.08MB/38.08MB
     e64a77ace59f: Loading layer [==================================================>]  8.894GB/8.894GB
     Loaded image: eviz:latest

4.2) Start the container: docker

Issue the command (`USERID` is your local userid):

     docker run -it -p 8080:8080 -v /Users/USERID/scratch/docker_plots:/usr/src/app/plots eviz

and you will get a new prompt on the terminal.


**If you do have an account on DISCOVER**, then the above steps are optional. 
However, on the day of the tutorial you will have to login to the DISCOVER system, go to your NOBACKUP space
and clone the `eViz` repository as follows:

     git clone -b develop /discover/nobackup/ccruz/eviz/eviz.main

**Please only issue the `git clone` commaand on the day of the tutorial (after 11:00 am).**

<!---
--->

### iViz Tutorial

iViz is an interactive visualization dashboard tool within eViz, based on python packages HoloViews, GeoViews, Xarray, Cartopy, and Panel. iViz offers a highly interactive GUI dashboard that can visualize various Earth system and climate model data. This training will teach attendees how to create custom visualizations, make comparisons with other data, create time averages and time series, and store personal plot options and visualization sessions. Attendees will learn how to launch the tool and visualize several different datasets, including provided GEOS datasets and remote climate datasets.


- **Date**: Friday, ~~March 25~~ May 20, 2022 (13:00 to 16:00 US EST)
- **SATERN Course ID**: GSFC-600-iViz
- **Registration Link**: [GSFC-600-iViz](https://hcm03.ns2cloud.com/sf/learning?destUrl=https%3a%2f%2fnasa%2dhcm03%2ens2cloud%2ecom%2flearning%2fuser%2fdeeplink%5fredirect%2ejsp%3flinkId%3dREGISTRATION%26scheduleID%3d131890%26fromSF%3dY&company=NASAHCM03)

#### Obtaining the Materials

1. **Install Docker**

Docker is an application that allows you to run applications in a “container” that is separate from your OS environment.

Mac: [https://docs.docker.com/desktop/mac/install/](https://docs.docker.com/desktop/mac/install/)

Windows: [https://docs.docker.com/desktop/windows/install/](https://docs.docker.com/desktop/windows/install/)

We will use Docker to create a container to run the iViz software and access some sample model data.

2. **Make sure you have access to NASA OneDrive**

While within the NASA firewall (VPN turned on), access the webpage below:

[https://nasa.sharepoint.com/sites/OneDriveSupport/SitePages/Collabor.aspx](https://nasa.sharepoint.com/sites/OneDriveSupport/SitePages/Collabor.aspx)

If you do not have an error message, you can proceed to the next step.

3. **Download Docker image tarball from:**

[https://nasa-my.sharepoint.com/:u:/g/personal/ccruz_ndc_nasa_gov/EVZz3fCHWOVNh-lmi82aO7UBSIM_d7IXP03dtJnqA-gcHQ](https://nasa-my.sharepoint.com/:u:/g/personal/ccruz_ndc_nasa_gov/EVZz3fCHWOVNh-lmi82aO7UBSIM_d7IXP03dtJnqA-gcHQ)

**Note that the file is over 9 Gb.** It takes anywhere from 20 minutes to more than 1 hour to download. That will depend on your connectivity as well as other network issues you may experience.

4. **Run the Docker**

- Start up the Docker application, if you have not done so already.
- After downloading the Docker image from the NASA OneDrive, navigate to the folder containing the Docker image and run load the tarball into docker:

     docker load --input iviz.tar

Note that the above command can take a few minutes. Please be patient.

Start the container:

     docker run -it -p 8080:8080 -v /Users/ccruz/scratch/docker_plots:/usr/src/app/plots iviz

The path after the `-v` option, `/Users/ccruz/scratch/docker_plots`, should reflect where you want the “plots volume” directory to be mounted (it will of course be different that the one above). 
That will allow you to access the plots generated in the container, `/usr/src/app/plots`, from your machine. 
Note that after you run the `docker run` command you will be in the Docker container and will see a different path, something like this:

     (base) root@821256789b56:/usr/src/app#

In another terminal you should now be able to see

     /Users/ccruz/scratch/docker_plots



## Accessing the SMCE Platform

To log in to the NASA Center for Climate Simulation (NCCS) Science Data Managed Cloud Environment (SMCE), click on the link:
 
[https://astg.mysmce.com](https://astg.mysmce.com)

It is assumed that you have already provided your gmail userid.
The system will ask you to provide your gmail password or give you automatic access if you are already logged in into gmail (through your browser).

We recommend that 2-4 days before the beginning of each class, you provide your gmail userid by filling out the online form:

[Provide your gmail userid HERE](https://forms.gle/JaCFNocQQP2WxYhL9)

### Installing the Anaconda Python Distribution

You not required to have Python installed on your computer.
If you want to have a Python distribution on your local platform, 
we recommend using he Anaconda Python distribution. 
To install it, follow the instructions at: [Anconda installation Guide](https://docs.continuum.io/anaconda/install/).
If you have a Mac, it is preferable to use the command line installation option.

**Note that you are not required to install anything on your local platform to take a course here.
The SMCE platform is self-contained and has all we need. 
However, we believe that it is important to have a local Python distribution that you can
use for code development. **

## Accessing the Materials

The materials are in a Git repository that can be cloneed:

```shell
     git clone https://git.mysmce.com/astg/training/py_materials.git
```

When you issue the above command, you will get a folder named `py_materials`.

## Teaching Team

- Vanessa Valenti (vanessa.l.valenti@nasa.gov)
- Bruce Van Aartsen (bruce.vanaartsen@nasa.gov)
- Carlos Cruz (carlos.a.cruz@nasa.gov)
- Megan Damon (megan.r.damon@nasa.gov)
- Aaron Skolnik (aaron.skolnik@nasa.gov)
- Jules Kouatchou (jules.kouatchou@nasa.gov)

