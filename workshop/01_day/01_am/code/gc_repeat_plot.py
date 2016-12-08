
# coding: utf-8

# In[2]:

# import library
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import sys


# In[3]:

# read data from our txt file
chr_data = pd.read_csv(sys.argv[1], sep='\t')
print(sys.argv[1])


# In[5]:

# calculate GC content per window
chr_data['gc_content'] = chr_data['gc_bases'] / (chr_data['win_end'] - chr_data['win_start'])


# In[6]:

# calculate complex repeat content per window
chr_data['repeat_content'] = chr_data['complex_rep_bases'] / (chr_data['win_end'] - chr_data['win_start'])


# In[ ]:

lm = smf.ols(formula='gc_content ~ repeat_content', data=chr_data).fit()


# In[9]:

# plot the result, saving to appropriate file
plt.plot(chr_data['repeat_content'], chr_data['gc_content'], 'ok')
plt.plot(chr_data['repeat_content'].dropna(), lm.fittedvalues, 'b')
plt.xlabel('Proportion Repeat Content')
plt.ylabel('Proportion GC Content')
plt.title('Are repetitive regions GC rich?')
plt.savefig(''.join([sys.argv[1], '.png']))

