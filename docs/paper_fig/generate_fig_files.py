# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:23:03 2022

@author: 318596
"""

from rabpro.core import profiler
import geopandas as gpd
import numpy as np
import os

os.environ['RABPRO_DATA'] = r'X:\Data'

coords = (-18.0931, 177.5461)
da = 1395

f = profiler(coords, da=1395)
f.delineate_basin(force_merit=True)
gdf_merit = f.watershed
f.delineate_basin(force_hydrobasins=True)
gdf_hb = f.watershed
f.elev_profile(dist_to_walk_km=10)

gdf_merit.to_file(r'X:\Research\RaBPro\Code\docs\paper_fig\basin_merit.gpkg', driver='GPKG')
gdf_hb.to_file(r'X:\Research\RaBPro\Code\docs\paper_fig\basin_hb.gpkg', driver='GPKG')
f.flowline.to_file(r'X:\Research\RaBPro\Code\docs\paper_fig\flowline.gpkg', driver='GPKG')
