import pandas as pd
#this reads the crash stats for Vic and saves it as a dataframe and returns data, the badfileloader does the same but for a modifed version of the crash stats for testing purposes
def fileloader():
    data = pd.read_csv("Crash Statistics Victoria.csv", delimiter=',') 
    data.dataframeName = 'Crash Statistics Victoria.csv'
    return data

def badfileLoader():
    data = pd.read_csv("wrong.csv", delimiter=',') 
    data.dataframeName = 'Crash Statistics Victoria.csv'
    return data
