import unittest
import pandas as pd
from SelectedTimePeriodTest import select_Time_Period

badinput1 = 'PED'
Nullinput = None
goodinput1 = '2016/06/06'
goodinput2 = '2017/10/05'

class testsortHourOfDay(unittest.TestCase):
    # file 2
    def testCorrectDataCorrectName(self):
        result = select_Time_Period(goodinput1, goodinput2)
        self.assertEqual(result, 'Success')
        
    def testCorrectDataNoName(self):
        result = sortHourOfDay(Nullinput, Nullinput)
        self.assertEqual(result, 'Invalid Date')
        
    def testCorrectDataBadinput1(self):
        result = sortHourOfDay(goodinput1, badinput1)
        self.assertEqual(result, 'Invalid Date')
    
    def testCorrectDataBadinput2(self):
        result = sortHourOfDay(data, badinput1, goodinput2)
        self.assertEqual(result, 'Invalid Date')

if __name__ =='__main__':
    unittest.main()