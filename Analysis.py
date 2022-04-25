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


with open('Summary.txt','w') as s:
    s.write("Description of the Data")
    s.write(2*"\n")
    s.write(str(lines))
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