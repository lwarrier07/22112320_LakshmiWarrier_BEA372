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


def age(age_list):
    age_counts = [0] * 10 # Initialize an empty list with 10 elements as 0

    for age in age_list:
        age = int(age)  # Convert age to an integer
        if age <= 9:
            age_counts[0] += 1
        elif age <= 19:
            age_counts[1] += 1
        elif age <= 29:
            age_counts[2] += 1
        elif age <= 39:
            age_counts[3] += 1
        elif age <= 49:
            age_counts[4] += 1
        elif age <= 59:
            age_counts[5] += 1
        elif age <= 69:
            age_counts[6] += 1
        elif age <= 79:
            age_counts[7] += 1
        elif age <= 89:
            age_counts[8] += 1
        else:
            age_counts[9] += 1

    for i in range(len(age_counts)):
        lower_bound = i * 10
        upper_bound = (i * 10) + 9
        histogram_line = f"{lower_bound}-{upper_bound}: {'|' * age_counts[i]} {age_counts[i]}"
        print(histogram_line)    

age(age_list)




