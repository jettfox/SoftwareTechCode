# For a user-selected period, (DONE)
# E.G. animal, ped. (user entered)
# Retrieve all accidents that contains a keyword In the DCA_CODE,

from selectedtimeperiod import select_Time_Period
data = select_Time_Period()

Keyword = input('Enter Keyword: ')


#%%

for lineNo in range(len(data['DCA_CODE'])):
    currkeywords = []
    currCode = data['DCA_CODE'][lineNo]
    currkeywords = currCode.split()
    
    if (Keyword in currkeywords):
        #savedata
        print('placeholder code')
