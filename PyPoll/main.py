#!/usr/bin/env python
# coding: utf-8

# In[104]:


# Dependencies
import os
import csv


# In[105]:


# Load in file
dat_path = os.path.join('Resources', 'election_data.csv')

num_votes = int(0)
cand_list = []
    
with open(dat_path, newline='') as raw_dat:
    raw_read = csv.reader(raw_dat, delimiter = ',')
    raw_header = next(raw_read)
    for row in raw_read:
        num_votes = num_votes + 1
        
        if  row[2] not in cand_list :
            cand_list.append(row[2])
            


# In[106]:


num_cand = len(cand_list)


# In[107]:


vote_count = [0] * (num_cand)
vote_perc = [0] * (num_cand)


# In[108]:


with open(dat_path, newline='') as raw_dat2:
    raw_read2 = csv.reader(raw_dat2, delimiter = ',')
    raw_header2 = next(raw_read2)
    for row in raw_read2:
        cand_name = row[2]
        for cand in cand_list: 
            cand_id = cand_list.index(cand)
            if cand_name == cand_list[cand_id]:
                vote_count[cand_id] = vote_count[cand_id] + 1
                

                
        


# In[109]:


for cand in cand_list: 
    cand_id = cand_list.index(cand)
    vote_perc[cand_id] = vote_count[cand_id] / num_votes
    


# In[110]:


max_perc = 0
for perc in vote_perc:
    if perc > max_perc:
        max_perc = perc
        winner_id = vote_perc.index(perc)


# In[111]:


print('Election Results')
print('-----------------------')
print('Total Votes:  ', '{:,.0f}'.format(num_votes))
for x in range(0, num_cand):
    print(cand_list[x], ' ', '{:.2%}'.format(vote_perc[x], ' (','{:,.0f}'.format(vote_count[x]),')'))
    
print('-----------------------')
print('Winner:  ', cand_list[winner_id])


# In[112]:


res_path = os.path.join('Resources', 'election_res.txt')
with open(res_path, 'a') as f:
    print('Election Results', file=f)
    print('-----------------------', file=f)
    print('Total Votes:  ', '{:,.0f}'.format(num_votes), file=f)
    for x in range(0, num_cand):
        print(cand_list[x], ' ', '{:.2%}'.format(vote_perc[x], ' (','{:,.0f}'.format(vote_count[x]),')'), file=f)
    print('-----------------------', file=f)
    print('Winner:  ', cand_list[winner_id], file=f)

