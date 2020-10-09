#A function that can acheive: For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).
from matplotlib import pyplot as plt
import pandas as pd

#this function takes a dataframe which is a section of the of the main dataframe and produces a graph that displays the amount of those crashes happen during each hour of a 24 hour period
def sortHourOfDay(data):
    #checks whether data is a dataframe
    if (type(data) == pd.core.frame.DataFrame):
        #makes sure that the data is formatted correctly
        data = data[[col for col in data]]
        #checks whether the has this collumn title
        if 'ACCIDENT_TIME' in data:
            # a dictionary with the all of the data that will go in the graph.
            BarData = {'00': 0, '01': 0, '02': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
            #this adds the data to the above dict by it's corresponding key
            for index, row in data.iterrows():
                Hour = row['ACCIDENT_TIME'].split('.')[0]
                BarData[Hour] +=1
            #no graphs in test version
            
            return 'Success'
        else:
            return 'Incorrect Data'
    else:
        return 'Invalid Data'