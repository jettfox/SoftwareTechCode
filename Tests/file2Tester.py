import unittestimport pandas as pdfrom file2Test import sortHourOfDayfrom file_loader import fileloaderfrom file_loader import badfileLoaderalteredfile = badfileLoader()emptydf = pd.DataFrame({'' : []})emptyName = NonewrongData = [1,2,3,4,5,6]emptyData = NoneincorrectName = 'jett'# neither can have an incorrect value for the input# file 2 it is only used in a title# file 3 incorrect data will come up with no matches but will not break anythinginput1 = 'PED'input2 = '2017/10/05'#Valid Data: datadata = fileloader()class testsortHourOfDay(unittest.TestCase):    def testCorrectDataCorrectName(self):        result = sortHourOfDay(data, input1, input2)        self.assertEqual(result, 'Success')            def testCorrectDataNoName(self):         result = sortHourOfDay(data, emptyName, emptyName)         self.assertEqual(result, 'Success')            def testCorrectDataIntName(self):        result = sortHourOfDay(data, 2, 10)        self.assertEqual(result, 'Success')            def testEmptyDataName1(self):        result = sortHourOfDay(emptyData, input1, input1)        self.assertEqual(result, 'Invalid Data')            def testAlteredDatainput1(self):        result = sortHourOfDay(alteredfile, input1, input1)        self.assertEqual(result, 'Incorrect Data')            def testAlteredDataIncorrectName(self):        result = sortHourOfDay(alteredfile, incorrectName, input1)        self.assertEqual(result, 'Incorrect Data')            def testEmptyDataIncorrectName(self):        result = sortHourOfDay(emptydf, incorrectName, input1)        self.assertEqual(result, 'Incorrect Data')            def testEmptyDataEmptyName(self):        result = sortHourOfDay(emptydf, emptyName, input1)        self.assertEqual(result, 'Incorrect Data')if __name__ =='__main__':    unittest.main()