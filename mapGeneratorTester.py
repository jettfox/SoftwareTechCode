import unittest
import pandas as pd
from mapGenerator import mapGenerator
from file_loader import fileloader
from file_loader import badfileLoader

alteredfile = badfileLoader()

emptydf = pd.DataFrame({'' : []})

wrongData = [1,2,3,4,5,6]

emptyData = None

incorrectYear = '2012'

emptyYear = None

incorrectMapType = 'LIGHT_CONDITION'

emptyMapType = None

# Valid Map Types: SEVERITY, ALCOHOL_RELATED, HIT_RUN_FLAG

correctMapType1 = 'SEVERITY'

correctMapType2 = 'ALCOHOL_RELATED'

correctMapType3 = 'HIT_RUN_FLAG'

# Valid years: 2013, 2014, 2015, 2016, 2017, 2018
correctYear1 = '2013'

correctYear2 = '2014'

correctYear3 = '2015'

correctYear4 = '2016'

correctYear5 = '2017'

correctYear6 = '2018'

#Valid Data: data
data = fileloader()


class testMapGenerator(unittest.TestCase):
    
    def testCorrectMapType1CorrectYear1(self):
        result = mapGenerator(data, correctMapType1, correctYear1)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType2CorrectYear1(self):
        result = mapGenerator(data, correctMapType2, correctYear1)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType3CorrectYear1(self):
        result = mapGenerator(data, correctMapType3, correctYear1)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType1CorrectYear2(self):
        result = mapGenerator(data, correctMapType1, correctYear2)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType1CorrectYear3(self):
        result = mapGenerator(data, correctMapType1, correctYear3)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType1CorrectYear4(self):
        result = mapGenerator(data, correctMapType1, correctYear4)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType1CorrectYear5(self):
        result = mapGenerator(data, correctMapType1, correctYear5)
        self.assertEqual(result, 'Success')
        
    def testCorrectMapType1CorrectYear6(self):
        result = mapGenerator(data, correctMapType1, correctYear6)
        self.assertEqual(result, 'Success')
   
    def testCorrectMapType1IncorrectYear(self):
        result = mapGenerator(data, correctMapType1, incorrectYear)
        self.assertEqual(result, 'Incorrect Year')
        
    def testCorrectMapType1EmptyYear(self):
        result = mapGenerator(data, correctMapType1, emptyYear)
        self.assertEqual(result, 'Incorrect Year')
        
    def testIncorrectMapTypeCorrectYear1(self):
        result = mapGenerator(data, incorrectMapType, correctYear1)
        self.assertEqual(result, 'Incorrect Data or mapType')
        
    def testEmptyMapTypeCorrectYear1(self):
        result = mapGenerator(data, emptyMapType, correctYear1)
        self.assertEqual(result, 'Incorrect mapType')
        
    def testCorrectMapType1CorrectYear1IncorrectData(self):
        result = mapGenerator(wrongData, correctMapType1, correctYear1)
        self.assertEqual(result, 'Incorrect Data Type')
        
    def testCorrectMapType1CorrectYear1IncorrectDataFrame(self):
        result = mapGenerator(emptydf, correctMapType1, correctYear1)
        self.assertEqual(result, 'Incorrect mapType')
        
    def testCorrectMapType1CorrectYear1EmptyData(self):
        result = mapGenerator(emptyData, correctMapType1, correctYear1)
        self.assertEqual(result, 'Incorrect Data Type')
        
    def testEmptyMapTypeCorrectYear1EmptyData(self):
        result = mapGenerator(emptyData, emptyMapType, correctYear1)
        self.assertEqual(result, 'Incorrect Data Type')
        
    def testCorrectMapTypeEmptyYear1EmptyData(self):
        result = mapGenerator(emptyData, correctMapType1, emptyYear)
        self.assertEqual(result, 'Incorrect Data Type')
        
    def testEmptyMapTypeEmptyYear1EmptyData(self):
        result = mapGenerator(emptyData, emptyMapType, emptyYear)
        self.assertEqual(result, 'Incorrect Data Type')

if __name__ =='__main__':
    unittest.main()