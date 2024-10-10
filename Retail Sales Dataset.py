#!/usr/bin/env python
# coding: utf-8

# # Retail Sales Dataset
# 

# # Data Loading and Cleaning

# In[5]:


import pandas as pd


# In[6]:


# load the datasets
df = pd.read_csv("ds.csv")


# # Data Dictionary
# 
# Transaction ID	String/Int	Unique identifier for each transaction.
# Date	Date/Time	The date on which the transaction took place.
# Customer ID	String/Int	Unique identifier for each customer.
# Gender	String	Gender of the customer (e.g., Male, Female).
# Age	Int	Age of the customer at the time of purchase.
# Product Category	String	Category of the product purchased (e.g., Electronics, Clothing).
# Quantity	Int	The number of units of the product purchased in that transaction.
# Price per Unit	Float	Price of one unit of the product.
# Total Amount	Float	Total amount for the transaction, calculated as (Quantity * Price per Unit).
# 

# In[4]:


#preview the dataset
print(df.head())


# In[8]:


# datatype information
df.info()


# In[9]:


# checking the columns in table
df.columns


# In[10]:


# checking for missing value
df.isnull().sum()


# In[11]:


# checking for duplicate value
df.duplicated().sum()


# 
# # Descriptive Statistics

# #Calculate descriptive stastics for relent colums

# In[12]:


mean_quantity = df['Quantity'].mean()


# In[13]:


medium_amount = df['Total Amount'].median()


# In[14]:


model_category = df['Product Category'].mode()[0]


# In[15]:


std_price = df['Price per Unit'].std()


# #Display summary statistics for numeric colums

# In[16]:


print(df[['Quantity','Total Amount','Product Category','Price per Unit']].describe())


# # Time Series Anylysis

# In[17]:


import matplotlib.pyplot as plt


# In[18]:


#Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])


# In[19]:


#set Date as index for time series analysis
df.set_index('Date',inplace=True)


# In[20]:


#Plot total sales over time
df['Total Amount'].plot(figsize=(10,6),title="Total Sales Over Time")
plt.show()


# In[39]:


#Resample date by month to analyze monthly sales trends
monthly_sales = df['Total Amount'].resample('M').sum()
monthly_sales.plot(title="Montly Sales Trends",figsize=(10,6))
plt.show()


# # Customer and Product Analysis

# In[40]:


#Sales by Gender
gender_sales = df.groupby('Gender')['Total Amount'].sum()


# In[42]:


#Sales by Age
age_sales = df.groupby('Age')['Total Amount'].sum()


# In[43]:


#Sales by Product Category
product_sales = df.groupby('Product Category')['Total Amount'].sum()


# In[48]:


#Top 10 customers (by Total Amount)
top_customers = df.groupby('Customer ID')['Total Amount'].sum().sort_values(ascending=False).head(10)


# #Display results

# In[49]:


print("Sales by Gender:\n",gender_sales)


# In[51]:


print("Sales by Age Group:\n",age_sales)


# In[53]:


print("Sales by Age Group:\n",age_sales)


# In[54]:


print("Top 5 Product Categories:\n",product_sales.sort_values(ascending=False).head(5))


# # Visualization

# In[2]:


import seaborn as sns


# In[4]:


#Bar chart for sales by product category
product_sales.plot(kind='bar',title="Sales by Product Category",figsize=(10,6))
plt.show()


# In[57]:


#Bar chart for sales by gender
gender_sales.plot(kind='bar',title="Sales by Gender",figsize=(10,6))
plt.show()


# In[1]:


sns.histplot(df['Total Amount'])


# In[60]:


#Correlation heatmap between numerical columns
corr = df[['Quantity', 'Price per Unit', 'Total Amount']].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()


# In[ ]:





# In[ ]:




