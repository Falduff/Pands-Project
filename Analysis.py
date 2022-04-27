#analysis.py is the python program that:
#1. Outputs a summary of each variable to a single text file,
#2. Saves a histogram of each variable to png files, and
#3. Outputs a scatter plot of each pair of variables. 
##Importing Libraries
from pydoc import describe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#1. Summary text file
df = pd.read_csv("iris.csv")
lines = (df.describe())
lines2 = (df.head())
lines3 = [(len(df))]
lines4 = [(len(df.columns))]
lines5 = [(df.__sizeof__())]
lines6 = (df.info(verbose=True))
lines7 = ['Summary of Variables','There are 5 variables in the Iris flower data set:',
'Sepal Length, Sepal Width, Petal Length, Petal Width and Variety of the flower.',
'The first 4 variables create a linear discriminant model to classify the Variety.',
'','Sepal Length',
'The sepal is the part of the flower that protects the flower when it is in bud.',
'The sepal length is measured from the middle of the flower to the outermost edge of the sepal','',
'Sepal Width','This is a measurement across the widest part of the sepal','',
'Petal Length','This is measured from the middle of the flower to the end of the petal',
'', 'Petal Width','This is a measurement across the widest part of the petal']

lines8 = (df.nunique())

with open('Summary.txt','w') as s:
    s.write("Description of the Data")
    s.write(2*"\n")
    s.write(str(lines))
    s.write(2*"\n")
    s.write("Unique Variables in each Column")
    s.write("\n")
    s.write(str(lines8))
    s.write(2*"\n")

    s.write("First 5 rows of the Dataset")
    s.write(2*"\n")
    s.write(str(lines2))
    s.write(2*"\n")
    s.write("Number of Rows in the Dataset")
    s.write("\n")
    s.write(str(lines3))
    s.write(2*"\n")
    s.write("Number of Columns in the Dataset")
    s.write("\n")
    s.write(str(lines4))
    s.write(2*"\n")
    s.write("Number of elements in the Dataset")
    s.write("\n")
    s.write(str(lines5))
    s.write("\n")
    s.write("\n")
    s.write('\n'.join(lines7))

#2 Histogram for each variable

#Sepal Length Histogram
plt.hist(df['sepal.length'], bins=30)
plt.title("Distribution of Sepal Length",fontsize = 15)
plt.xlabel("Sepal Length in cm", fontsize = 10)
plt.ylabel("Frequency of Species", fontsize = 10)
plt.savefig('sepal_length.png')
plt.clf()

#Sepal Width Histogram
plt.hist(df['sepal.width'], bins=30)
plt.title("Distribution of Sepal Width",fontsize = 15)
plt.xlabel("Sepal Width in cm", fontsize = 10)
plt.ylabel("Frequency of Species", fontsize = 10)
plt.savefig('sepal_width.png')
plt.clf()

#Petal Length Histogram
plt.hist(df['petal.length'], bins=30)
plt.title("Distribution of Petal Length",fontsize = 15)
plt.xlabel("Petal Length in cm", fontsize = 10)
plt.ylabel("Frequency of Species", fontsize = 10)
plt.savefig('petal_length.png')
plt.clf()

#Petal Width Histogram
plt.hist(df['petal.width'], bins=30)
plt.title("Distribution of Petal Width",fontsize = 15)
plt.xlabel("Petal Width in cm", fontsize = 10)
plt.ylabel("Frequency of Species", fontsize = 10)
plt.savefig('petal_width.png')
plt.clf()

#Variety of Species Histogram
plt.hist(df['variety'], bins=30)
plt.title("Distribution of Species",fontsize = 15)
plt.xlabel("Species Name", fontsize = 10)
plt.ylabel("Frequency of Species", fontsize = 10)
plt.savefig('variety.png')
plt.clf()