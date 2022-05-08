Pands-Project by Patrick Foley

Fisher's Iris data set is a very famous multivariate data set used for data science. The data set is made up of 5 variables which are summarised below. There are 3 varieties of the species Iris. These are: Setosa, Versicolor, Verginica. There are 50 of each variety included in the data set.


Summary of Variables
There are 5 variables in the Iris flower data set:
Sepal Length, Sepal Width, Petal Length, Petal Width and Variety of the flower all measured in centimeters.
The first 4 variables create a linear discriminant model to classify the Variety.

-Sepal Length
    The sepal is the part of the flower that protects the flower when it is in bud.
    The sepal length is measured from the middle of the flower to the outermost edge of the sepal.

-Sepal Width
    This is a measurement across the widest part of the sepal.

-Petal Length
    This is measured from the middle of the flower to the end of the petal.

-Petal Width
    This is a measurement across the widest part of the petal.

-Variety
    The 3 varieties of the species are Setosa, Versicolor, Verginica.


Analysis.py
This file can be run using py .\Analysis.py
This is a python file that carries out analytical tasks on the Iris Data set which is contained in the Comma Separated Value file iris.csv. The dataframe used in Analysis.py (df) is read directly from this csv file using pandas. This file outputs a description of the dataset to Summary.txt, along with outputting histograms to png files, followed by outputting scatter plots of each variable pair to png files. A boxplot of each variable is also outputted to a png file.

Summary.txt
Analysis.py outputs some descriptive information about the dataset to summary.txt including the amounts of rows, columns and elements in the dataset. Summary.txt also includes the standard deviations, means, min, max and percentile of each column/variable. Summary is opened using the "with open" function in write mode. Using "with open" means the file does not have to be closed with "f.close()". Pandas is a very useful library for descibing datasets, containing functions that can be seen in Analysis.py to describe a lot of aspects of a dataframe. Even when read from a csv file. The write function is used extensively in analysis.py to format the Summary.txt files and also to write each pandas function (as a string) to the text file.

Iris.csv
Comma separated values files are files that allow for data to be saved in tabular format. The values in the file are separated by commas. Pandas is useful for reading data in this format.

Histograms
The code for the histograms starts on line 60 of Analysis.py. Both the seaborn and matplotlib libraries are used to design and output these graphs. Each of these histograms is saved to its own png file titled with the attribute that is being displayed. The bars in the histograms are coloured according to the variety that the measurement applies to.

Analysis
-petal_length.png:  We can see here that setosa have the shortest petals (1 - 2cm)
                    Versicolor have the medium length petals (3 - 5.5cm)
                    Virginica has the longest petals (4.5 - 6.8cm)

-sepal_length.png:  Setosa has the shortest sepals (4.5 - 5.9cm)
                    Versicolor has the medium length of sepals (5 - 7cm). It is also widely distributed here.
                    Virginica has the longest sepals (5.5 - 7.9cm)

-petal-width.png:   Setosa have the slimmest petals (0.2 - 0.7cm)
                    Versicolor has the medium width of petal (1 - 2cm)
                    Virginica has largest distribution and widest petals (1.2 - 2.5cm)

-sepal-width.png:   Versicolor has the slimmest sepals (2 - 3.5cm)
                    Virginica have the medium width of sepal (2.2 - 3.8cm)
                    Setosa have the widest sepals (2.75 - 4.4cm)
                    The Sepal widths are most widely distributed and overlap more than any other variable.

-variety.png:       This shows the even distribution of varieties in the dataset. 50 of each variety.


Scatter Plots
The code for the scatter plots starts on line 110 of Analysis.py. These are plots of 2 of the variables against each other with the variety of the flower each having its own colour on the plot. These plots are a good way of displaying the legths and widths of the petals and sepals of each variety. These plots use seaborn to generate the plot and give the different varities a different hue/colour. Matplotlib is used to give the charts titles and axes titles. The plt.savefig saves the charts to its respecive png file which are titled with the variables that are shown. The plt.clf function is to stop adding code to each figure.

Analysis
-plength vs pwidth.png: We can see the size of petals increases in the following order setosa, versicolor, virginica.
-plength vs swidth.png: This shows the differnence in length of the petals of setosa from the other 2 varieties. The setosa petals are much shorter.
-slength vs plength.png: This shows how setosa has overall the shortest petals and sepals. While versicolor and virginica have longer. With virginica being the longest.
-slength vs swidth.png: Setosa have shorter wider sepals while the other 2 have longer and skinier sepals.
-swidth vs pwidth.png:  Setosa have much wider sepals while versicolor have wider petals with virginica having the widest petals.

Boxplot
Boxplot.png is a figure of 4 boxplot subplots. These boxplots are an effective way of showing the distribution of the measurements of each variety of iris. Once again seaborn was used to generate the subplots while titles were added using matplotlib. This plot is defined as graph(y) and each subplot substitutes a variable for the y while the x variable remains the variety of plant. The size of the subplots is set using plt.figure function while their positions are set using grid positions after the plt.subplot function. This was once again saved to a png file.

Analysis
The boxplots show the distribution of each variable for each variety as the black lines. The densest portion of the distribution is a coloured block. The mean is a line across the coloured block. The outliers are diamonds outside these areas. Much of the above information on variety and measurements is contained in this.

Conclusion
The Fisher Iris Dataset is of sufficient size to perform many basic analytical techniques on. These techniques and graphs can be used to identify a variety of this species when given the length and width of its petals and/or sepals.
-For Example:
     
     If you are given
     sepal length = 5cm
     petal length = 1.5cm 
     you can see that this would be of the setosa variety.

     If you are given
     petal length = 4.1cm
     petal width = 1.4cm
     you can see that this would be of the versicolor variety

This analysis would be much tougher to carry out while looking at the csv file but when the data science techniques are carried out and visuals are created, this analysis becomes much easier.

Furthermore the dataset also provides a good dataframe for very useful libraries such as matplotlib, numpy, pandas and seaborn to be expressed. The functions from these libraries prove very efficient in producing all necesarry data summaries and plots, and give a good degree of scope for customisation (of the plots).


References
Andrew Beatty 2022, Accessed 2022 <https://learnonline.gmit.ie/course/view.php?id=5057#section-11>
Elina Loseva 2018, Accessed 2022 <http://rstudio-pubs-static.s3.amazonaws.com/450733_9a472ce9632f4ffbb2d6175aaaee5be6.html>
Aditya Jetely 2020 Accessed 29-04-2022 <https://towardsdatascience.com/eda-of-the-iris-dataset-190f6dfd946d>
Pranshu Sharma 2021, Accessed 29-04-2022 <https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda>
GeeksforGeeks 2022 Accessed 30-04-2022 <https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/>
<https://www.geeksforgeeks.org/plotting-graph-for-iris-dataset-using-seaborn-and-matplotlib/>
curran 2022, accessed 27-04-2022 <https://gist.github.com/curran/a08a1080b88344b0c8a7>
Zach  2021, accessed 27-04-2022 <https://www.statology.org/iris-dataset-r/>
scikit-learn.org, accessed 30-04-2022 <https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html>
Injemamul Irshad 2021, accessed 27-04-2022 <https://njkhanh.com/iris-flower-classification-step-by-step-tutorial-p5f313139>
Michael Friendly and Matthew Sigal 2016, Accessed 31-04-2022 <https://mattsigal.github.io/eqcov_supp/iris-ex.html>
Saral Gyaan , accessed 27-04-2022 <https://saralgyaan.com/posts/matplotlib-tutorial-in-python-chapter-6-scatter-plotting/>
Stackoverflow, accessed 04-2022 <https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another>
<https://stackoverflow.com/questions/52385428/plot-point-markers-and-lines-in-different-hues-but-the-same-style-with-seaborn>
<https://stackoverflow.com/questions/6916978/how-do-i-tell-matplotlib-to-create-a-second-new-plot-then-later-plot-on-the-o>
<https://stackoverflow.com/questions/27157522/pandas-plot-histogram-data-frame-index>
Zolzaya Luvsandorj 2021 <https://towardsdatascience.com/4-simple-tips-for-plotting-multiple-graphs-in-python-38df2112965c>
Preeya Sawadmanod 2019 accessed 27-04-2022<https://medium.com/analytics-vidhya/editing-data-visualization-in-python-64f42225ba21>