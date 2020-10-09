import unittest
import pandas as pd
from sortHourDayTestVersion import sortHourOfDay
from file_loader import fileloader
from file_loader import badfileLoader

alteredfile = badfileLoader()
emptydf = pd.DataFrame({'' : []})
emptyName = None
wrongData = [1,2,3,4,5,6]
emptyData = None
incorrectName = 'jett'


# neither can have an incorrect value for the input
# file 2 it is only used in a title
# file 3 incorrect data will come up with no matches but will not break anything

#Valid Data: data
data = fileloader()


class testsortHourOfDay(unittest.TestCase):
    def testCorrectData(self):
        result = sortHourOfDay(data)
        self.assertEqual(result, 'Success')
        
    def testAlteredData(self):
        result = sortHourOfDay(alteredfile)
        self.assertEqual(result, 'Incorrect Data')
        
    def testEmptyData(self):
        result = sortHourOfDay(emptydf)
        self.assertEqual(result, 'Incorrect Data')



if __name__ =='__main__':
    unittest.main()