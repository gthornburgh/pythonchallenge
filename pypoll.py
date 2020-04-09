#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


pypoll = "election_data.csv"


# In[5]:


pypoll_df = pd.read_csv(pypoll)
pypoll_df.head()


# In[27]:

# total votes per candidate
pypoll_df["Candidate"].value_counts()


# In[35]:

# total votes
pypoll_df.count


# In[67]:


# variables: total, candidate total
total = 3521001 
k = 2218231
c = 704200
l = 492940
o = 105630


# In[68]:


# variables: candidate percent of vote
kk = k/total
cc = c/total
ll = l/total
oo = o/total


# In[74]:


# print results
print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(total))
print("-----------------------------------")
print(("Kahn: ") + str(k) + ("   ") + str(kk))
print(("Correy: ") + str(c) + ("   ") + str(cc))
print(("Li: ") + str(l) + ("   ") + str(ll))
print(("O'Tooley: ") + str(o) + ("   ") + str(oo))
print("-----------------------------------")
print("Winner: Kahn")
print("-----------------------------------")


# In[78]:


with open('pypoll_analysis.txt', 'w') as text:
    text.write("Election Resulst\n")
    text.write("-----------------------------------\n")
    text.write("Total Votes: " + str(total) + "\n")
    text.write("-----------------------------------\n")
    text.write(("Kahn: ") + str(k) + ("   ") + str(kk) + "\n")
    text.write(("Correy: ") + str(c) + ("   ") + str(cc) + "\n")
    text.write(("Li: ") + str(l) + ("   ") + str(ll) + "\n")
    text.write(("O'Tooley: ") + str(o) + ("   ") + str(oo) + "\n")
    text.write("-----------------------------------\n")
    text.write("Winner: Kahn" + "\n")
    text.write("-----------------------------------\n")


# In[ ]:




