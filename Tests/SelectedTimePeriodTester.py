import unittest

from SelectedTimePeriodTestVersion import select_Time_Period



#valid start and end dates
vStart = '12/12/2015'
vEnd = '05/05/2017'
#not valid
bStart = '2015/04/01'
bEnd = '2017/01/04'
#empty
eStart = ''
eEnd = ''
#str
sStart = 'ow/ow/wood'
sEnd = 'wo/wo/doow'

# neither can have an incorrect value for the input
# file 2 it is only used in a title
# file 3 incorrect data will come up with no matches but will not break anything


class testselect_Time_Period(unittest.TestCase):
    def testCorrectStartCorrectEnd(self):
        result = select_Time_Period(vStart, vEnd)
        self.assertEqual(result, 'Success')
        
    def testIncorrectStartIncorrectEnd(self):
        result = select_Time_Period(bStart, bEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testCorrectStartIncorrectEnd(self):
        result = select_Time_Period(vStart, bEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testIncorrectStartCorrectEnd(self):
        result = select_Time_Period(bStart, vEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testEmptyStartEmptyEnd(self):
        result = select_Time_Period(eStart, eEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testCorrectStartEmptyEnd(self):
        result = select_Time_Period(vStart, eEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testEmptyStartCorrectEnd(self):
        result = select_Time_Period(eStart, vEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testStringStartStringEnd(self):
        result = select_Time_Period(sStart, sEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testStringStartCorrectEnd(self):
        result = select_Time_Period(sStart, vEnd)
        self.assertEqual(result, 'Invalid Date')
        
    def testCorrectStartStringEnd(self):
        result = select_Time_Period(vStart, sEnd)
        self.assertEqual(result, 'Invalid Date')



if __name__ =='__main__':
    unittest.main()