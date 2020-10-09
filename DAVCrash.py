import wx
import matplotlib.pyplot as plt
from wx.lib.plot import PlotCanvas
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
from file_loader import fileloader as fl
from main import alcoholTimeAnalizer as ata
data = fl()

class RightPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
       # panel = wx.Panel(self, -1)
      #  self.figure = plt.figure()
     #   #self.figureTest = self.figure.add_subplot(111)
    #    #self.axes = self.figure.add_subplot(111)
   #     self.canvas = PlotCanvas(panel)
  #      self.canvas.Draw(ata(data, 'DAY_OF_WEEK'))
 #       self.sizer = wx.BoxSizer(wx.VERTICAL)
        #Add canvas to sizer
       # self.sizer.Add(self.canvas, 1, wx.EXPAND)
       # self.SetSizer(self.sizer)
        
        
#    def draw(self):
  #      alcTimeGraph = ata(data, 'DAY_OF_WEEK')
   #     self.canvas.draw()
        
 #   def alcTime(self, valString):
  #      print(f'{valString} We got here')
   #     alcTimeGraph = 111
    #    if (valString == 'DAY_OF_WEEK'):
     #       ata(data, 'DAY_OF_WEEK')
      #  elif (valString == 'LIGHT_CONDITION'):
       #     alcTimeGraph = ata(data, 'LIGHT_CONDITION')
        #elif (valString == 'ALCOHOL_RELATED'):
        #    alcTimeGraph = ata(data, 'ALCOHOL_RELATED')
        #elif (valString == 'SEVERITY'):
        #    alcTimeGraph = ata(data, 'SEVERITY')
        #print(alcTimeGraph)
        #return self.figureTest.plot(alcTimeGraph)
    
    
        



class LeftPanel(wx.Panel):
    def __init__(self, parent, right):
        wx.Panel.__init__(self, parent = parent)
        #Create main and give background colour
        self.leftMainPanel = wx.Panel(self)
        self.leftMainPanel.SetBackgroundColour((144, 164, 174))
        #Create function title and give background colour
        self.func3Title = wx.StaticText(self.leftMainPanel, -1, "Function One", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.func3Title.SetBackgroundColour((207, 217, 220))
        #Create function description and give background colour
        self.func3Desc = wx.StaticText(self.leftMainPanel, -1, "Function One Description.\nThis is a description for function one", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER|wx.TE_MULTILINE)
        self.func3Desc.SetBackgroundColour((207, 217, 220))
        #List of choices to be passed into drop down
        func3Choices = ['Day of the week', 'Light condition', 'Alcohol related', 'Severity']
        #Drop down menu for selecting options
        self.func3Choice = wx.Choice(self.leftMainPanel, -1, wx.DefaultPosition, wx.DefaultSize, func3Choices, 0)
        #Set Default selection to first index
        self.func3Choice.SetSelection(0)
        #Create button 
        self.func3Btn = wx.Button(self.leftMainPanel, -1, 'Generate', wx.DefaultPosition, wx.DefaultSize, 5)
        #Bind button event -> f3OnClick
        self.func3Btn.Bind(wx.EVT_BUTTON, self.f3OnClick, self.func3Btn)
        
        
        #Sizers declarations
        sizerMain = wx.BoxSizer(wx.VERTICAL) #Sizer for highest level panel (DO NOT TOUCH)
        mainSizer = wx.BoxSizer(wx.VERTICAL) #Sizer for highest level panel (DO NOT TOUCH)
        sizerLeftInterior = wx.BoxSizer(wx.VERTICAL) #Sizer that sits inside highest level panel
        #Add new sizers above or below for each function required
        sizerFunc3Title = wx.BoxSizer(wx.HORIZONTAL) #Title Sizer
        sizerFunc3Desc = wx.BoxSizer(wx.HORIZONTAL) #Desciption Sizer
        sizerFunc3Buttons = wx.BoxSizer(wx.HORIZONTAL) #Selection element sizer
        
        #Add elements to sizers
        sizerFunc3Title.Add(self.func3Title, -1, wx.ALL|wx.EXPAND|wx.CENTER, 0)
        sizerFunc3Desc.Add(self.func3Desc, -1, wx.ALL|wx.EXPAND|wx.CENTER, 0)
        sizerFunc3Buttons.Add(self.func3Choice, -1, wx.ALL, 5)
        sizerFunc3Buttons.Add(self.func3Btn, -1, wx.ALL|wx.SHAPED, 5)
        
        
        #Add sizers to main sizer
        #Add above or below for panel position
        #wx.ALL == all borders
        #wx.EXPAND == expand to full width of sizer
        #wx.CENTER == position in center
        sizerLeftInterior.Add(sizerFunc3Title, 0, wx.ALL|wx.EXPAND|wx.CENTER, 5)
        sizerLeftInterior.Add(sizerFunc3Desc, 0, wx.ALL|wx.EXPAND|wx.CENTER, 5)
        sizerLeftInterior.Add(sizerFunc3Buttons, 0, wx.ALL|wx.EXPAND, 5)
        
        
        #Top level sizers (keep at bottom)
        self.leftMainPanel.SetSizer(sizerLeftInterior)
        self.leftMainPanel.Layout()
        mainSizer.Add(self.leftMainPanel, 1, wx.EXPAND, 0)
        sizerMain.Add(mainSizer, 1, wx.EXPAND, 0)
        self.SetSizer(sizerMain)
        self.Layout()
        
        
        
        #For referencing 
        self.graph = right
        
    def f3OnClick(self, event):
        #This returns the index of the choice
        val = self.func3Choice.GetSelection()
        valString = ''
        if (val == 0):
            ata(data, 'DAY_OF_WEEK')
        elif (val == 1):
            ata(data, 'LIGHT_CONDITION')
        elif (val == 2):
            ata(data, 'ALCOHOL_RELATED')
        elif (val == 3):
            ata(data, 'SEVERITY')
            
        #Call function on right panel to draw graph
        self.graph.alcTime(valString)
        
        
        
        
        
        
        
        
        
        
        
class Main(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="DAVCrash", size=(500, 500))
        #Create menu bar
        self.menuBarMain = wx.MenuBar(0)
        self.menuFile = wx.Menu()
        #Add about button to menu bar with status bar details
        self.menuItemFileAbout = wx.MenuItem(self.menuFile, wx.ID_ANY, "About",
                                             "Details about this program")
        #Add about button to menuFile
        self.menuFile.Append(self.menuItemFileAbout)
        #Add help button to menu bar with status bar details
        self.menuItemFileHelp = wx.MenuItem(self.menuFile, wx.ID_ANY, "Help",
                                            "View documentation for this application")
        #Add help button to menuFile
        self.menuFile.Append(self.menuItemFileHelp)
        #Add separator
        self.menuFile.AppendSeparator()
        #Add exit button to menu bar with status bar details
        self.menuItemFileExit = wx.MenuItem(self.menuFile, wx.ID_ANY, "Exit",
                                            "Exit DAVCrash")
        #Add exit button to menuFile
        self.menuFile.Append(self.menuItemFileExit)
        self.menuFile.Bind(wx.EVT_MENU, self.ExitProgram, self.menuItemFileExit)
        
        #Create clickable menu button
        self.menuBarMain.Append(self.menuFile, "File")
        #Generate menuBar
        self.SetMenuBar(self.menuBarMain)
        splitter = wx.SplitterWindow(self)
        right = RightPanel(splitter)
        left = LeftPanel(splitter, right)
        splitter.SplitVertically(left, right)
        splitter.SetMinimumPaneSize(300)
        #TODO if here??
        #right.draw()
        #right.alcTime(RightPanel.alcTime)
        
    def ExitProgram(self, event):
        self.Close()
        
        
if __name__ == '__main__':
    app = wx.App()
    frame = Main()
    frame.Show()
    app.MainLoop()