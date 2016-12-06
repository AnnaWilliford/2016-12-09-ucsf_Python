# first, we notice that none of our data files have headers, which will be problematic for our script
head -1 *

# to fix it, we prepend the header.txt file to each and create a new file with a .head suffix
for file in human*.txt; do cat header.txt $file > $file.head; done

# our Python script isn't immediately available to us in our current working directory, so we must copy it here
cp ../gc_repeat_plot.py ./

# now we can run our analysis script on each headed file and get the plots we desire
for files in *.head; do python gc_repeat_plot.py $file; done
