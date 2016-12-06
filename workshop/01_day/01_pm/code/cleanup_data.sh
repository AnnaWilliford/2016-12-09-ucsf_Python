# download data
wget https://github.com/darencard/2016-12-09-ucsf_Python/blob/gh-pages/workshop/01_day/01_pm/data/human_window_stats_sab.zip?raw=true

# unzip data, move into directory, view contents
unzip human_window_stats_sab.zip\?raw\=true
cd human_sabotaged/
ls

# rename chr4 and chr16
mv human\ chr4.txt human_chr4.txt
mv human.chr16.txt human_chr16.txt

# gather line counts and sort to see if any files are weird, chr1 is
wc -l * | sort -n -r

# fix chr1 file by extracting only chr1 data and replace old one
head -40 human_chr1.txt | tail -20 > chr1_fix.txt
cat chr1_fix.txt
mv chr1_fix.txt human_chr1.txt

# gather word counts and sort to see if any files are weird, chrSex is
wc -w * | sort -n -r
cat human_chrSex.txt

# use cut to separate chrSex into chrX and chrY, delete chrSex
cut -f 1-8 human_chrSex.txt > human_chrX.txt
cut -f 9- human_chrSex.txt > human_chrY.txt
rm human_chrSex.txt
