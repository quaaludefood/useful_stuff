#!/bin/bash
target="/code/app/data"

for file in "$target"/*
do
    filename=$(basename -- "$file")
    filename_without_ext="${filename%.*}"
    /root/miniconda3/bin/gdal_polygonize.py "$file" "-f" "GeoJSON" "/code/app/output/$filename_without_ext.json"
done

