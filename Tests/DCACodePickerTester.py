import unittest
import pandas as pd
from DCACodePickerTestVersion import DCACodePicker
from SelectedTimePeriod import select_Time_Period
from file_loader import fileloader
from file_loader import badfileLoader

alteredfile = badfileLoader()
emptydf = pd.DataFrame({'' : []})
emptyName = None
wrongData = [1,2,3,4,5,6]
emptyData = None
incorrectName = 'BADNESS'


# neither can have an incorrect value for the input
# file 2 it is only used in a title
# file 3 incorrect data will come up with no matches but will not break anything

input1 = 'PED'
start = '05/10/2015'
end = '05/10/2016'

#Valid Data: data
data = fileloader()
goodData = select_Time_Period( start, end)


class DCACodePickerTester(unittest.TestCase):

    def testCorrectDataCorrectName3(self):
        result = DCACodePicker(goodData, input1)
        self.assertEqual(result, 'Success')
        
    def testCorrectDataNoName3(self):
        result = DCACodePicker(goodData, emptyName)
        self.assertEqual(result, 'No Search Term Supplied')
        
    def testEmptyDataName3(self):
        result = DCACodePicker(emptyData, input1)
        self.assertEqual(result, 'Unknown Error')
        
    def testAlteredDataCorrectName3(self):
        result = DCACodePicker(alteredfile, input1)
        self.assertEqual(result, 'Incorrect Data')
        
    def testAlteredDataIncorrectName3(self):
        result = DCACodePicker(alteredfile, incorrectName)
        self.assertEqual(result, 'Incorrect Data')
        
    def testEmptyDataIncorrectName3(self):
        result = DCACodePicker(emptydf, incorrectName)
        self.assertEqual(result, 'Incorrect Data')
        
    def testEmptyDataEmptyName(self):
        result = DCACodePicker(emptydf, emptyName)
        self.assertEqual(result, 'Incorrect Data')


if __name__ =='__main__':
    unittest.main()