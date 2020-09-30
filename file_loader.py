import pandas as pd 
def fileloader():
    data = pd.read_csv("Crash Statistics Victoria.csv") 
    data.head()
    return data