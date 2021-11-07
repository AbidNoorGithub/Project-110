import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
from statistics import mean
import random
import pandas as pd
import csv
import colorama
from colorama import Fore

#I used a different csv file, as the one given had only string data instead of numbers
df = pd.read_csv("SampleGraph.csv")
dataWeight = list(df["Weight"])
dataHeight = list(df["Height"])
data = dataWeight + dataHeight

# fig = ff.create_distplot([data], ["temp"], show_hist=False)

#Finding the mean of the data
dataMean = mean(data)

#Finds 30 random samples and finds the mean of all the samples
def RandomMeans():
    dataSet = []
    for i in range(0, 30):
        random_index = random.randint(0, len(data))
        value = data[random_index]
        dataSet.append(value)
    meanOfRandomMeans = mean(dataSet)
    return meanOfRandomMeans

def setup():
    meanList = []
    for i in range(0, 100):
        tempMean = RandomMeans()
        meanList.append(tempMean)


    #PLots the meanList
    fig = ff.create_distplot([meanList], ["info"])
    fig.show()

    #Compares mean of graph and mean of meanList
    meanOfMeanList = mean(meanList)
    print(Fore.MAGENTA + "The mean of the data is " + Fore.CYAN + str(dataMean) + Fore.MAGENTA + 
    " and the mean of the meanList is " + Fore.CYAN + str(meanOfMeanList))

setup()