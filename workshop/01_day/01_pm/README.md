# Introduction to Shell

1. Introducting the Shell
2. Navigating Files and Directories
3. Working with Files and Directories
  - Have students download and unzip a set of files for all human chromosomes (they have 21) - will be used later
  - [Data](https://github.com/darencard/2016-12-09-ucsf_Python/blob/gh-pages/workshop/01_day/01_pm/human_window_stats_sab.zip?raw=true)
4. *Break*
5. Pipes and Filters
  - As in Nelle's pipeline, there will be some files that are messed up (different length), which will be obvious when they start sorting data by length
  - They'll need to fix these issues with the data before running their shell script
  - Here are the problems to fix:
    1. `human chr4.txt` should be `human_chr4.txt` for consistency
    2. `human.chr16.txt` should be `human_chr16.txt` for consistency
    3. `human_chr1.txt` contains data for chr1, chr10, and chr11 (but not in order). Demonstrates a common wild-card issue that people encounter. Need to use `sort` and `head`/`tail` to separate out. `human_chr10.txt` and `human_chr11.txt` files are fine, so can overwrite them or just delete proper lines in `human_chr1.txt`
    4. `human_chrSex.txt` contains information about the `X` and `Y` chromosomes, but pasted side by side. Need to use `cut` to extract each into `human_chrX.txt` and `human_chrY.txt`, and delete the original.
6. Loops
  - After introducting, will have students run their python script and produce a set of output plots comparing a couple stats for each chromosome file
7. Shell Scripts
  - Work the for loop into a nice script that they can save, which automates their analysis. They'll keep this shell script and their Python script for the later Git lesson
8. Finding Things
  - Some grep/find would be cool. I'll certainly cover some subsetting in Python, but shell is so powerful here.
  - Once they've cleaned their data and corrected issues, we'll have them concatenate all chromosome data together into one file, for later work in Python in Day 2.
  - Can use this combined dataset to play around with things like grep, and can also introduce cut/sort/uniq/etc.
