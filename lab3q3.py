# -*- coding: utf-8 -*-
"""lab3q3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n3eCBHgR_1XaETZRAY3RXq1vUh9jiH5C
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
df = pd.read_csv ('Iris.csv')

def barChart():
  df.Species.value_counts().plot(figsize=(7,5),kind='bar',color=['orange','blue','green'],xlabel='Species',ylabel='Frequency of Species')
  plt.title("Frequency Bar Graph")
  plt.show()

def scatterPlot():
  print()
  X = df.iloc[:, 1:5].values
  X_std = StandardScaler().fit_transform(X)
  pca = PCA(n_components=2)
  principalComponents = pca.fit_transform(X_std)
  principalDf = pd.DataFrame(data = principalComponents
              , columns = ['principal component 1', 'principal component 2'])
  finalDf = pd.concat([principalDf, df['Species']], axis = 1)

  fig = plt.figure(figsize = (7,5))
  ax = fig.add_subplot(1,1,1)
  ax.set_xlabel('First Principle Component')
  ax.set_ylabel('Second Principal Component')
  ax.set_title('PCA Graph')
  targets = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
  colors = ['orange', 'blue', 'green']
  for target, color in zip(targets,colors):
      indicesToKeep = finalDf['Species'] == target
      ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1']
                , finalDf.loc[indicesToKeep, 'principal component 2']
                , c = color
                , s = 50)
  ax.legend(targets)
  plt.show()

def distributionHistogram():
  print()
  plt.figure(figsize = (7, 5))
  x = df.SepalLengthCm
  plt.hist(x, color = "turquoise")
  plt.title("Sepal Length Histogram")
  plt.xlabel("Sepal Length cm")
  plt.ylabel("Distribution Count")
  plt.show()

  print()
    plt.figure(figsize = (7, 5))
  x = df.SepalWidthCm
  plt.hist(x, color = "crimson")
  plt.title("Sepal Width Histogram")
  plt.xlabel("Sepal Width cm")
  plt.ylabel("Distribution Count")
  plt.show()

  print()
  plt.figure(figsize = (7, 5))
  x = df.PetalLengthCm
  plt.hist(x, color = "yellow")
  plt.title("Petal Length Histogram")
  plt.xlabel("Petal Length cm")
  plt.ylabel("Distribution Count")
  plt.show()

  print()
  plt.figure(figsize = (7, 5))
  x = df.PetalWidthCm
  plt.hist(x, color = "indigo")
  plt.title("Petal Width Histogram")
  plt.xlabel("Petal Width cm")
  plt.ylabel("Distribution Count")
  plt.show()

#calling functions
barChart()
scatterPlot()
distributionHistogram()