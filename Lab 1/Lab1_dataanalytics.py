#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Given the Dataset of a Bank (Bank.csv). 
#The file has the following properties.
#Values are separated by a semicolon (;)
#The first line is the header row.
#You have to create a menu-driven program with the help of functions to perform the following:
#Without using the help of any libraries, open the given dataset.
#Print the headers in the file.
#Find the count of customers in each category 'marital'.
#Prepare a histogram for age using a print statement.
#Advance Challange:
#Ask the user to select any column of his choice from the list of headers, after which you can create a count plot for the column.


# In[4]:


#Without using the help of any libraries, open the given dataset.
df=open("C:\\Users\\Admin\\Documents\\GitHub\\22112320_LakshmiWarrier_BEA372\\Lab 1\\bank.csv","r")
header=df.readline()
data=df.readlines()


# In[5]:


#Print the headers in the file.
header = header.replace('"','').split(";")
for item in header:
    print(item)


# In[6]:


#Find the count of customers in each category 'marital'.
dictionary={}
married=0
single=0
divorced=0
for value in data:
    value = value.replace('"','').split(";")
    for status in value:
        if status=="married":
            married+=1
        elif status=="single":
            single+=1
        elif status=="divorced":
            divorced+=1
print("married",married)
print("single",single)
print("divorced",divorced)
dictionary["married"]=married
dictionary["single"]=single
dictionary["divorced"]=divorced
print(dictionary)
                 


# In[7]:


#Prepare a histogram for age using a print statement.
# extracting the data "age" from the csv file
age_list=[]
for line in data:
    columns=line.strip().split(';')
    age=columns[0]
    age_list.append(age)
print(age_list)
print(len(age_list))


# In[8]:


# Determine the maximum value in the data
max_value = max(age_list)
print(max_value)


# In[9]:


# Define the scale factor for the histogram
scale_factor = 4521 / 87  # Scale to fit within 4521 characters
print(int(scale_factor))


# In[ ]:


# Print the histogram
for agelist in age_list:
    scaled_value = int(agelist * int(scale_factor))  # Scale the value
    histogram_row = ""

    # Add '#' symbols to the histogram row
    for u in range(scaled_value):
        histogram_row += "#"
        print(histogram_row)


# In[ ]:





# In[ ]:




