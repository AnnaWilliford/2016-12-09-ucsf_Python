# Introduction to Python

## Learning Objectives
- Transition from common layman methods of analyzing and plotting data (e.g., Excel) to Python.
- Realize the importance of properly recording data.
- Understand the basics of data types and structures for Python.
- Master assigning values to variable names for manipulation.
- Learn to import a data table into Python using `Pandas` and summarize it.
- Learn to make basic plots of data using `matplotlib`.

## Starting in Excel
Excel has long been the *de facto* data analysis tool for most people due to its easy-to-understand graphical user interface (GUI) and ability to manipulate and analyze tabular data. We'll begin with a dataset in Excel to forge a connection with most users before moving our data into Python. Begin by downloading the the [Excel dataset for Human chromosome 21](https://github.com/darencard/2016-12-09-ucsf_Python/blob/gh-pages/workshop/01_day/01_am/data/human_chr21_broken.xlsx?raw=true) and open it in Excel. This dataset includes several genomic measures for 20 equal-sized windows in Human chromosome 21: number of ambiguous bases, number of G or C bases, number of bases from exons, number of bases from simple repeats, and number of bases from complex repeats.

One should be accustomed to viewing data in this format. A few pieces of data are quite conspicuous, as they are encoding in a manner that isn't consistent with the rest of the data. These issue highlight the fact that data is often messy and can be prone to error during collection or can be poorly currated. To combat this, one should take care when collecting and storing data, and should be wearly of data collected by others.

Correct the following issues with the dataset (0-indexed row(s): column(s)):

1. 0:1-2 - both headers are 'window', but should be 'window_start' and 'window_end'
2. 2:5-7 - various encodings of missing data, standardize to 'NA'
3. 9:3 - 0 (the number) encoded as O (the letter)
4. 15:0 - should be 'chr1' instead of 'chr_1'
5. 2,14:8 - spurious commment that should be deleted
6. 22:3 - spurious comment that should be deleted

One major shortcoming of Excel is that it stores data in a proprietary binary data format, which typically cannot be ready by other applications. Data analysis that leverages languages like Python relies on simple text files to encode data. Therefore, to move forward with Python, we need our data in this type of format. Excel allows us to save text files of our data, so users should create an appropriate text file of their fixed dataset by clicking `File`, `Save As`, and selecting `Comma Separated Values (.csv)` under `Format` in the `Save As` box. This file should be saved as `human_chr21.csv` in a Desktop directory called `swc_dec2016`.

The choosen file and directory names highlight another best practice that should be following when analyzing data: do **not** place spaces in file names or directories, or anywhere in data files, as these characters can sometimes confuse data analysis software and lead to big headaches.

Now that we have a plain text version of our data, we can get started with Python.

## Getting Started with Python and Jupyter Notebooks

We will be interacting with Python using an interface called Jupyter, which provides a GUI feel and several other nice features. Jupyter allows users to create notebooks, which store chunks of code alongside images, text, etc., and allows users to interactively work with Python. To open a Jupyter notebook, open your Terminal and enter the following:
```shell
jupyter notebook
```

A new window or tab will open in your internet browser and you will be greeted with a list of the contents of your current working directory. You'll also see some other tabs and buttons, but we will not be working with most of those. Let's first navigate to our `swc_dec2016` directory on the Desktop. You should see the `human_chr21.csv` file. Now, in the upper right corner click on the `New` button and under `Notebooks` click on `Python 3`. This will open a new window or tab where we will do most of our work. First, let's save our new Python notebook as `day1_python_intro` by clicking the `Untitled` text near the Jupyter icon at the top of the page. Below this, you will see a number of GUI elements that should be relatively familiar, and others that we will begin by exploring.

1. The `Save` disk icon will allow you to save changes, and should be used often.
2. The `+` icon allows you to add more blocks to the notebook space below (you'll see one already there).
3. You'll see `Cut`, `Copy`, and `Paste` icons to manipulate text.
4. The `Up` and `Down` arrow icons allow you to move through blocks on the notebook.
5. The `Run` botton icon allows you to execute the code within a block.

There are shortcut keystrokes for buttons in Jupyter, like other GUIs, which will save lots of time, so it is worth learning them.

## Introduction to Python built-in data types

### Strings, integers and floats

The most basic data types in Python are strings, integers and floats:

```python
text = "Data Carpentry"
number = 42
pi_value = 3.1415
```

Here we've assigned data to variables, namely `text`, `number` and `pi_value`,
using the assignment operator `=`. The variable called `text` is a string which
means it can contain letters and numbers. We could reassign the variable `text`
to an integer too - but be careful reassigning variables as this can get 
confusing.

To print out the value stored in a variable we can simply type the name of the
variable into the interpreter:

```python
>>> text
"Data Carpentry"
```

however, in scripts we must use the `print` function:

```python
# Comments start with #
# Next line will print out text
print(text)
"Data Carpentry"
```

### Operators

We can perform mathematical calculations in Python using the basic operators
 `+, -, /, *, %`:

```python
>>> 2 + 2
4
>>> 6 * 7
42
>>> 2 ** 16  # power
65536
>>> 13 % 5  # modulo
3
```

We can also use comparison and logic operators:
`<, >, ==, !=, <=, >=` etc.
`and, or, not`

```python
>>> 3 > 4
False
>>> True and True
True
>>> True or False
True
```

### Challenge

Let's assign a number to a variable and then perform a math operation.

1. First, assign the number `7` to the variable `a`.
2. Now multiple variable `a` by `4` and store the result as a new variable, `b`.

## Sequential types: Lists and Tuples

### Lists

**Lists** are a common data structure to hold an ordered sequence of
elements. Each element can be accessed by an index:

```python
>>> numbers = [1,2,3]
>>> numbers[0]
1
```

A `for` loop can be used to access the elements in a list or other Python data
structure one at a time:

```python
for num in numbers:
    print(num)
1
2
3
```

**Indentation** is very important in Python. Note that the second line in the
example above is indented. This is Python's way of marking a block of code. We will
discuss this in more detail later.

To add elements to the end of a list, we can use the `append` method:

```python
>>> numbers.append(4)
>>> print(numbers)
[1,2,3,4]
```

Methods are a way to interact with an object (a list, for example). We can invoke 
a method using the dot `.` followed by the method name and a list of arguments in parentheses. 
To find out what methods are available for an object, we can use the built-in `help` command:

```python
help(numbers)

Help on list object:

class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 ...
```

We can also access a list of methods using `dir`. Some methods names are
surrounded by double underscores. Those methods are called "special", and
usually we access them in a different way. For example `__add__` method is
responsible for the `+` operator.

```python
dir(numbers)
>>> dir(numbers)
['__add__', '__class__', '__contains__', ...]
```

### Tuples

A tuple is similar to a list in that it's an ordered sequence of elements. However,
tuples can not be changed once created (they are "immutable"). Tuples are
created by placing comma-separated values inside parentheses `()`.

```python
# tuples use parentheses
a_tuple= (1,2,3)
another_tuple = ('blue','green','red')
# Note: lists use square brackets
a_list = [1,2,3]
```

### Challenge
1. What happens when you type `a_tuple[2]=5` vs `a_list[1]=5` ?
2. Type `type(a_tuple)` into python - what is the object type?


## Dictionaries

A **dictionary** is a container that holds pairs of objects - keys and values.

```python
>>> translation = {"one" : 1, "two" : 2}
>>> translation["one"]
1
```
Dictionaries work a lot like lists - except that you index them with *keys*. 
You can think about a key as a name for or a unique identifier for a set of values
in the dictionary. Keys can only have particular types - they have to be 
"hashable". Strings and numeric types are acceptable, but lists aren't.

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[1]
'one'
>>> bad = {[1,2,3] : 3}
...
TypeError: unhashable type: 'list'
```

To add an item to the dictionary we assign a value to a new key:

```python
>>> rev = {1 : "one", 2 : "two"}
>>> rev[3] = "three"
>>> rev
{1: 'one', 2: 'two', 3: 'three'}
```

### Challenge
Can you do reassignment in a dictionary? Give it a try. 

1. First check what `rev` is right now (remember `rev` is the name of our dictionary). 
    
    Type:
`>>> rev`

    You should see the following output:
`{1: 'one', 2: 'two', 3: 'three'}`
2. Try to reassign the second value (in the *key value pair*) so that it no longer reads "two" but instead reads "apple-sauce". 
`>>> rev[2] = "apple-sauce"`
3. Now display `rev` again to see if it has changed; you should see the following:
`{1: 'one', 2: 'apple-sauce', 3: 'three'}`

It is important to note that dictionaries are "unordered" and do not remember the
sequence of their items (i.e. the order in which key:value pairs were added to 
the dictionary). Because of this, the order in which items are returned from loops
over dictionaries might appear random and can even change with time.

## Working with Data in `Pandas`
A lot of powerful, general tools are built into languages like Python, but specialized tools built up from these basic units live in libraries that can be called upon when needed. In order to import our data into Python for analysis, we need to access, or `import` in Python lingo, a library called `Pandas`. We can do this by issuing the following in a code block:
```python
import pandas
```

Another important thing to point out is that built-in Python functions and library functions have associated help pages, which give a description of the function and the options available to the user. You can view the general help page for `Pandas` by issuing the following command:
```python
help(pandas)
```

You'll see some general information about `Pandas`. This tool is really designed for providing help with individual functions, and as a beginner you will be using them a lot, so take a look at the help pages for the functions you call below as you work through the rest of this lesson.

`Pandas` is a library for manipulating dataframes. A dataframe is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, factors and more) in columns. It is similar to a spreadsheet or an SQL table or the data.frame in R. A dataframe always has an index (0-based). An index refers to the position of an element in the data structure.

`Pandas` has useful functions (or commands) that can be used to import our plain text data file.
```python
# read data in from our csv file
human_chr21 = pandas.read_csv("human_chr21.csv")
```

We've read this dataframe into a logical variable. We can print its contents by issuing the following command:
```python
print(human_chr21)
```

Which gives us the following output:
```python
   chromosome  window_start  window_end  n_bases  gc_bases  exon_bases  \
0       chr21             0     2335499  2335499         0         NaN   
1       chr21       2335499     4670998  2335499         0         NaN   
2       chr21       4670998     7006497   889002    648702    253805.0   
3       chr21       7006497     9341996   600001    729820    154932.0   
4       chr21       9341996    11677495   350800    778829     41904.0   
5       chr21      11677495    14012994    50400    889396     12672.0   
6       chr21      14012994    16348493        0    867338    270654.0   
7       chr21      16348493    18683992        0    867175    190141.0   
8       chr21      18683992    21019491        0    822404     11697.0   
9       chr21      21019491    23354990        0    809656     86625.0   
10      chr21      23354990    25690489        0    839298     55946.0   
11      chr21      25690489    28025988        0    880857    254203.0   
12      chr21      28025988    30361487        0    890511    197183.0   
13      chr21      30361487    32696986       30    979741    339787.0   
14      chr21      32696986    35032485        0   1016543    668592.0   
15      chr21      35032485    37367984        0   1009754    530783.0   
16      chr21      37367984    39703483       10    995639    641001.0   
17      chr21      39703483    42038982      103   1029888    489845.0   
18      chr21      42038982    44374481    50020   1172446    909833.0   
19      chr21      44374481    46709983    10000   1183628   1041644.0   

    simple_rep_bases  complex_rep_bases  
0                NaN                NaN  
1                NaN                NaN  
2           154999.0           631392.0  
3           345062.0           740985.0  
4          1617305.0           497476.0  
5          1836309.0           508445.0  
6            41741.0          1048889.0  
7            29885.0          1194210.0  
8            43919.0          1151173.0  
9            45584.0          1142404.0  
10           41427.0          1128161.0  
11           33249.0          1091910.0  
12           36281.0          1080532.0  
13           42324.0          1105190.0  
14           33233.0          1036531.0  
15           33519.0          1093246.0  
16           39385.0          1038114.0  
17           49423.0          1009580.0  
18           58130.0           913144.0  
19           54193.0           937997.0  
```

Notice that the 'NA' values we encoded in Excel have been changed to `NaN`, the standard value Python uses to encode missing data.

We can also convince ourselves that our data is stored in a dataframe object.
```python
type(human_chr21)
# output
pandas.core.frame.DataFrame
```

Let's begin by summarizing the data a bit. It is always good to know what data types exist in each column of your dataframe.
```python
human_chr21.dtypes
# output
chromosome            object
window_start           int64
window_end             int64
n_bases                int64
gc_bases               int64
exon_bases           float64
simple_rep_bases     float64
complex_rep_bases    float64
dtype: object
```

We can also look at what the column names are.
```python
human_chr21.columns.values
# output
array(['chromosome', 'window_start', 'window_end', 'n_bases', 'gc_bases',
       'exon_bases', 'simple_rep_bases', 'complex_rep_bases'], dtype=object)
```

Or the unique window start positions in our dataset.
```python
pandas.unique(human_chr21['window_start'])
# output
array([       0,  2335499,  4670998,  7006497,  9341996, 11677495,
       14012994, 16348493, 18683992, 21019491, 23354990, 25690489,
       28025988, 30361487, 32696986, 35032485, 37367984, 39703483,
       42038982, 44374481])
```

Let's say we are interesting in summarizing the data in a particular column. We can issue the following to summarize how many G or C bases are found in each window.
```python
human_chr21['gc_bases'].describe()
# output
count    2.000000e+01
mean     8.205812e+05
std      3.106788e+05
min      0.000000e+00
25%      8.019492e+05
50%      8.740975e+05
75%      9.991678e+05
max      1.183628e+06
Name: gc_bases, dtype: float64
```

Finally, it is also possible to perform arithmetic on one or more columns of the dataset.
```python
# let's translate the window start from bp to Mbp.
human_chr21['window_start']/1000000
# output
0      0.000000
1      2.335499
2      4.670998
3      7.006497
4      9.341996
5     11.677495
6     14.012994
7     16.348493
8     18.683992
9     21.019491
10    23.354990
11    25.690489
12    28.025988
13    30.361487
14    32.696986
15    35.032485
16    37.367984
17    39.703483
18    42.038982
19    44.374481
Name: window_start, dtype: float64
```

### Challenge
Right now all values are reported as the number of bases that meet a condition. Translate each of these values to a proportion out of the total window size.
```python
# calculate the window size
window_size = human_chr21['window_end']-human_chr21['window_start']
human_chr21['gc_bases']/window_size
# output
0     0.000000
1     0.000000
2     0.277757
3     0.312490
4     0.333474
5     0.380816
6     0.371372
7     0.371302
8     0.352132
9     0.346674
10    0.359366
11    0.377160
12    0.381294
13    0.419500
14    0.435257
15    0.432350
16    0.426307
17    0.440971
18    0.502011
19    0.506798
dtype: float64
```

See if you can also do this as a single command and save it to an appropriate variable, like `gc_content`.

## Plotting Data using `matplotlib`

Aside from performing operations on pieces of data, Python is also very useful for plotting the data or the results of analyses. The most common library used for plotting in Python is `matplotlib`, which is what we will use to make some plots of our data. Remember, in order to use non-built-in libraries, you must `import` them. We are going to work with a specific subset of the `matplotlib` library called `pyplot`.
```python
import matplotlib.pyplot as plt
```

Note how we imported `pyplot` as `plt`. This allows us to use the shorter string of characters when calling plotting functions and is similar to assigning the library to a variable for future use.

When we started with our dataset, the first thing we did was summarize it to determine the mean, median, standard deviation, etc. We can visualize similar information using plots, like a boxplot. Let's create a boxplot of our `gc_content` data that we created in the above challenge.
```python
plt.boxplot(gc_content)
```

This creates a simple boxplot of our GC content. However, notice that the x-axis lacks much information about what the data are. By looking at the contents of `help(plt.boxplot)`, we determine that we can pass alist to `labels` to provide more content.
```python
plt.boxplot(gc_content, labels=["GC Content"])
```

We can also plot a histogram of the data to see the frequency of certain levels of GC content.
```python
plt.hist(gc_content)
# or to create more bins
plt.hist(gc_content, bins=20)
```

Those two plots provided a lot of information about one piece of data in our dataset. However, we are probably interested in visualizing the relationship between a couple pieces of data. For instance, it has been established that regions of genomes with more genes typically have higher GC content. We can see if that trend appears in our data.
```
# first we need to calculate the gene content per window
gc_content = human_chr21['gc_bases']/(human_chr21['window_end']-human_chr21['window_start'])
# now we can plot, using 'o' to create a scatter plot of points
plt.plot(gene_content, gc_content, 'o')
```

Generally, it does appear that GC content rises as gene content increases. However, you are probably noticing that this plot leaves a lot to be desired. Where are the axis labels and title? We can add those pretty easily by adding the following lines and executing the code block.
```python
plt.xlabel('Gene Content')
plt.ylabel('GC Content')
plt.title('Are genes more GC rich?')
```

## Building a Python Script
What we have done so far has demonstrated the utility of Python for interactive data analysis. However, Python can also be used for more passive, automated work by creating what is called a `script`. Scripts are a series of Python commands that are executed on one or more files. Let's learn how to make our first script.

### Challenge
We'll begin by laying out the series of commands that are going to analyze our dataset of interest. First, save the current Jupyter notebook and open a new one, like before. You can name this one `gc_repeat_plot`. As the name implies, this is a script that reads in the dataset we're working with, calculates the proportion of complex repeat content and GC content per window, and then plots the relationship between these two variables, saving the plot to an appropriately named PNG file. Given what we've covered so far, you should be able to construct this series of commands. You can also use the `help()` function to see other plotting options available to customize your plot. You can also test commands as you go and make sure that this works as planned. It is also good practice to use comments (`#`) to describe what your code is doing.

```python
import pandas as pd
import matplotlib.pyplot as plt

# read data in from our csv file
human_chr21 = pd.read_csv("human_chr21.csv")

# calculate GC content per window
gc_content = human_chr21['gc_bases']/(human_chr21['window_end']-human_chr21['window_start'])

# calculate complex repeat content per window
repeat_content = gc_content = human_chr21['complex_rep_bases']/(human_chr21['window_end']-human_chr21['window_start'])

# plot the results, saving to appropriate file
plt.plot(repeat_content, gc_content, 'o')
plt.xlabel('Proportion Repeat Content')
plt.ylabel('Proportion GC Content')
plt.title('Are repetitive regions more GC-rich?')

# save result to .png image file
plt.savefig('repeats_vs_gc.png')
```

And now you have your first data analysis script. You can run all cells by clicking on `Run All` under the `Cells` menu, and you'll see them all execute properly.

By now, maybe you are noticing the downside to this script: it isn't very flexible. We've restricted it to working only on one data file in one way. There are ways we can build in more flexibility, such that we can specify any appropriately-formated dataset to analyze. Then we can run our script from the command line, specifying the proper input(s), and automate our work. Let's show you how to do this.

The key to solving this problem is passing a file to Python for analysis. The Python library that is used to read file names, or any other input information, is called `sys`, which is short for system. As with other libraries, we first have to import the library.
```python
import sys
```

We call the data files or other information we pass to Python scripts 'arguments'. These arguments are passed automatically to a list, in the order they are received, and by subsetting our list properly we can insert the proper information in the proper location in our script. We can pass any number of arguments using `sys`, as follows:
```python
# first argument (remember Python numbering begins at 0)
sys.argv[0]
# second argument
sys.argv[1]
```

Therefore, if we want to pass our data file to our Python script as the first argument, we must make a change to the portion of the script where the data is read.
```python
# pass the file name to the Pandas input command
# note we don't need the quotes because our variable is a string of the file name
human_chr21 = pd.read_csv(sys.argv[0])
# or we may prefer to store our agument as an appropriate variable 
# and then pass to the command
input_file = sys.argv[0]
human_chr21 = pd.read_csv(input_file)
```

We should also probably build flexibility into the output plot file name as well, so we aren't continually overwriting previous plots.
```python
# join input file name with ".png"
# pass tuple to "".join()
plt.savefig(''.join((sys.argv[0],'.png')
```

There, now we have an operational script where we can use any chromosome file like `human_chr21.txt` as input to create a plot.

You should save your Jupyter notebook with this script. However, you may have already noticed that this notebook isn't plain text, and therefore we wouldn't be able to run our script in the command line. We should export a plain text version of our python script by clicking `File`, `Download As`, and `Python (.py)`. This will initiate a download from your browser called `gc_repeat_plot.py`, and you can open this in a text editor and see it is a plain text representation of what you coded. Store this in your `swc_dec2016` directory.

### Challenge
We've built a bit of flexibility into our script, but we could go further. Create a script that allows you to explicitely pass an output file name as an additional argument, rather than having it automatically created based on the input file name. If you are up to the challenge, you can also code in flexibility that allows you to specify which columns of the dataset to analyze, so the script will plot more than just the relationship between GC content and complex repeat element content.
