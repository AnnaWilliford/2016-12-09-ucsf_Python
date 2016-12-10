
# coding: utf-8

# # Data Processing and Visualization in Python
# 
# ## Creating our Dataset
# 
# We have our individual chromosome datasets, but let's make a full genome dataset by combining all chromosomes together.
# 1. Open a Shell
# 2. Navigate to the directory containing the raw data files
# 3. Concatenate the header with all of the individual chromosome files into a file called `human_full.txt`
# ```shell
# cat header.txt human_chr*.txt > human_full.txt
# ```

# ## Plotting using `ggplot`
# 
# - `ggplot` does not come with with `Anaconda`, but it is easy to install
# ```bash
# conda install -c conda-forge ggplot
# # -c means channel, which indicates the repository that conda will search
# # backup command
# # pip install -U ggplot
# ```
# - Open a new Jupyter notebook
# ```bash
# jupyter notebook
# # click on New -> Python3
# ```

# #### Let's read in our full dataset and calculate proportion GC content and gene content
# - first save the Jupyter notebook as `ggplot_plotting`

# In[1]:

import pandas as pd


# #### \~\~Challenge\~\~
# 1. Import `human_full.txt` using `pandas`
# 2. Calculate proportion GC content and gene content

# In[3]:

human = pd.read_csv("human_full.txt", sep="\t")
human.head()


# In[4]:

human['gc_content'] = human['gc_bases'] / (human['win_end'] - human['win_start'])
human['gene_content'] = human['exon_bases'] / (human['win_end'] - human['win_start'])


# #### Now we can begin learning how to plot using `ggplot`

# In[5]:

# must load package first
from ggplot import *


# In[7]:

# now let's create our first plot
p = ggplot(aes(x='gene_content',               y='gc_content'), data=human)
p
# but we only see a coordinate plot
# need to layer on our data


# In[8]:

p = ggplot(aes(x='gene_content',               y='gc_content'), data=human)
p + geom_point()
p


# In[10]:

# cool! but look at those ugly axis labels
p = ggplot(aes(x='gene_content',                y='gc_content'), data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p


# In[14]:

# awesome. but this represents all chromosomes
# how can we visualize with chromosomes... add color
p = ggplot(aes(x='gene_content',                y='gc_content', color='chromosome'),                data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p


# In[15]:

# or we can do it by shape
p = ggplot(aes(x='gene_content',                y='gc_content', shape='chromosome'),                data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p


# In[17]:

# we can also use lines instead of points
p = ggplot(aes(x='gene_content',                y='gc_content', shape='chromosome'),                data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p + geom_line()
p


# In[21]:

# problem here is that there are so many chromosomes
# that this is hard to interpret anything
# what if we could plot each separately
# can do this by subsetting and plotting
chr1 = human[human['chromosome'] == 'chr1']
chr1.tail()


# In[24]:

# now we can just plot chr1 as points
# let's add a title also
p = ggplot(aes(x='gene_content',                y='gc_content'),                data=chr1) + xlab("Gene Content") + ylab("GC Content") + ggtitle("Chromosome 1")
p + geom_point()
p


# In[25]:

# finally, what if we don't like this gray background
# we can use themes to change this
# a couple are built into ggplot
# we can do a simple 'black and white'
p = ggplot(aes(x='gene_content',                y='gc_content'),                data=chr1) + xlab("Gene Content") + ylab("GC Content") + ggtitle("Chromosome 1")
p + geom_point()
p + theme_bw()
p


# In[27]:

# there is a built in theme for xkcd
p = ggplot(aes(x='gene_content',                y='gc_content'),                data=chr1) + xlab("Gene Content") + ylab("GC Content") + ggtitle("Chromosome 1")
p + geom_point()
p + theme_xkcd()
p
# unfortunately, not many themes available for 
# ggplot in Python right now


# In[35]:

# one problem with subsetting is that it is more 
# labor intensive, or requires a loop
# ggplot can help us easily get around that
p = ggplot(aes(x='gene_content',                y='gc_content'), data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p + facet_wrap("chromosome")
p + theme_bw()
p


# In[44]:

## ggplot makes it easy to add trendlines too
p = ggplot(aes(x='gene_content',                y='gc_content'), data=human) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p + stat_smooth()
p + facet_wrap("chromosome")
p + theme_bw()
p


# In[41]:

# it appears that NaNs are creating issues with the lines
# can fix easily
# can also change color of lines
p = ggplot(aes(x='gene_content',                y='gc_content'), data=human.dropna()) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p + stat_smooth(color='royalblue')
p + facet_wrap("chromosome")
p + theme_bw()
p


# In[39]:

# or based on a linear model
p = ggplot(aes(x='gene_content',                y='gc_content'), data=human.dropna()) + xlab("Gene Content") + ylab("GC Content")
p + geom_point()
p + stat_smooth(method='lm', color='royalblue')
p + facet_wrap("chromosome")
p + theme_bw()
p


# - Have students save this file as `ggplot_plotting`

# ## Tidy Data and Analysis
# 
# - have went through a pretty full data processing workflow
# - let's say you show to your boss and he is pleased
# - but a collaborator just finished collecting the same type of data on chicken
# - he or she has stored the data up on GitHub
# - we need to download it and your boss wants to see the same type of plots with that dataset, which should be quick and easy
# - let's first download
# ```shell
# # move back to `swc_dec2012` directory
# git clone https://github.com/darencard/chicken.git
# ```
# - now the students should open a new Jupyter notebook called `chicken_analysis`
# 
# #### \~\~Challenge\~\~
# Load the chicken data into your notebook using 'pandas' and explore it briefly.

# In[45]:

import pandas as pd


# In[48]:

chicken = pd.read_csv("chicken_messy.txt", sep="\t")
chicken.head()


# - look at how ugly this data is
# - your collaborator has collected each piece of data in separate columns
# - data like this, which is very wide and typically has lots of columns and fewer rows is called *messy* data
# - you can compare it to the data we've been working with so far, which is considered *tidy* data
# - let's spend some time *tidying* these data

# In[50]:

# pandas provides some functionality that improves 
# things with a command called melt()
tidy_chicken = pd.melt(chicken, 
               id_vars='window', 
               var_name='statistic', 
               value_name='value')
tidy_chicken.head()


# In[51]:

# functions for the apply function
def parse_chr(s):
    return s.split("-")[0]
def parse_stat(s):
    return s.split("-")[1]


# In[52]:

# this has made our data 'long', which is more tidy
# but the statistic and the chromosome information 
# is still merged into one column
# we'll use another useful pandas 
tidy_chicken['chromosome'] = tidy_chicken['statistic'].apply(parse_chr)
tidy_chicken['stat'] = tidy_chicken['statistic'].apply(parse_stat)
tidy_chicken.head()


# In[56]:

# things still aren't ideal, tidier but not as ideal as our human dataset
# we have to use subset and joining to merge our genome
# characteristics so they are side-by-side for each chromosome/window
# lets do this with chr1 and win_start/win_end
win_start = tidy_chicken[tidy_chicken['chromosome'] == 'chr1']                [tidy_chicken['stat'] == 'win_start']
win_end = tidy_chicken[tidy_chicken['chromosome'] == 'chr1']                [tidy_chicken['stat'] == 'win_end']
win_end.head()


# In[68]:

# now we can merge the two together based on common data columns 
# chromosome and window
merge = win_start.merge(win_end, on=['window', 'chromosome'],                                 suffixes=['_start', '_end'])
merge.head()
# then we could trim out columns we don't want
merge.drop(['window', 'statistic_start', 'statistic_end',             'stat_start', 'stat_end'], axis=1, inplace=True)
#  and reorder
merge = merge[['chromosome', 'value_start', 'value_end']]
# and rename using a dictionary
merge.rename(columns={'value_start' : 'win_start',                       'value_end' : 'win_end'}, 
            inplace=True)
merge.head()


# - that's cool, but it would take forever to do on all chromosomes and statistics
# - using loops can help with this
# - let's plan this out with pseudocode as a Challenge

# In[69]:

# for each chromosome
    # for each statistic
        # merge statistics using 'chromsome' & 'window'
        # so they are side-by-side
    # concatenate each chromsome together top to bottom
# drop trash columns we don't need
# rename with appropriate headers


# In[71]:

# create chromosomes list
chromosomes = pd.unique(tidy_chicken['chromosome'])
chromosomes


# In[72]:

# create statistics list
statistics = pd.unique(tidy_chicken['stat'])
statistics


# In[73]:

# need counter for DataFrame initialization
chr_counter = 1
# for each chromosome
for chromosome in chromosomes:
    # print chromsome number to watch progress
    print(chromosome)
    # need another counter for DataFrame initialization
    stat_counter = 1
    # if this is the first chromosome we are analyzing
    if chr_counter is 1:
        # for each statistic
        for statistic in statistics:
            # if this is the first statistic
            if stat_counter is 1:
                # create a new chr DataFrame and add first statistic subset to it
                chr_df = tidy_chicken[tidy_chicken['chromosome'] == chromosome]                [tidy_chicken['stat'] == statistic][['chromosome','window','value']]
            # if this is beyond the first statistic
            else:
                # subset new statistic/chromosome
                new_df = tidy_chicken[tidy_chicken['chromosome'] == chromosome]                            [tidy_chicken['stat'] == statistic]
                # create a proper suffix for new stat
                suffix = ''.join(['_',statistic])
                # merge the full dataframe and this new stat subset
                chr_df = chr_df.merge(new_df[['chromosome','window','value']],                                       on=['window', 'chromosome'],                                       suffixes=['',suffix])
            # increase stat counter
            stat_counter += 1
        # once full set of stats from chromosome is together, initialize output dataframe
        full_df = chr_df
    # if this is beyond the first chromosome we are analyzing        
    else:
        # for each statistic
        for statistic in statistics:
            # if this is the first statistic
            if stat_counter is 1:
                # create a new chr DataFrame and add first statistic subset to it
                chr_df = tidy_chicken[tidy_chicken['chromosome'] == chromosome]                [tidy_chicken['stat'] == statistic][['chromosome','window','value']]
            # if this is beyond the first statistic
            else:
                # subset new statistic/chromosome
                new_df = tidy_chicken[tidy_chicken['chromosome'] == chromosome]                            [tidy_chicken['stat'] == statistic]
                # create a proper suffix for new stat
                suffix = ''.join(['_',statistic])
                # merge the full dataframe and this new stat subset
                chr_df = chr_df.merge(new_df[['chromosome','window','value']],                                       on=['window', 'chromosome'],                                       suffixes=['',suffix])
            # increase stat counter
            stat_counter += 1
        # once full set of stats from chromosome is together
        # concatenate to full output dataframe
        full_df = pd.concat([full_df, chr_df], ignore_index=True)
    # increase chromosome counter
    chr_counter += 1

# rename existing columns to make it consistent with human dataset
full_df.rename(columns={'value': 'win_start',                         'value_win_end': 'win_end',                         'value_n_bases': 'n_bases',                         'value_gc_bases': 'gc_bases',                         'value_exon_bases': 'exon_bases',                         'value_simple_rep_bases': 'simple_rep_bases',                         'value_complex_rep_bases': 'complex_rep_bases',                        }, inplace=True)
# delete the 'window' column because we don't need it
full_df.drop('window', axis=1, inplace=True)
# print result
print(full_df)


# #### \~\~Challenge\~\~
# Now that we have a chicken dataset, practice your `ggplot` plotting and make some appropriate plots. If you are feeling ambitious, you can also load in the human dataset and compare them in some way.

# ## Using Markdown to Narrate your Work
# - Jupyter notebooks are great for displaying commands and results in a notebook form that can be easily shared with others
# - However, often need more information to interpret the goals, methods, results, and conclusions of an analysis
# - 'Markdown' can be used to achieve this

# In[ ]:



