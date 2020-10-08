# For a user-selected period, (DONE)
# E.G. animal, ped. (use1r entered)
# Retrieve all accidents that contains a keyword In the DCA_CODE,
from pandas import pandas as pd
def DCACodePicker(data, Keyword):
    if (type(data) == pd.core.frame.DataFrame):
        if 'DCA_CODE' in data:
            if (Keyword):
                data = data[[col for col in data]]
                RelevantData = pd.DataFrame({'' : []})
                for index, row in data.iterrows():
                    currkeywords = row['DCA_CODE']
                
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
        return 'Unknow Error'