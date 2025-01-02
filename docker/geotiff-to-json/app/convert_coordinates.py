import argparse

from osgeo import gdal,osr


ds = gdal.Open('/code/app/data/GHS_2030_UK.tif')
width = ds.RasterXSize
height = ds.RasterYSize
print(width, height)
print("works")


