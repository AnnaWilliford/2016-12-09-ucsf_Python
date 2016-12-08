
# coding: utf-8

# In[2]:

# import library
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


# In[3]:

# read data from our txt file
human_chr21 = pd.read_csv("human_chr21.txt", sep='\t')


# In[5]:

# calculate GC content per window
human_chr21['gc_content'] = human_chr21['gc_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])


# In[6]:

# calculate complex repeat content per window
human_chr21['repeat_content'] = human_chr21['complex_rep_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])

lm = smf.ols(formula='gc_content ~ repeat_content', data=human_chr21).fit()


# In[9]:

# plot the result, saving to appropriate file
plt.plot(human_chr21['repeat_content'], human_chr21['gc_content'], 'o')
plt.plot(human_chr21['repeat_content'].dropna(), lm.fittedvalues, 'b')
plt.xlabel('Proportion Repeat Content')
plt.ylabel('Proportion GC Content')
plt.title('Are repetitive regions GC rich?')
plt.savefig('repeats_vs_gc.png')

