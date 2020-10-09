import pandas as pd
from datetime import datetime as dt
from file_loader import fileloader
fulldata = fileloader()
def select_Time_Period(StartDate, EndDate):
    #this error checking makes sure that the date is valid
    if (type(fulldata) == pd.core.frame.DataFrame):
        if ((StartDate and EndDate) == False):
            return 'Invalid Date'
        if (len(StartDate.split('/')) != 3):
            return 'Invalid Date'
        else:
            valid = True
            for i in range(3):
                if (StartDate.split('/')[i].isdigit() == False):
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
    #this takes the full data from the database and converts the accident date from a string to an actual datetime.
    fulldata['ACCIDENT_DATE'] = pd.to_datetime(fulldata['ACCIDENT_DATE'])
    #this converts the input start and end dates into datetime as well
    StartDate = dt.strptime(StartDate,'%d/%m/%Y')
    EndDate = dt.strptime(EndDate,'%d/%m/%Y')
    #this uses the pandas filter feature to makes the df dateframe with only the data that has an accident date above or equal to start date and below or equal to end date
    df = fulldata.loc[(fulldata['ACCIDENT_DATE'] >= StartDate)&(fulldata['ACCIDENT_DATE'] <= EndDate)]
    #this converts the format of the new df dateframe accident date from datetime format to dd/mm/yyyy format
    df['ACCIDENT_DATE'] = df['ACCIDENT_DATE'].dt.strftime('%d/%m/%Y')
    #this converts it back into a string like it was originally as to keep the data constistant with orginal just filtered not changed
    df['ACCIDENT_DATE'] = df['ACCIDENT_DATE'].astype(str)
    return df

