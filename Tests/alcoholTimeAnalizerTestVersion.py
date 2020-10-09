#A function that can acheive: Allow the user to analyse the impact of alcohol time in accidents� ie: trends over days, the relationship with dark street lights, etc.
import matplotlib.pyplot as plt
import pandas
import numpy as np
#alcoholTimeAnalizer is the name of the 4th function that the program performs, it takes all of the data, and a name as inputs and creates 1 of 4 graphs based on alcohol time and the name input.
#the graphs have been removed for testing purposes
def alcoholTimeAnalizer(data, name):
    if (type(data) == pandas.core.frame.DataFrame):
        data = data[[col for col in data]]
        nRow, nCol = data.shape
        if name in data:
            if (name == 'DAY_OF_WEEK'):
                trueBarData = {'Mon': 0, 'Tues': 0, 'Wed': 0, 'Thurs': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}
                falseBarData = {'Mon': 0, 'Tues': 0, 'Wed': 0, 'Thurs': 0, 'Fri': 0, 'Sat': 0, 'Sun': 0}
                for index, row in data.iterrows():
                    if (row['DAY_OF_WEEK'] == "Monday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Mon"] +=1
                        else:
                            falseBarData["Mon"] +=1
                    elif (row['DAY_OF_WEEK'] == "Tuesday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Tues"] +=1
                        else:
                            falseBarData["Tues"] +=1
                    elif (row['DAY_OF_WEEK'] == "Wednesday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Wed"] +=1
                        else:
                            falseBarData["Wed"] +=1
                    elif (row['DAY_OF_WEEK'] == "Thursday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Thurs"] +=1
                        else:
                            falseBarData["Thurs"] +=1
                    elif (row['DAY_OF_WEEK'] == "Friday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Fri"] +=1
                        else:
                            falseBarData["Fri"] +=1
                    elif (row['DAY_OF_WEEK'] == "Saturday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Sat"] +=1
                        else:
                            falseBarData["Sat"] +=1
                    elif (row['DAY_OF_WEEK'] == "Sunday"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Sun"] +=1
                        else:
                            falseBarData["Sun"] +=1
                #Graph was here
                return 'Success'
            elif (name == 'LIGHT_CONDITION'):
                trueBarData = {'Day': 0, 'Street lights on': 0, 'Dusk/Dawn': 0, 'No street lights': 0, 'Unk.': 0}
                falseBarData = {'Day': 0, 'Street lights on': 0, 'Dusk/Dawn': 0, 'No street lights': 0, 'Unk.': 0}
                for index, row in data.iterrows():
                    if (row['LIGHT_CONDITION'] == "Day"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Day"] +=1
                        else:
                            falseBarData["Day"] +=1
                    elif (row['LIGHT_CONDITION'] == "Dark Street lights on"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Street lights on"] +=1
                        else:
                            falseBarData["Street lights on"] +=1
                    elif (row['LIGHT_CONDITION'] == "Dusk/Dawn"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Dusk/Dawn"] +=1
                        else:
                            falseBarData["Dusk/Dawn"] +=1
                    elif (row['LIGHT_CONDITION'] == "Dark No street lights"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["No street lights"] +=1
                        else:
                            falseBarData["No street lights"] +=1
                    elif (row['LIGHT_CONDITION'] == "Unk."):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Unk."] +=1
                        else:
                            falseBarData["Unk."] +=1
                #Graph was here
                return 'Success'
            elif (name == 'ALCOHOL_RELATED'):
                trueBarData = {'Yes': 0, 'No': 0}
                falseBarData = {'Yes': 0, 'No': 0}
                for index, row in data.iterrows():
                    if (row['ALCOHOL_RELATED'] == "Yes"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Yes"] +=1
                        else:
                            falseBarData["Yes"] +=1
                    elif (row['ALCOHOL_RELATED'] == "No"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["No"] +=1
                        else:
                            falseBarData["No"] +=1
                #Graph was here
                return 'Success'
            elif (name == 'SEVERITY'):
                trueBarData = {'Other': 0, 'Serious': 0, 'Fatal': 0, 'None': 0}
                falseBarData = {'Other': 0, 'Serious': 0, 'Fatal': 0, 'None': 0}
                for index, row in data.iterrows():
                    if (row['SEVERITY'] == "Other injury accident"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Other"] +=1
                        else:
                            falseBarData["Other"] +=1
                    elif (row['SEVERITY'] == "Serious injury accident"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Serious"] +=1
                        else:
                            falseBarData["Serious"] +=1
                    elif (row['SEVERITY'] == "Fatal accident"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["Fatal"] +=1
                        else:
                            falseBarData["Fatal"] +=1
                    elif (row['SEVERITY'] == "Non injury accident"):
                        if (row['ALCOHOLTIME'] == "Yes"):
                            trueBarData["None"] +=1
                        else:
                            falseBarData["None"] +=1
                #Graph was here
                return 'Success'
            else:
                return 'Incorrect Data or Name'
        else:
            return 'Incorrect Data or Name'
    else:
        return 'Incorrect Data Type'