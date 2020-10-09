#A function that can acheive: One other ‘insight’ or analysis tool of your choice
import matplotlib.pyplot as plt
import pandas
#mapGenerator is the name of the 5th function that the program performs, it takes all of the data, and a maptype and year as inputs and creates 1 of 3 graphs types of scatter plots on map based on maptime and only includes the data from the year specified
#the graphs have been removed for testing purposes
def mapGenerator(data, mapType, year):
    if (type(data) == pandas.core.frame.DataFrame):
        imgMap = plt.imread('map.png')
        data = data[[col for col in data]]
        nRow, nCol = data.shape
        if mapType in data:
            limits = ((data['LONGITUDE'].min(), data['LONGITUDE'].max(), data['LATITUDE'].min(), data['LATITUDE'].max()))
            if (mapType == 'SEVERITY'):
                oLong = []
                oLat = []
                sLong = []
                sLat = []
                fLong = []
                fLat = []
                nLong = []
                nLat = []
                for index, row in data.iterrows():
                    if (row['ACCIDENT_DATE'].split('/')[2] == year):
                        if (row['SEVERITY'] == "Other injury accident"):
                            oLong.append(row['LONGITUDE'])
                            oLat.append(row['LATITUDE'])
                        elif (row['SEVERITY'] == "Serious injury accident"):
                            sLong.append(row['LONGITUDE'])
                            sLat.append(row['LATITUDE'])
                        elif (row['SEVERITY'] == "Fatal accident"):
                            fLong.append(row['LONGITUDE'])
                            fLat.append(row['LATITUDE'])
                        elif (row['SEVERITY'] == "Non injury accident"):
                            nLong.append(row['LONGITUDE'])
                            nLat.append(row['LATITUDE'])
                if (len(oLong) < 1 or len(sLong) < 1 or len(fLong) < 1):
                    return 'Incorrect Year'
                else:
                    #Graph was here
                    return 'Success'
            elif (mapType == 'ALCOHOL_RELATED'):
                aLong = []
                aLat = []
                sLong = []
                sLat = []
                for index, row in data.iterrows():
                    if (row['ACCIDENT_DATE'].split('/')[2] == year):
                        if (row['ALCOHOL_RELATED'] == "Yes"):
                            aLong.append(row['LONGITUDE'])
                            aLat.append(row['LATITUDE'])
                        elif (row['ALCOHOL_RELATED'] == "No"):
                            sLong.append(row['LONGITUDE'])
                            sLat.append(row['LATITUDE'])
                    
                if (len(aLong) < 1 or len(sLong) < 1):
                    return 'Incorrect Year'
                else:
                    #Graph was here
                    return 'Success'
            elif (mapType == 'HIT_RUN_FLAG'):
                yLong = []
                yLat = []
                nLong = []
                nLat = []
                for index, row in data.iterrows():
                    if (row['ACCIDENT_DATE'].split('/')[2] == year):
                        if (row['HIT_RUN_FLAG'] == "Yes"):
                            yLong.append(row['LONGITUDE'])
                            yLat.append(row['LATITUDE'])
                        elif (row['HIT_RUN_FLAG'] == "No"):
                            nLong.append(row['LONGITUDE'])
                            nLat.append(row['LATITUDE'])
                if (len(yLong) < 1 or len(nLong) < 1):
                    return 'Incorrect Year'
                else:
                    #Graph was here
                    return 'Success'
            else:
                return 'Incorrect Data or mapType'
        else:
            return 'Incorrect mapType'
    else:
        return 'Incorrect Data Type'
