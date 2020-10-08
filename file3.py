# For a user-selected period, (DONE)
# E.G. animal, ped. (user entered)
# Retrieve all accidents that contains a keyword In the DCA_CODE,
from pandas import pandas as pd
def DCACodePicker(data, Keyword):
    data = data[[col for col in data]]
    
    RelevantData = pd.DataFrame({'' : []})
    for index, row in data.iterrows():
        currkeywords = row['DCA_CODE']
    
        if (Keyword in currkeywords):
            RelevantData = data.append(row , ignore_index=True)
    
    return RelevantData