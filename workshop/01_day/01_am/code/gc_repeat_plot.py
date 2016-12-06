
# coding: utf-8

# In[2]:

# import library
import pandas as pd
import matplotlib.pyplot as plt
import sys


# In[3]:

# read data from our txt file
human_chr21 = pd.read_csv(sys.argv[1], sep='\t')
print(sys.argv[1])


# In[13]:

#help(str.join)


# In[5]:

# calculate GC content per window
gc_content = human_chr21['gc_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])


# In[6]:

# calculate complex repeat content per window
repeat_content = human_chr21['complex_rep_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])


# In[9]:

# plot the result, saving to appropriate file
plt.plot(repeat_content, gc_content, 'o')
plt.xlabel('Proportion Repeat Content')
plt.ylabel('Proportion GC Content')
plt.title('Are repetitive regions GC rich?')
plt.savefig(''.join([sys.argv[1], '.png']))

