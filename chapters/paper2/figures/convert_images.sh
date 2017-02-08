#!/bin/bash
convert volume_scatter.png strain_scatter_1.png +append data_matching.png
convert emax.png global_synch_mean.png +append contractility.png

# convert pipeline.png -resize 2048x2048 pipeline_resize.png
convert pipeline.png -resize 1615x1615 pipeline_resize.png
convert flow.png -resize 1615x1615 flow_resize.png
# convert pipeline_resize.png flow_resize.png +append -geometry +100+100 models.png
montage -background White -mode concatenate -tile 2 -border 10x10x10x10 -bordercolor White pipeline_resize.png flow_resize.png models.png
# montage -background none -mode concatenate -tile 2 -border 50x50 -bordercolor White -mattecolor none pipeline_resize.png flow_resize.png models.png
# convert models.png -resize 100x100 models.png
