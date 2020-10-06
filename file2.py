#A function that can acheive: For a user-selected period, produce a chart to show the number of accidents in each hour of the day (on average).

from SelectedTimePeriod import select_Time_Period
    
SelDate = input("input Start date YYYY/MM/DD: ")
EndDate = input("input End date YYYY/MM/DD: ")
data = select_Time_Period()

def sortHourOfDay(data, name):
    data = data[[col for col in data]]
    nRow, nCol = data.shape
       
    if (name == 'ACCIDENT_TIME'):
        BarData = {'00': 0, '01': 0, '02': 0, '02': 0, '03': 0, '04': 0, '05': 0, '06': 0, '07': 0, '08': 0, '09': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
        for index, row in data.iterrows():
            Hour = row['ACCIDENT_TIME'].split(".")[0]
            BarData[Hour] +=1         
    return BarData


print(sortHourOfDay(data, 'ACCIDENT_TIME'))