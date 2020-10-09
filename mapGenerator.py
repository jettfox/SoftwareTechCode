#A function that can acheive: One other ‘insight’ or analysis tool of your choice
import matplotlib.pyplot as plt
import pandas
#mapGenerator is the name of the 5th function that the program performs, it takes all of the data, and a maptype and year as inputs and creates 1 of 3 graphs types of scatter plots on map based on maptime and only includes the data from the year specified
def mapGenerator(data, mapType, year):
    #makes sure that the data is a dataframe
    if (type(data) == pandas.core.frame.DataFrame):
        #this takes the map.png image which is an image of a map of victoria at the max and min longitudes and latitudes of this database
        imgMap = plt.imread('map.png')
        #this makes sure that the dataframe is formatted properly
        data = data[[col for col in data]]
        nRow, nCol = data.shape
        #this check whether maptype input is a collumn in the dataframe
        if mapType in data:
            #this sets the limits for the scatterplot that are used later
            limits = ((data['LONGITUDE'].min(), data['LONGITUDE'].max(), data['LATITUDE'].min(), data['LATITUDE'].max()))
            #if the maptype is severity then do this branch
            if (mapType == 'SEVERITY'):
                #these are the empty arrays that will filled with dataframe data
                oLong = []
                oLat = []
                sLong = []
                sLat = []
                fLong = []
                fLat = []
                nLong = []
                nLat = []
                #this goes line by line in the dataframe to check whether collumn severity is set to a specified category and the for that is put in its corresponding array
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
                #if there is no data then the year inputed doesn't have data for it
                if (len(oLong) < 1 or len(sLong) < 1 or len(fLong) < 1):
                    return 'Incorrect Year'
                else:
                    #this sets up the ax plot that has subplots
                    fig, ax = plt.subplots(figsize = (8,7))
                    #these are scatter sub plots that place a dot at the coresponding coordinates of an accident, the colour of the dot is based on the severity
                    ax.scatter(nLong, nLat, zorder=1, alpha= 0.3, label ='No Injury', c='#E7E393', s=5)
                    ax.scatter(oLong, oLat, zorder=1, alpha= 0.5, label ='Other Injury', c='#F4C95D', s=5)
                    ax.scatter(sLong, sLat, zorder=1, alpha= 0.7, label ='Serious Injury', c='#DD7230', s=5)
                    ax.scatter(fLong, fLat, zorder=1, alpha= 0.9, label ='Fatality', c='#AB2346', s=5)
                    #title has the inputed year included
                    title = 'Map of Victoria Crashes by Severity in '+year
                    ax.set_title(title)
                    ax.set_xlim(limits[0],limits[1])
                    ax.set_ylim(limits[2],limits[3])
                    ax.set_ylabel('Latitude')
                    ax.set_xlabel('Longitude')
                    ax.legend()
                    #this shows the scatter plot with the image as the background
                    ax.imshow(imgMap, zorder=0, extent = limits, aspect= 'equal')
                    plt.show()
                    return 'Success'
            #these other ifs work the same as above but with a different collum being targeted, it would be a waste to comment each one
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
                    fig, ax = plt.subplots(figsize = (8,7))
                    ax.scatter(sLong, sLat, zorder=1, alpha= 1, label ='No', c='#767481', s=2)
                    ax.scatter(aLong, aLat, zorder=1, alpha= 1, label ='Yes', c='#09090B', s=2)
                    title = 'Map of Victoria Crashes whether Alcohol Related in '+year
                    ax.set_title(title)
                    ax.set_xlim(limits[0],limits[1])
                    ax.set_ylim(limits[2],limits[3])
                    ax.set_ylabel('Latitude')
                    ax.set_xlabel('Longitude')
                    ax.legend()
                    ax.imshow(imgMap, zorder=0, extent = limits, aspect= 'equal')
                    plt.show()
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
                    fig, ax = plt.subplots(figsize = (8,7))
                    ax.scatter(nLong, nLat, zorder=1, alpha= 1, label ='No', c='#767481', s=2)
                    ax.scatter(yLong, yLat, zorder=1, alpha= 1, label ='Yes', c='#09090B', s=2)
                    title = 'Map of Victoria Crashes Whether Hit and Run in '+year
                    ax.set_title(title)
                    ax.set_xlim(limits[0],limits[1])
                    ax.set_ylim(limits[2],limits[3])
                    ax.set_ylabel('Latitude')
                    ax.set_xlabel('Longitude')
                    ax.legend()
                    ax.imshow(imgMap, zorder=0, extent = limits, aspect= 'equal')
                    plt.show()
                    return 'Success'
            else:
                return 'Incorrect Data or mapType'
        else:
            return 'Incorrect mapType'
    else:
        return 'Incorrect Data Type'
