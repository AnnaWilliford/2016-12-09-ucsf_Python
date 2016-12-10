# Introduction to Shell

# Learning objectives
After completing this session, learners should be able to:
- Replicate standard movement and actions (view, copy, and move files) from graphical file managers (e.g. Windows Explorer, OSX File Manager) in the shell.
- Understand that standard shell commands deal exclusively with raw text, and realize the implications of this information for chaining commands.
- Combine simple shell commands using pipes to create more complex actions.
- Standardize and automate data analysis workflows using loops.
- Store sequences of commands as scripts for reusable data processing.

1. Introducing the Shell (5 minutes)
  - Why use the shell?
    - The Unix philosophy -- tools that do one thing, but do it well, and work well with each other. Whereas traditional GUIs can do lots of things, but are fundamentally limiting, chained shell programs can be strung together in a virtually limitless number of ways.
    - Reproducibility -- In general, the same command executed the same way will do the same thing every time.
    - Automation -- Hand-in-hand with reproducibility
    - Power -- small programs with well-defined purpose can be combined to do anything you want
    - Ubiquity -- The command line is the default way to interact with computers systems, especially super-computers.

2. Navigating Files and Directories (15 minutes)
  - How to tell a prompt (not `>`)
  - Read, Evaluate, Print, Loop (REPL)
  - Where are you? `pwd`
  - Directories and the file system
    - Root directory `/`
    - Each directory level separated by a `/`
    - Home directory -- isolated so that you don't mess with system files; in general, you should try to do your work in here. Other parts of the system are usually restricted for security.
  - What is here? `ls`
    - Show directories -- `ls -F`
    - `-X` is the standard way of passing bash arguments. Many core Unix commands have single dash options which are only one character long and can be combined with the same dash (`-lt`) and longer flags preceded by double dashes (`-F` is the same as `--classify`) (though this is not true of all commands, e.g. `find`)
    - `<command> -h/--help` to learn about a program's options and function. 
    - `man command` to view full documentation (may not work on Windows systems)
  - `ls -f <dir>` -- List contents of a particular directory
    - Relative vs absolute directory paths
    - Hidden directories (start with `.` -- show with `ls -a`)
    - Special directories `.` (current) and `..` (parent)
  - Moving around -- `cd`
    - Get home with `cd` with no arguments
  - Shell shortcuts
    - Browse previous commands with arrows
    - Complete command, file, and directory names with TAB

3. Working with Files and Directories (15 minutes)
  - Create directory with `mkdir`
  - Avoid spaces and prefer lowercase in directory names
  - Create files with command-line text editor. I will use `nano`.
    - Some nano basics. Give people a minute to get acquainted.
    - Shoutout to vim (and emacs, but explain why I prefer vim)
    - Discussion of ***plain text*** editors -- _not_ Word/Pages/etc.
      - Can use non-CLI ones for larger editing if they prefer, but it is faster/more convenient to make small changes from the command line (generally a good skill)
  - Copy files with `cp <from> <to>`
    - If `to` is a directory, copy file inside of there with the same name.
    - If `to` is a filename, create a file with that name and copy to it
    - `from` can be longer than 1, but if that's the case, `to` has to be a directory
  - Move _or_ rename files with `mv`
    - Note that to Unix, this is effectively the _same operation_. 
    - Also can be a dangerous operation -- `mv` will *silently overwrite files with the same name*
  - Deleting files with `rm`
    - Standard `rm` caveats -- "deleting is forever"
    - Some people map `rm` to `rm -i` to prompt deletion; may be a good thing to do starting out.
    - Doesn't work on directories as a safeguard. `rmdir` is a separate command that only works on empty directories. To recursively remove things, do `rm -r`
  - Have students download and unzip a set of files for all human chromosomes (they have 21) - will be used later
    - [Data](https://github.com/darencard/2016-12-09-ucsf_Python/blob/gh-pages/workshop/01_day/01_pm/data/human_window_stats_sab.zip?raw=true)

**Break**

4. Filters, redirection, and pipes (15 minutes)
  - Redirection with `>` -- basic example using `wc`
  - Introduce the `sort` command on the output of `wc -l`
  - Introduce the `head` and `tail` commands
  - Chain together with pipes -- `wc -l | sort -n | head -n 1`
  - As in Nelle's pipeline, there will be some files that are messed up (different length), which will be obvious when they start sorting data by length
  - They'll need to fix these issues with the data before running their shell script
  - Need to fix the following problems in the provided files using the commands available: 
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
      - Cut by field -- `cut -f <n>-<m>`
      - Mention that you can also cut by character -- `cut -c`

5. Loops (15 minutes)
  - Introduce bash variables -- `x='hi'`; access with `$x`
  - Introduce bash separator; by default, it's a space
    - Implicit in previous commands (`cp`, `mv`, `ls`) 
  - `for` loop also looks for a list -- `for <varname> in <list>; do <command> $<varname>`
  - Writing `for` loops interactively -- pay attention to the prompt!
    - Escape with `Ctrl-C`
  - After introducting, will have students run their python script and produce a set of output plots comparing a couple stats for each chromosome file

6. Shell Scripts (15 minutes)
  - Scripts are just sequences of commands
  - Basic examples with `echo`
    - Execute a script with `bash script.sh`
  - Arguments
    - Specific argument position `$1`
    - All arguments `$@`
  - Comments -- start with `#`
  - `history` makes life easier
    - Browse history with `history`: `-<n>` specifies how many entries back to go, `<n>` (no dash) specifies where to start printing
    - Convert your last few commands into a bash script -- `history -<n> > script.sh` 
  - Create a script containing the loop to run the Python analysis -- `for f in "$@"; do python "$f"; done`
  - Create a script to concatenate all chromosome data into one file (for use in Python day 2)
    - Introduce the `cat` command
    - `for f in human_chr{?,??}.txt; do cat "$f" >> all_chr.txt; done`

7. Finding Things (15 minutes)
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
  - (Time-permitting) Other commands:
    - `uniq`
    - `sed`
