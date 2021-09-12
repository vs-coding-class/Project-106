import plotly.express as plex
import numpy as np
import csv
import pandas as pd

def plot(fileName):
    with open(fileName) as f:
        reader = pd.read_csv(f)
        fig = plex.scatter(reader, x = "Coffee in ml", y = "sleep in hours", color = "week")
        fig.show()

def getData(fileName):
    xArray= []
    yArray = []
    with open(fileName) as f:
        reader = csv.DictReader(f)
        for row in reader:
            xArray.append(float(row["Coffee in ml"]))
            yArray.append(float(row["sleep in hours"]))
    return {"x": xArray, "y": yArray}

def correlation(source):
    correlation = np.corrcoef(source["x"], source["y"])
    print(f"The correlation of this data set is {correlation[0,1]}.")

def main():
    file = "coffeeVsSleep.csv"
    plot(file)
    dataSource = getData(file)
    correlation(dataSource)

main()