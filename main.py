from file4 import alcoholTimeAnalizer
from file_loader import fileloader
data = fileloader()
alcoholTimeAnalizer(data,'DAY_OF_WEEK')
alcoholTimeAnalizer(data,'LIGHT_CONDITION')
alcoholTimeAnalizer(data,'ALCOHOL_RELATED')
alcoholTimeAnalizer(data,'SEVERITY')