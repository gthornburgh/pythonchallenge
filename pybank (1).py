#!/usr/bin/env python
# coding: utf-8

# In[8]:


# add modules
import os
import csv

# import budget data
budget_data = os.path.join("budget_data.csv")

# read budget data csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:

# store in lists
total_PnL = []
PnL = []
PnL_Delta = []

# define variables
count = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

# calc profits
total_PnL = total_PnL + init(row[1])

PnL.append(init(row[1]))

for value to len(PnL):

delta_PnL = PnL[index+1] - value


final_profit = init(1)
monthly_change_profit = final_profit - initial_profit


average_change_profit = (total_change_profit/count)

max_profit = max(change_profit)
min_profit = min(change_profit)

# print 
print("---------------------------------")
    print("Financial Analysis")
    print("---------------------------------")
    print("Total Months: " + str(count))
    print("Total Profits: " + "$" + str(total_profit))
    print("---------------------------------")
   

# text
with open('pybank_analysis.txt', 'w') as text:
    text.write("---------------------------------\n")
    text.write("Financial Analysis"+ "\n")
    text.write("---------------------------------\n")
    text.write("Total Months: " + str(count)+ "\n")
    text.write("Total Profits: " + "$" + str(total_profit)+ "\n")
    text.write("---------------------------------\n")