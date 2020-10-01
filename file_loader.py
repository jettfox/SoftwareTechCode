import pandas as pd
def fileloader():
    data = pd.read_csv("Crash Statistics Victoria.csv", delimiter=',') 
    data.dataframeName = 'Crash Statistics Victoria.csv'
    return data