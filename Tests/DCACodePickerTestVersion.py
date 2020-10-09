# For a user-selected period,
# E.G. animal, ped. (use1r entered)
# Retrieve all accidents that contains a keyword In the DCA_CODE,
from pandas import pandas as pd
def DCACodePicker(data, Keyword):
    #check whether data is a dataframe
    if (type(data) == pd.core.frame.DataFrame):
        #checks whether 'DCA_CODE' is a column heading
        if 'DCA_CODE' in data:
            #checks whether user input a keyword
            if (Keyword):
                #makes sure data is formatted
                data = data[[col for col in data]]
                #create a new dataframe to return
                RelevantData = pd.DataFrame({'' : []})
                #this iterates through the data row by row
                for index, row in data.iterrows():
                    currkeywords = row['DCA_CODE']
                    #if a user key word is in the row's DCA CODE then, that row of data gets added to the df
                    if (Keyword in currkeywords):
                        RelevantData = data.append(row , ignore_index=True)
                
                return 'Success'
            else:
                return 'No Search Term Supplied'
        else:
            return 'Incorrect Data'
    elif (data == 'Invalid Date'):
        return 'Invalid Date'
    else:
        return 'Unknown Error'