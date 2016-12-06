#!/bin/bash

# Author: Daren Card
# Date: 12/06/2016
# Description: A script to automatically plot the relationship \
# between GC content and repeat content for each chromosome \
# using our `gc_repeat_plot.py` script.

for file in *.head; 
do 
	echo "Plotting $file"
	python gc_repeat_plot.py $file
done
