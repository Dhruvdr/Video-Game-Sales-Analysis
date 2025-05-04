import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import seaborn as sns

#to show the maximum number of columns 
pd.set_option('display.max_column', None)

#------- DATASET EXPLORATION----------

df= pd.read_csv(r"D:\DEVELOPMENT\PROJECTS\EDA\vgsales.csv")
# print(df.head(5))

#looking at the data size , feature numbers 
# print(df.shape)
# print(df.tail(5))

#Attributing Information
# print(df.columns)
# print(df.info())

#checking missing values
print(df.isnull().sum())

# replacing the missing values
print(df['Year'].unique())
print(df['Year'].value_counts())

# replacing the missing values with mode
# print(df['Year'].mode()[0])
df['Year']= df['Year'].fillna(df['Year'].mode()[0])         #replaces the null value with given value
# print(df['Year'].isnull().sum())

# print(df['Publisher'].unique())
# print(df['Publisher'].value_counts())

df['Publisher']= df['Publisher'].fillna(df['Publisher'].mode()[0])         #replaces the null value with given value
# print(df['Publisher'].isnull().sum())

# print(df.info())

# Describe shows the main statistical characteristics of the dataset for each feature
# print(df.describe())
# to see statistics of non-numeric features 
# print(df.describe(include= ["object"]))

#SORTING
#sorting by Name
print(df.sort_values(by = "Name", ascending=True).head())
#sorting by Year and Name
print(df.sort_values(by = ["Year","Name"], ascending=[False,True]).head())

# Indexing and Extracting Data 
# print(df.head())

# Sales of Wii Plaatform in Europe 
print("Sales of Wii Platform games in Europe =",df[df['Platform']=="Wii"]['EU_Sales'].sum())

#Get the last line of the dataframe
# print(df[-1:])

# PIVOT TABLES
print(pd.crosstab(df["Publisher"],df["Genre"]))

# ------VISUALIZATION---------

# visualize the pair wise dependencies between features
pd.plotting.scatter_matrix(
    df[["NA_Sales","EU_Sales","JP_Sales"]],
    figsize=(15,15),
    diagonal="kde")
# plt.show()

# Getting the year where games are sold the most 
df['Year'].hist()
df.hist(color = 'k',
        bins = 30,
        figsize = (15,10))
# plt.show()
# Histogram presented allows us to make assumptions about the variability of the source data


#List of top 10 Global Sales 
print(df.sort_values(by = "Global_Sales", ascending=False).head(10))
#List of top 1) Global Sales after 2000
print(df[df["Year"]>2000.0].sort_values(by = "Global_Sales", ascending=False).head(10))
