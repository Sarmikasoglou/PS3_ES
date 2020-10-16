#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Problem 1 (5 pts):
#Write a script (or Jupyter Notebook code block)
#that opens the file, uses a for loop to read through the file line by line and reports the highest water level and the date and time that was observed.

import csv
FILE = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')     #open the file 

maxvalue = float(0)          #create a variable 
maxdate = ''                #create a variable 


for line in FILE:             #for loop in order to identify the largest level of water
        try:
            date = line.split(",")[0]     #for each line identify the date and time
            water = line.split(",")[1]     #for each line identify the level of water
            if float(maxvalue) < float(water):    #test if the value of this line is greater than the value from the initial value
                maxvalue = float(water)           #if yes, replace the initial value for the current value
                maxdate = date                  #if yes, replace the date and time for the current date and time

        except:
            continue
print(f'The highest water level is', maxvalue, 'at', maxdate)      #print the result


# In[ ]:


#Problem 2 (5 pts):
#Either in a new script or modifying the above script, calculate the lowest, highest and average water level observed during the time period.
#As above, print the date and time for the lowest and highest readings.

import pandas as pd  #read csv as pandas dataframe

df = pd.read_csv('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')
df.nlargest(1, [' Water Level']) #find the highest water level value and print entire line\n",


# In[ ]:


#Problem 2(lowest water level)
import csv
FILE = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')     #open the file 

minvalue = float(2)          #create a variable 
mindate = ''                #create a variable 


for line in FILE:             #for loop in order to identify the Lowest level of water
        try:
            date = line.split(",")[0]     #for each line identify the date and time
            water = line.split(",")[1]     #for each line identify the level of water
            if float(minvalue) > float(water):    #test if the value of this line is lower than the value from the initial value
                minvalue = float(water)           #if yes, replace the initial value for the current value
                mindate = date                  #if yes, replace the date and time for the current date and time

        except:
            continue
print(f'The lowest water level is', minvalue, 'at', mindate)      #print the result


# In[ ]:


#Alternative to previous script
df.nsmallest(1, [' Water Level']) #find the lowest water level value and print entire line\n",


# In[ ]:


#find the Average water level value and print entire line
df[' Water Level'].mean() #It's printing the value but there is a problem with rounding the value


# In[ ]:


#Problem 3 (5 pts):
#Write a script (or Jupyter Notebook) that calculates the fastest rise in water level per 6-minute period between measurements
#(for this assignment, assume that each line of the dataset is a 6-minute interval)
#and reports the date and time that was observed and the change in water level from the previous recording.

import pandas as pd  #read csv as pandas dataframe

df = pd.read_csv('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')     #open the file and rename it as df
df['Water Difference'] = df[' Water Level'].diff(1)      #create a new column on file df and calculate the diference between 
df.nlargest(1, ['Water Difference'])


# In[ ]:


#Problem 4 (5 pts):
#Imagine that the file is providing live readings of the water level.
#Write a script (or Jupyter Notebook) to print a line of text with a warning if any of these events occur:
# The water level increases more than 0.25 since the previous recording.
# The water level is over 5.0.
# No reading is received at a time point.

FILE = open('/blue/bsc4452/share/Class_Files/data/CO-OPS__8729108__wl.csv')     #open the file 

headerout = FILE.readlines()[1:]
level_before = float(headerout[0].split(",")[1])

for line in headerout:
    try:
            h2o_lvl = float(line.split(",")[1])
            diff = h2o_lvl - level_before
            level_before = h2o_lvl
                if diff > 0.25: #if the difference(rise of water level) is bigger than 0.25
                    print("WARNING: The water level has increased more than 0.25 since the last recording")
                if h2o_lvl > 5.0: # if the water level is greater than 5
                    print("WARNING: The water level is over 5.0")
    except: 
                    print("No reading was received")

