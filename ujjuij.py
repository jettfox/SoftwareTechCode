import io
import wx
import pandas
import numpy as np
import matplotlib.pyplot as plt
from file_loader import fileloader


class MainPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        self.SetSize((1024,768))
        self.SetBackgroundColour('yellow')
        
        #Generate Sample Graph
        data = fileloader()
        name = 'DAY_OF_WEEK'
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
                labels = trueBarData.keys()
                true = trueBarData.values()
                false = falseBarData.values()
                x = np.arange(len(labels))
                width = 0.2
                fig, ax = plt.subplots()
                rects1 = ax.bar(x - width/2, true, width, label='True', color='#0F084B')
                rects2 = ax.bar(x + width/2, false, width, label='False', color='#3AA7A3')
                
                ax.set_ylabel('Crashes')
                ax.set_xlabel('Days of the Week')
                ax.set_title('Crashes by Alcohol Time')
                ax.set_xticks(x)
                ax.set_xticklabels(labels)
                ax.legend()
                fig.tight_layout()
                plt.show()
#        t = np.arange(0.0, 2.0, 0.01)
#       s = 1 + np.sin(2 * np.pi * t)
 #       fig, ax = plt.subplots()
  #      ax.plot(t, s)
#
 #       ax.set(xlabel='time (s)', ylabel='voltage (mV)',
  #             title='About as simple as it gets, folks')
   #     ax.grid()
#       buf = io.BytesIO()
 #       plt.savefig(buf,format='png')
  #      buf.seek(0)
#
 #       self.Image = wx.Image(buf, wx.BITMAP_TYPE_ANY)
  #      self.Image = wx.StaticBitmap(self, wx.ID_ANY, 
   #                                      wx.Bitmap(self.Image))
    #    self.sizer = wx.BoxSizer(wx.HORIZONTAL)
     #   self.sizer.Add(self.Image,1,wx.ALIGN_CENTRE)
      #  self.SetSizer(self.sizer)

class MyForm(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY,
            "Graph to Image Test", size=(1024,768))
        self.panel = MainPanel(self)


if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm()
    frame.Show()
    app.MainLoop()