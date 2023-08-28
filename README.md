[![pypi](https://img.shields.io/pypi/v/sertit.svg)](https://pypi.python.org/pypi/sertit)
[![Conda](https://img.shields.io/conda/vn/conda-forge/sertit.svg)](https://anaconda.org/conda-forge/sertit)
[![Tests](https://github.com/sertit/sertit-utils/actions/workflows/test.yml/badge.svg)](https://github.com/sertit/sertit-utils/actions/workflows/test.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Apache](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/sertit/eoreader/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5082060.svg)](https://doi.org/10.5281/zenodo.5082060)

# Sertit-Utils

Library gathering functions for all SERTIT's projects.

Find the API documentation [**here**](https://sertit-utils.readthedocs.io/en/latest/).

## Installing

### Pip
For installing this library to your environment, please type this: `pip install sertit[full]`

`[full]` will allow you to use the whole library, but you will need to install also `rioxarray` and `geopandas`
(with GDAL installation issues on Windows, so please install them from wheels that you can
find [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#rasterio)).

However, if you do not need everything, you can type instead:

- *nothing*, and you won't need `rasterio`, `rioxarray`: `pip install sertit --extra-index-url ...`
- `[rasters]`, and you won't need `rioxarray`: `pip install sertit[rasters] --extra-index-url ...`
- `[rasters_rio]`: `pip install sertit[rasters_rio] --extra-index-url ...`
- `[colorlog]`: `pip install sertit[colorlog] --extra-index-url ...` to have `colorlog` installed
- `[dask]`: `pip install sertit[dask] --extra-index-url ...` to have `dask` installed

### Conda

You can install it via conda (but you will automatically have the full version):

`conda config --env --set channel_priority strict`

`conda install -c conda-forge sertit`

## What is in it ?

### Files

Helpers for files, i.e. :

- paths
- Create archive
- Add folder to zip file
- file extraction
- file name
- copy/remove
- find files
- JSON/pickles
- hash
- ...

### Logs
Helpers for logs, i.e. :
- Init simple logger
- Create complex logger (file and stream + color)
- Shutdown and reset logger
- ...

### Misc
Helpers of all sort, i.e. :
- Function on lists: convert a list to a dict, remove empty values...
- Function on dicts: nested set, check mandatory keys, find by key
- Run a command line
- Get a function name
- Test if in docker
- Change current directory (`cd`) as a context manager
- ...

### Strings
Helpers for string manipulation, i.e. :
- Conversion from string to bool, logging level, list, list of dates...
- Convert the string to be usable in command line
- Case conversion (`snake_case` to/from `CamelCase`)
- ...

### Vectors
Helpers for vector functions, i.e. :

- Read vectors from disk or on the cloud
- Load an AOI as WKT
- Get UTM projection from lat/lon
- Manage bounds and polygons
- Get `geopandas.Geodataframe` from polygon and CRS
- ...

### Rasters and rasters_rio
Helpers for rasters functions, i.e. :

- Get extent and footprint of a raster
- Read/write overload of rasterio functions
- Masking and cropping with masked array
- Collocation (superimpose)
- Sieving
- Vectorization and get nodata vector
- Merge rasters (as GTiff and VRT)
- Get the path of the BEAM-DIMAP image that can be read by rasterio
- Manage bit arrays
- Hillshade and slope computation
- ...

The main difference between the two is that `rasters` outputs one `xarray` variable
when `rasters_rio` outputs `numpy.ma.masked_arrays` + `dict` for the raster array and its metadata.

### Network
- Standard [Exponential Backoff](https://en.wikipedia.org/wiki/Exponential_backoff) algorithm
- ...

### SNAP

Helpers for SNAP, such as creating a GPT command line with optimizations

### XML

Helpers for handling XMLs objects (lxml.etree Elements), i.e.:
- Read and write elements
- Add, update and remove nodes
- ...

### CI

Helpers for CI with function asserting equality between rasters, geometry, files, XML...

### arcpy

Helpers for arcpy integration, i.e. a logger class designed to work with ArcGis logs.

### display

Helpers scaling images for display purposes.

## Documentation

An HTML documentation is provided to document the code.
It can be found:

- online ([here](https://sertit.github.io/sertit-utils/)),
- on git, in `docs`.
  To consult it, just open the `index.html` file in a web browser (you need first to clone this project)
  To generate the HTML documentation, just type `pdoc sertit -o docs\html -f --html -c sort_identifiers=False`
