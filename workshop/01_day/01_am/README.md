# Introduction to Python

## Learning Objectives
- Transition from common layman methods of analyzing and plotting data (e.g., Excel) to Python.
- Realize the importance of properly recording data.
- Understand the basics of data types and structures for Python.
- Master assigning values to variable names for manipulation.
- Learn to import a data table into Python using `pandas` and summarize it.
- Learn to make basic plots of data using `matplotlib`.

## Starting in Excel
Excel has long been the de facto data analysis tool for most people due to its easy-to-understand graphical user interface (GUI) and ability to manipulate and analyze tabular data. We'll begin with a dataset in Excel to forge a connection with most users before moving our data into Python. Begin by downloading the the [Excel dataset for Human chromosome 21]() and open it in Excel.

One should be accustomed to viewing data in this format. A few pieces of data are quite conspicuous, as they are encoding in a manner that isn't consistent with the rest of the data. These issue highlight the fact that data is often messy and can be prone to error during collection or poorly currated. To combat this, one should take care when collecting and storing data, and should be wearly of data collected by others.

Correct the following issues with the dataset (0-indexed row: column):

1. 0:1-2 - both headers are 'window', but should be 'window_start' and 'window_end'
2. 2:5-7 - various encodings of missing data, standardize to 'NA'
3. 9:3 - 0 (the number) encoded as O (the letter)
4. 15:0 - should be 'chr1' instead of 'chr_1'
5. 2,14:8 - spurious commment that should be deleted
6. 22:3 - spurious comment that should be deleted

One major shortcoming of Excel is that it stores data in a proprietary binary data format, which typically cannot be ready by other applications. Data analysis that leverages languages like Python relies on simple text files to encode data. Therefore, to move forward with Python, we need our data in this type of format. Excel allows text files to be saved of data files, so users should create an appropriate text file of their fixed dataset by clicking `File`, `Save As`, and selecting `Comma Separated Values (.csv)` under `Format` in the `Save As` box. This file should be saved as `human_chr21.csv` in a Desktop directory called `swc_dec2016`.

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
