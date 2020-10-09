import pandas as pd
from datetime import datetime as dt
from file_loader import fileloader
fulldata = fileloader()
def select_Time_Period(SelDate, EndDate):
    if (type(fulldata) == pd.core.frame.DataFrame):
        if ((SelDate and EndDate) == False):
            return 'Invalid Date'
        if (len(SelDate.split('/')) != 3):
            return 'Invalid Date'
        else:
            valid = True
            for i in range(3):
                if (SelDate.split('/')[i].isdigit() == False):
                    valid = False
            if(valid == False):
                return 'Invalid Date'
                
        if (len(EndDate.split('/')) != 3):
            return 'Invalid Date'
        else:
            valid = True
            for i in range(3):
                if (EndDate.split('/')[i].isdigit() == False):
                    valid = False
            if(valid == False):
                return 'Invalid date'
    fulldata['ACCIDENT_DATE'] = pd.to_datetime(fulldata['ACCIDENT_DATE'])
    SelDate = dt.strptime(SelDate,'%d/%m/%Y')
    EndDate = dt.strptime(EndDate,'%d/%m/%Y')
    df = fulldata.loc[(fulldata['ACCIDENT_DATE'] >= SelDate)&(fulldata['ACCIDENT_DATE'] <= EndDate)]
    df['ACCIDENT_DATE'] = df['ACCIDENT_DATE'].dt.strftime('%d/%m/%Y')
    df['ACCIDENT_DATE'] = df['ACCIDENT_DATE'].astype(str)
    return df

