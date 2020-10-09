from alcoholTimeAnalizer import alcoholTimeAnalizer
from mapGenerator import mapGenerator
from file_loader import fileloader
from SelectedTimePeriod import select_Time_Period
from sortHourDay import sortHourOfDay
from DCACodePicker import DCACodePicker
#data = fileloader()

timedata = select_Time_Period('01/04/2015', '04/06/2016')
sortHourOfDay(timedata)

#alcoholTimeAnalizer(data,'DAY_OF_WEEK')
#alcoholTimeAnalizer(data,'LIGHT_CONDITION')
#alcoholTimeAnalizer(data,'ALCOHOL_RELATED')
#alcoholTimeAnalizer(data,'SEVERITY') 

#mapGenerator(data, 'SEVERITY', "2013")
#mapGenerator(data, 'SEVERITY', "2014")
#mapGenerator(data, 'SEVERITY', "2015")
#mapGenerator(data, 'SEVERITY', "2016")
#mapGenerator(data, 'SEVERITY', "2017")
#mapGenerator(data, 'SEVERITY', "2018")

#mapGenerator(data, 'ALCOHOL_RELATED', "2013")
#mapGenerator(data, 'ALCOHOL_RELATED', "2014")
#mapGenerator(data, 'ALCOHOL_RELATED', "2015")
#mapGenerator(data, 'ALCOHOL_RELATED', "2016")
#mapGenerator(data, 'ALCOHOL_RELATED', "2017")
#mapGenerator(data, 'ALCOHOL_RELATED', "2018")

#mapGenerator(data, 'HIT_RUN_FLAG', "2013")
#mapGenerator(data, 'HIT_RUN_FLAG', "2014")
#mapGenerator(data, 'HIT_RUN_FLAG', "2015")
#mapGenerator(data, 'HIT_RUN_FLAG', "2016")
#mapGenerator(data, 'HIT_RUN_FLAG', "2017")
#mapGenerator(data, 'HIT_RUN_FLAG', "2018")


#Keyword = input('Enter Keyword: ')

#data = DCACodePicker(timedata, Keyword)
#print(data['DCA_CODE'],data['ACCIDENT_DATE'])
