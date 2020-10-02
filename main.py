from file4 import alcoholTimeAnalizer
from file5 import mapGenerator
from file_loader import fileloader
data = fileloader()
alcoholTimeAnalizer(data,'DAY_OF_WEEK')
alcoholTimeAnalizer(data,'LIGHT_CONDITION')
alcoholTimeAnalizer(data,'ALCOHOL_RELATED')
alcoholTimeAnalizer(data,'SEVERITY')

mapGenerator(data, 'SEVERITY', "2013")
mapGenerator(data, 'SEVERITY', "2014")
mapGenerator(data, 'SEVERITY', "2015")
mapGenerator(data, 'SEVERITY', "2016")
mapGenerator(data, 'SEVERITY', "2017")
mapGenerator(data, 'SEVERITY', "2018")

mapGenerator(data, 'ALCOHOL_RELATED', "2013")
mapGenerator(data, 'ALCOHOL_RELATED', "2014")
mapGenerator(data, 'ALCOHOL_RELATED', "2015")
mapGenerator(data, 'ALCOHOL_RELATED', "2016")
mapGenerator(data, 'ALCOHOL_RELATED', "2017")
mapGenerator(data, 'ALCOHOL_RELATED', "2018")

mapGenerator(data, 'HIT_RUN_FLAG', "2013")
mapGenerator(data, 'HIT_RUN_FLAG', "2014")
mapGenerator(data, 'HIT_RUN_FLAG', "2015")
mapGenerator(data, 'HIT_RUN_FLAG', "2016")
mapGenerator(data, 'HIT_RUN_FLAG', "2017")
mapGenerator(data, 'HIT_RUN_FLAG', "2018")