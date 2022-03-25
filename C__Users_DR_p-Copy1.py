#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mysql-connector-python


# In[2]:


import mysql.connector


# In[3]:


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="password1234!",
    database='sys')


# In[4]:


# Run the SQL query
mycursor = mydb.cursor()
mycursor


# In[5]:


mycursor.execute("Select * from sys.sys_config")


# In[6]:


myresults = mycursor.fetchall()
type(myresults)


# In[7]:


myresults[0]


# In[8]:


mycursor.column_names # Returning the column names from the table


# In[9]:


df = []   # Initialising empty list
for x in myresults:    # for loop to append each entry to a new list of lists
    df.append(list(x)) 
df = pd.DataFrame(df)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[10]:


df = [] 
df = pd.DataFrame(df)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[11]:


df = pd.DataFrame(df)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[12]:


df = pd.DataFrame(myresults)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[13]:


df = []   # Initialising empty list
for x in myresults:    # for loop to append each entry to a new list of lists
    df.append(list(x)) 
df = pd.DataFrame(df)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[14]:


import pandas as pd


# In[15]:


df = []   # Initialising empty list
for x in myresults:    # for loop to append each entry to a new list of lists
    df.append(list(x)) 
df = pd.DataFrame(df)  # Convert list of lists into a DataFrame
df.columns = mycursor.column_names # Add the columns names
df.head()


# In[ ]:




