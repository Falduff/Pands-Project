#analysis.py is the python program that:
#1. Outputs a summary of each variable to a single text file,
#2. Saves a histogram of each variable to png files, and
#3. Outputs a scatter plot of each pair of variables. 
##Importing Libraries
from pydoc import describe
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#1. Summary text file
#This code uses functions to produce the summary outputs of the dataset. iris.csv
#The dataframe (df) is defined as iris.csv
#Each function is defined by lines followed by a number.
#This was to make it easier when writing and formatting the text file (line 33)
#The pandas library is used extensively here.

df = pd.read_csv("iris.csv")
lines = (df.describe())
lines2 = (df.head())
lines3 = [(len(df))]
lines4 = [(len(df.columns))]
lines5 = [(df.__sizeof__())]
lines6 = (df.info(verbose=True))

lines8 = (df.nunique())
lines9 = df.drop_duplicates(subset ="variety",)


#The following code is used to output the different functions above as strings
#Into the Summary.txt file. It makes use of the s.write function and \n to
#forat the text in a neat way and as to space it out in the text file.
#The headings are also added above each output here.
with open('Summary.txt','w') as s:
    s.write("Description of the Data")
    s.write(2*"\n")
    s.write(str(lines))
    s.write(2*"\n")
    s.write("Unique Variables in each Column")
    s.write("\n")
    s.write(str(lines8))
    s.write(2*"\n")
    s.write("Varieties of Species")
    s.write("\n")
    s.write(str(lines9))
    s.write(2*"\n")
    s.write("First 5 rows of the Dataset")
    s.write("\n")
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



#2 Histogram for each variable
#Bins refers to the size of the bars on the histogram
#Title and labels added using matplotlib
#Histograms made using matplotlib
#Histograms all saved to png files 
#plt.clf clears the plot figure, so that plots do not overlap on top of each other

#Sepal Length Histogram
sns.histplot(data = df, x = "sepal.length", hue="variety")
plt.title("Distribution of Sepal Length",fontsize = 15)
plt.xlabel("Sepal Length in cm", fontsize = 10)
plt.ylabel("Frequency of Variety", fontsize = 10)
plt.savefig('sepal_length.png')
plt.clf()

#Sepal Width Histogram
sns.histplot(data = df, x = "sepal.width", hue="variety")
plt.title("Distribution of Sepal Width",fontsize = 15)
plt.xlabel("Sepal Width in cm", fontsize = 10)
plt.ylabel("Frequency of Variety", fontsize = 10)
plt.savefig('sepal_width.png')
plt.clf()

#Petal Length Histogram
sns.histplot(data = df, x = "petal.length", hue="variety")
plt.title("Distribution of Petal Length",fontsize = 15)
plt.xlabel("Petal Length in cm", fontsize = 10)
plt.ylabel("Frequency of Variety", fontsize = 10)
plt.savefig('petal_length.png')
plt.clf()

#Petal Width Histogram
sns.histplot(data = df, x = "petal.width", hue="variety")
plt.title("Distribution of Petal Width",fontsize = 15)
plt.xlabel("Petal Width in cm", fontsize = 10)
plt.ylabel("Frequency of Variety", fontsize = 10)
plt.savefig('petal_width.png')
plt.clf()

#Variety of Species Histogram
sns.histplot(data = df, x = "variety", hue="variety")
plt.title("Distribution of Species",fontsize = 15)
plt.xlabel("Species Name", fontsize = 10)
plt.ylabel("Frequency of Variety", fontsize = 10)
plt.savefig('variety.png')
plt.clf()



#3 Scatter Plots of Each variable pair
#Seaborn used to create scatterplot to add a hue to the variety.
#Plot design still makes use of matplotlib (titles and axis)
#All scatter plots are outputted to individual png files png files

#Sepal Length and Sepal Width
a = sns.scatterplot(x="sepal.length", y="sepal.width", hue="variety", data=df)
plt.title("Sepal Length vs Sepal Width Scatter",fontsize = 15)
plt.xlabel("Sepal Length", fontsize = 10)
plt.ylabel("Sepal Width", fontsize = 10)
plt.savefig('slength vs swidth.png')

#plt.show()
plt.clf()

#Sepal Length and Petal Length
b = sns.scatterplot(x="sepal.length", y="petal.length", hue="variety", data=df)
plt.title("Sepal Length vs Petal Length Scatter",fontsize = 15)
plt.xlabel("Sepal Length", fontsize = 10)
plt.ylabel("Petal Length", fontsize = 10)
plt.savefig('slength vs plength.png')
#plt.show()
plt.clf()

#Petal Length and Petal Width
c = sns.scatterplot(x="petal.length", y="petal.width", hue="variety", data=df)
plt.title("Petal Length vs Petal Width Scatter",fontsize = 15)
plt.xlabel("Petal Length", fontsize = 10)
plt.ylabel("Petal Width", fontsize = 10)
plt.savefig('plength vs pwidth.png')
#plt.show()
plt.clf()

#Sepal Width and Petal Width
d = sns.scatterplot(x="sepal.width", y="petal.width", hue="variety", data=df)
plt.title("Sepal Width vs Petal Width Scatter",fontsize = 15)
plt.xlabel("Sepal Width", fontsize = 10)
plt.ylabel("Petal Width", fontsize = 10)
plt.savefig('swidth vs pwidth.png')
#plt.show()
plt.clf()

#Sepal Length and Petal Width
e = sns.scatterplot(x="sepal.length", y="petal.width", hue="variety", data=df)
plt.title("Sepal Length vs Petal Width Scatter",fontsize = 15)
plt.xlabel("Sepal Length", fontsize = 10)
plt.ylabel("Petal Width", fontsize = 10)
plt.savefig('slength vs pwidth.png')
#plt.show()
plt.clf()

#Petal Length and Sepal Width
f = sns.scatterplot(x="petal.length", y="sepal.width", hue="variety", data=df)
plt.title("Petal Length vs Sepal Width Scatter",fontsize = 15)
plt.xlabel("Petal Length", fontsize = 10)
plt.ylabel("Sepal Width", fontsize = 10)
plt.savefig('plength vs swidth.png')
#plt.show()
plt.clf()


#Boxplot subplots used to see how the value of numerical variables is distributed between categorical variables
def graph(y):
    sns.boxplot(x="variety", y=y, data=df)

  
plt.figure(figsize=(9,9))
      
# Adding the subplot at the specified grid position
# y labels and titles are also added to the subplots here.

plt.subplot(221)
graph('sepal.length')
plt.ylabel("Sepal Length", fontsize = 10)
plt.title("Sepal Length for each Variety")

plt.subplot(222)
graph('sepal.width')
plt.ylabel("Sepal Width", fontsize = 10)
plt.title("Sepal Width for each Variety")

plt.subplot(223)
graph('petal.length')
plt.ylabel("Petal Length", fontsize = 10)
plt.title("Petal Length for each Variety")

plt.subplot(224)
graph('petal.width')
plt.ylabel("Petal Width", fontsize = 10)
plt.title("Petal Width for each Variety")

plt.savefig('Boxplots.png')