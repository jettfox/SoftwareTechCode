import pandas as pd
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
        
        
        #fulldata['Year'] = fulldata['ACCIDENT_DATE']
        #fulldata['Month'] = fulldata['ACCIDENT_DATE']
        #fulldata['Day'] = fulldata['ACCIDENT_DATE']
        for line in range(len(fulldata['ACCIDENT_DATE'])):
        #    fulldata['Year'][line] = fulldata['ACCIDENT_DATE'][line].split('/')[2]
        #    fulldata['Month'][line] = fulldata['ACCIDENT_DATE'][line].split('/')[1]
        #    fulldata['Day'][line] = fulldata['ACCIDENT_DATE'][line].split('/')[0]
            if(line % (749*5) == 0):
                print(f'{line//749}%')
        
        #StartYear = SelDate.split('/')[0]
        #StartMonth = SelDate.split('/')[1]
        #StartDay = SelDate.split('/')[2]
        #EndYear = EndDate.split('/')[0]
        #EndMonth = EndDate.split('/')[1]
        #EndDay = EndDate.split('/')[2]
        
        #toconcat = []
        #if (StartYear != EndYear):
            #middle years 
        #    df0 = fulldata.loc[fulldata['Year'] > StartYear]
        #    df0 = df0.loc[df0['Year'] < EndYear]
        #    toconcat.append(df0)
        #    # first year
        #    df1 = fulldata.loc[fulldata['Year'] == StartYear]
        #    # first month
        #    df2 = df1.loc[df1['Month'] == StartMonth]
        #    df2 = df2.loc[df2['Day'] >= StartDay] 
        #    df1 = df1.loc[df1['Month'] > StartMonth]
        #    toconcat.append(df1)
        #    toconcat.append(df2)
            # last year
        #    df3 = fulldata.loc[fulldata['Year'] == EndYear]
            # first month
        #    df4 = df3.loc[df3['Month'] == EndMonth]
        #    df4 = df4.loc[df4['Day'] <= EndDay]    
        #    df3 = df3.loc[df3['Month'] < EndMonth]
        #    toconcat.append(df3)
        #    toconcat.append(df4)
        #    df = pd.concat(toconcat)
            
        return 'Success'
    else:
        return 'Invalid File'