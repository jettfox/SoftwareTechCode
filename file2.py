#A function that can acheive: For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).
from matplotlib import pyplot as plt
import pandas as pd

def sortHourOfDay(data, start, end):
    if (type(data) == pd.core.frame.DataFrame):
        data = data[[col for col in data]]
        if 'ACCIDENT_TIME' in data:
            BarData = {'00': 0, '01': 0, '02': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
            for index, row in data.iterrows():
                Hour = row['ACCIDENT_TIME'].split('.')[0]
                BarData[Hour] +=1
                    
            plt.title(f'Number of crashes between {start} and {end}')
            plt.xlabel('Hour of the day')
            plt.ylabel('Number of Crashes')
            Yaxis = BarData.values()
            Xaxis = BarData.keys()
            plt.bar(Xaxis, Yaxis, align = 'center')
            plt.show()
            
            return BarData
        else:
            return 'Incorrect Data'
    elif (data == 'Invalid Date'):
        return 'Invalid Date'
    else:
        return 'Invalid Data'