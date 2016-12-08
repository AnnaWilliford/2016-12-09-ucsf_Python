# Introduction to Shell

# Learning objectives
After completing this session, learners should be able to:
- Replicate standard movement and actions (view, copy, and move files) from graphical file managers (e.g. Windows Explorer, OSX File Manager) in the shell.
- Understand that standard shell commands deal exclusively with raw text, and realize the implications of this information for chaining commands.
- Combine simple shell commands using pipes to create more complex actions.
- Standardize and automate data analysis workflows using loops.
- Store sequences of commands as scripts for reusable data processing.

1. Introducting the Shell (5 minutes)
2. Navigating Files and Directories (15 minutes)
3. Working with Files and Directories (15 minutes)
  - Have students download and unzip a set of files for all human chromosomes (they have 21) - will be used later
  - [Data](https://github.com/darencard/2016-12-09-ucsf_Python/blob/gh-pages/workshop/01_day/01_pm/data/human_window_stats_sab.zip?raw=true)
4. *Break*
5. Filters, redirection, and pipes (15 minutes)
  - As in Nelle's pipeline, there will be some files that are messed up (different length), which will be obvious when they start sorting data by length
  - They'll need to fix these issues with the data before running their shell script
  - Here are the problems to fix:
    1. `human chr4.txt` should be `human_chr4.txt` for consistency (`mv`)
    2. `human.chr16.txt` should be `human_chr16.txt` for consistency (`mv`)
    3. `human_chr1.txt` contains data for chr1, chr10, and chr11 (but not in order). Demonstrates a common wild-card issue that people encounter. Need to use `sort` and `head`/`tail` to separate out. `human_chr10.txt` and `human_chr11.txt` files are fine, so can overwrite them or just delete proper lines in `human_chr1.txt`
      - Create backup (`mv human_chr1.txt backup.human_chr1.txt`)
      - Try a naive sort (`sort`) -- Why doesn't this work? (Because it's sorting by the whole column)
      - Sort by indicating the key (`sort -k 1,1`)
        - `-s` indicates a "stable" sort; i.e. the order of things that are not explicitly labelled as the key is preserved.
      - Copy first 20 entries (`head -n 20 >`)
      - Copy last 20 entries (`tail -n 20 >`)
      - Copy middle 20 entries (`head -n -20 | tail -n 20`)
    4. `human_chrSex.txt` contains information about the `X` and `Y` chromosomes, but pasted side by side. Need to use `cut` to extract each into `human_chrX.txt` and `human_chrY.txt`, and delete the original.
6. Loops (15 minutes)
  - After introducting, will have students run their python script and produce a set of output plots comparing a couple stats for each chromosome file
7. Shell Scripts (15 minutes)
  - Work the for loop into a nice script that they can save, which automates their analysis. They'll keep this shell script and their Python script for the later Git lesson
8. Finding Things (15 minutes)
  - Searching inside files with `grep`
    * Play around by doing `echo 'phrase' | grep 'pattern'`
      - Also, create some files to play with
    * Alternative way to fix `chr1/10/11` mixup is with `grep 'chr10'`
      - But, can't do `grep 'chr1'`, which leads nicely to...
    * Introduce some basic regular expressions
      - Character expressions: `[]`, `.`, `^`, `$` `\b`
      - Modifiers: `?`, `+`, `*`, `{m,n}`
      - Alternation with `|`
      - Grouping with `()`
      - [Complete regex table](http://userguide.icu-project.org/strings/regexp)
    * Alternative way to do `human_chrSex.txt` processing above is to search for `chrY` in the file: `grep -o ... > `
  - Finding files with `find`
    * Basic searching: 
      - By name -- `-name wildcard`
      - By path -- `-path wildcard` 
    * Advanced searching:
      - By modified time (minutes/days) -- `-mmin/-mtime +/-n`
      - Empty files -- `-empty`
      - Size -- `-size <size>c` (effectively the number of "characters" in a file plus one)
    * Performing actions on found files:
      - Arbitrary command -- `-execdir command {} \;`
      - Deletion (be _very_ careful with this) -- `-delete`
  - Once they've cleaned their data and corrected issues, we'll have them concatenate all chromosome data together into one file, for later work in Python in Day 2.
  - Can use this combined dataset to play around with things like grep, and can also introduce cut/sort/uniq/etc.
