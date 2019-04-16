#!/usr/bin/env python
# coding: utf-8

# In[31]:


# Dependencies
import os
import csv


# In[32]:


# Load in file
dat_path = os.path.join('Resources', 'budget_data.csv')

# Initialize variables
num_rows = int(0)
balance = float(0)
prev_val = float(0)
max_change = float(0)
min_change = float(0)
change_sum = float(0)
change = float(0)

# Read in the CSV
with open(dat_path, newline='') as raw_dat:
    raw_read = csv.reader(raw_dat, delimiter = ',')
    raw_header = next(raw_read)
    for row in raw_read:    
        num_rows = num_rows + 1   # compute total number of rows aka months
        balance = balance + float(row[1])  # add profits and losses across months
        if num_rows >= 2: 
            change = float(row[1]) - prev_val  # compute changes from one month to the next
            change_sum = change_sum + change   # compute sum of all monthly changes--failure
        if change > max_change:            # track and hold maximum change
            max_date = row[0]
            max_change = change
        elif change < min_change:          # track and hold minimum change
            min_date = row[0]
            min_change = change
        prev_val = float(row[1])           # keep the value from the previous row to use for the next row            
avg_change = change_sum / (num_rows - 1)   # attempt to compute the average monthly change.  
        


# In[33]:


#  Print to Screen
print(f'Financial Analysis')
print('------------------------------------------------------------')
print(f'Total Months:  {num_rows}')
print('Net Gain or Loss:  ', '${:,.2f}'.format(balance))
print('Average Change Between Adjacent Days with Data:  ','${:,.2f}'.format(avg_change))
print('Greatest Increase in Profits: ', max_date, ' (', '${:,.2f}'.format(max_change), ')')
print('Greatest Decrease in Profits: ', min_date, ' (', '${:,.2f}'.format(min_change), ')')


# In[34]:


write_path = os.path.join('Resources', 'budget_report.txt')


# In[35]:


# Write to file
bud_path = os.path.join('Resources', 'budget_report.txt')
with open(bud_path, 'a') as f:
    print(f'Financial Analysis', file=f)
    print('------------------------------------------------------------', file=f)
    print(f'Total Months:  {num_rows}', file=f)
    print('Net Gain or Loss:  ', '${:,.2f}'.format(balance), file=f)
    print('Average Change Between Adjacent Days with Data:  ','${:,.2f}'.format(avg_change), file=f)
    print('Greatest Increase in Profits: ', max_date, ' (', '${:,.2f}'.format(max_change), ')', file=f)
    print('Greatest Decrease in Profits: ', min_date, ' (', '${:,.2f}'.format(min_change), ')', file=f)


# In[ ]:




