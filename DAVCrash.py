try:
    import wx
except ImportError:
    raise ImportError("The Python wx module is required to run this program.")
try:
    from file_loader import fileloader as fl
except ImportError:
    raise ImportError("Failed to import fileloader.")
try:
    from main import alcoholTimeAnalizer as ata
except ImportError:
    raise ImportError("Failed to import alcoholTimeAnalizer.")
try:
    from main import mapGenerator as mG
except ImportError:
    raise ImportError("Failed to import mapGenerator")
try:
    from SelectedTimePeriod import select_Time_Period as sTP
except ImportError:
    raise ImportError("Failed to import selectedTimePeriod")
try:
    from sortHourDay import sortHourOfDay as sHD
except ImportError:
    raise ImportError("Faied to import sortHourDay")
try:
    from DCACodePicker import DCACodePicker as DCP
except ImportError:
    raise ImportError("Failed to import DCACodePicker")

#Declare data value from fileloader    
data = fl()

class myGui(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, pos=wx.DefaultPosition, size=(1000, 800))
        self.parent = parent
        self.initialise()

    def initialise(self):
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        # MenuBar
        self.menuBarMain = wx.MenuBar(0)
        self.menuFile = wx.Menu()
        # File 'button' to menu bar
        self.menuBarMain.Append(self.menuFile, "File")
        # Menu about 'button'
        self.menuItemFileAbout = wx.MenuItem(
            self.menuFile, wx.ID_ANY, "About", "Details about this program.", wx.ITEM_NORMAL)
        self.menuFile.Append(self.menuItemFileAbout)
        # Menu help 'button'
        self.menuItemFileHelp = wx.MenuItem(
            self.menuFile, wx.ID_ANY, "Help", "Access documentation for this program", wx.ITEM_NORMAL)
        self.menuFile.Append(self.menuItemFileHelp)
        # Add divider line
        self.menuFile.AppendSeparator()
        # Menu exit 'button'
        self.menuItemFileExit = wx.MenuItem(
            self.menuFile, wx.ID_ANY, "Exit", "Exit DAVCrash", wx.ITEM_NORMAL)
        self.menuFile.Append(self.menuItemFileExit)
        # Set menubar
        self.SetMenuBar(self.menuBarMain)
        # Add status bar
        self.m_statusBar = self.CreateStatusBar(1, wx.STB_SIZEGRIP, wx.ID_ANY)
        
        panel = wx.Panel(self)
        # Main Frame setup
        FrameMainSizer = wx.BoxSizer(wx.VERTICAL)
        MainFrameSizer = wx.BoxSizer(wx.VERTICAL)
        
        self.panelMain = wx.Panel(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.panelMain.SetBackgroundColour(wx.Colour(47, 56, 61))
        # Content inside of main frame
        gSizerMain = wx.GridSizer(2, 2, 0, 0)
        
        # Function 1
        self.panelDef1 = wx.Panel(
            self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerPanelDef1 = wx.BoxSizer(wx.VERTICAL)
        # Add title via text control & set a background colour
        # TODO Rename function1
        self.func1Title = wx.StaticText(
            self.panelDef1, wx.ID_ANY, "function1", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        self.func1Title.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        # Expand title to full grid width
        sizerPanelDef1.Add(self.func1Title, 0, wx.ALL | wx.EXPAND, 5)
        # Add description of what this function will do
        # TODO Change description str (multiline)
        self.func1Desc = wx.StaticText(self.panelDef1, wx.ID_ANY, "This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.func1Desc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        # Add function1 description to panelDef1
        sizerPanelDef1.Add(self.func1Desc, 0, wx.ALL | wx.EXPAND, 5)
        # Add horizontal sizer to bottom of function1 panel
        sizerFunc1 = wx.BoxSizer(wx.HORIZONTAL)
        # Add function selector
        # TODO change input string names
        self.func1Input1 = wx.TextCtrl(self.panelDef1, wx.ID_ANY, 'TODOInput1', wx.DefaultPosition, wx.DefaultSize)
        sizerFunc1.Add(self.func1Input1, 0, wx.ALL, 5)
        self.func1Input2 = wx.TextCtrl(self.panelDef1, wx.ID_ANY, 'TODOInput1', wx.DefaultPosition, wx.DefaultSize)
        sizerFunc1.Add(self.func1Input2, 0, wx.ALL, 5)
        # Add selection button to execute the function
        self.func1Btn = wx.Button(self.panelDef1, wx.ID_ANY, 'Generate', wx.DefaultPosition, wx.DefaultSize, 5)
        self.func1Btn.Bind(wx.EVT_BUTTON, self.f1OnClick, self.func1Btn)
        sizerFunc1.Add(self.func1Btn, 0, wx.ALL | wx.SHAPED, 5)
        # Add everything in sizerFunc1 into sizerPanelDef1
        sizerPanelDef1.Add(sizerFunc1, 1, wx.EXPAND, 5)
        # Set panelOne (first set of functions) sizer and layout -> then add to grid
        self.panelDef1.SetSizer(sizerPanelDef1)
        self.panelDef1.Layout()
        sizerPanelDef1.Fit(self.panelDef1)
        gSizerMain.Add(self.panelDef1, 1, wx.EXPAND | wx.ALL, 5)
        
        # Function 2
        self.panelDef2 = wx.Panel(self.panelMain, wx.ID_ANY,
          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        # Function 2 main box sizer
        sizerPanelDef2 = wx.BoxSizer(wx.VERTICAL)
        # Function 2 title
        # TODO function 2 title change
        self.function2Title = wx.StaticText(self.panelDef2, wx.ID_ANY, "function2",
          wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        # Function
        self.function2Title.SetBackgroundColour(
          wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        # Add function 2 Title to sizerFunction2
        sizerPanelDef2.Add(self.function2Title, 0, wx.ALL | wx.EXPAND, 5)
        # Create function 2 description and add background colour
        # TODO function 2 description (multiline)
        self.function2Desc = wx.StaticText(self.panelDef2, wx.ID_ANY, "This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.function2Desc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        # Add function 2 description into sizerFunc2
        sizerPanelDef2.Add(self.function2Desc, 0, wx.ALL | wx.EXPAND, 5)
        
        sizerFunc2 = wx.BoxSizer(wx.HORIZONTAL)
        # TODO change input names
        self.func2Input1 = wx.TextCtrl(self.panelDef2, wx.ID_ANY, 'TODOInput1', wx.DefaultPosition, wx.DefaultSize)
        sizerFunc2.Add(self.func2Input1, 0, wx.ALL, 5)
        self.func2Input2 = wx.TextCtrl(self.panelDef2, wx.ID_ANY, 'TODOInput2', wx.DefaultPosition, wx.DefaultSize)
        sizerFunc2.Add(self.func2Input2, 0, wx.ALL, 5)
        self.func2Input3 = wx.TextCtrl(self.panelDef2, wx.ID_ANY, 'TODOInput3', wx.DefaultPosition, wx.DefaultSize)
        sizerFunc2.Add(self.func2Input3, 0, wx.ALL, 5)
        
        self.func2Btn = wx.Button(
          self.panelDef2, wx.ID_ANY, "Generate", wx.DefaultPosition, wx.DefaultSize, 5)
        self.func2Btn.Bind(wx.EVT_BUTTON, self.f2OnClick, self.func2Btn)
        sizerFunc2.Add(self.func2Btn, 0, wx.ALL | wx.SHAPED, 5)
        
        sizerPanelDef2.Add(sizerFunc2, 1, wx.EXPAND, 5)
        
        self.panelDef2.SetSizer(sizerPanelDef2)
        self.panelDef2.Layout()
        sizerPanelDef2.Fit(self.panelDef2)
        gSizerMain.Add(self.panelDef2, 1, wx.EXPAND | wx.ALL, 5)
        
        # Function 3
        self.panelDef3 = wx.Panel(self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerPanelDef3 = wx.BoxSizer(wx.VERTICAL)
        
        self.alcoholTimeTitle = wx.StaticText(self.panelDef3, wx.ID_ANY, "Alcohol Time Analyser",
          wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        self.alcoholTimeTitle.SetBackgroundColour(
          wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        sizerPanelDef3.Add(self.alcoholTimeTitle, 0, wx.ALL | wx.EXPAND, 5)
        
        self.alcoholTimeDescription = wx.StaticText(self.panelDef3, wx.ID_ANY, "This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.alcoholTimeDescription.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        sizerPanelDef3.Add(self.alcoholTimeDescription, 0, wx.ALL | wx.EXPAND, 5)
        
        sizerFunc3 = wx.BoxSizer(wx.HORIZONTAL)
        
        
        func3Choices = [
          "Day of the week", "Light condition", "Alcohol related", "Severity"]
        self.func3Choice = wx.Choice(self.panelDef3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, func3Choices, 0)
        self.func3Choice.SetSelection(0)
        
        sizerFunc3.Add(self.func3Choice, 0, wx.ALL, 5)
        
        
        self.func3Btn = wx.Button(
          self.panelDef3, wx.ID_ANY, "Generate", wx.DefaultPosition, wx.DefaultSize, 5)
        self.func3Btn.Bind(wx.EVT_BUTTON, self.f3OnClick, self.func3Btn)
        sizerFunc3.Add(self.func3Btn, 0, wx.ALL | wx.SHAPED, 5)
        
        sizerPanelDef3.Add(sizerFunc3, 1, wx.EXPAND, 5)
        
        
        self.panelDef3.SetSizer(sizerPanelDef3)
        self.panelDef3.Layout()
        sizerPanelDef3.Fit(self.panelDef3)
        gSizerMain.Add(self.panelDef3, 1, wx.EXPAND | wx.ALL, 5)
        
        # Function 4
        self.panelDef4 = wx.Panel(self.panelMain, wx.ID_ANY,
          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        sizerPanelDef4 = wx.BoxSizer(wx.VERTICAL)
        
        
        self.func4Title = wx.StaticText(
          self.panelDef4, wx.ID_ANY, "Map Generator", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE)
        self.func4Title.SetBackgroundColour(
          wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        sizerPanelDef4.Add(self.func4Title, 0, wx.ALL | wx.EXPAND, 5)
        
        self.func4Desc = wx.StaticText(self.panelDef4, wx.ID_ANY, "This dataset will generate a map that presents the data based on the following selectable categories:\n\nSeverity: The severity of injuries sustained by perons involved in each incident.\n\nAlcohol related: If alcohol was a critical factor as a cause of the incident.\n\nHit and run: If the incident was classified as a hit and run.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE)
        self.func4Desc.SetBackgroundColour(
          wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
        
        sizerPanelDef4.Add(self.func4Desc, 0, wx.ALL | wx.EXPAND, 5)
        
        sizerFunc4 = wx.BoxSizer(wx.HORIZONTAL)
        
        
        func4Choices = [
          "Severity", "Alcohol related", "Hit and run"]
        self.func4Choice = wx.Choice(
          self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, func4Choices, 0)
        self.func4Choice.SetSelection(0)
        sizerFunc4.Add(self.func4Choice, 0, wx.ALL, 5)
        
        func4Choices1 = [
          "2013", "2014", "2015", "2016", "2017", "2018"]
        self.func4Choice1 = wx.Choice(
          self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, func4Choices1, 0)
        self.func4Choice1.SetSelection(0)
        sizerFunc4.Add(self.func4Choice1, 0, wx.ALL, 5)
        
        self.func4Btn = wx.Button(
          self.panelDef4, wx.ID_ANY, "Generate", wx.DefaultPosition, wx.DefaultSize, 5)
        self.func4Btn.Bind(wx.EVT_BUTTON, self.f4OnClick, self.func4Btn)
        sizerFunc4.Add(self.func4Btn, 0, wx.ALL | wx.SHAPED, 5)
        
        sizerPanelDef4.Add(sizerFunc4, 1, wx.EXPAND, 5)
        
        self.panelDef4.SetSizer(sizerPanelDef4)
        self.panelDef4.Layout()
        sizerPanelDef4.Fit(self.panelDef4)
        gSizerMain.Add(self.panelDef4, 1, wx.EXPAND | wx.ALL, 5)
        
        
        # Main panel set sizer & layout
        self.panelMain.SetSizer(gSizerMain)
        self.panelMain.Layout()
        gSizerMain.Fit(self.panelMain)
        MainFrameSizer.Add(self.panelMain, 1, wx.EXPAND, 0)
        FrameMainSizer.Add(MainFrameSizer, 1, wx.EXPAND, 0)
        
        self.SetSizer(FrameMainSizer)
        self.Layout()
        self.Center(wx.BOTH)
        # Show the App
        self.Show(True)

    
    def f1OnClick(self, event):
        # First text input value
        val = self.func1Input1.GetValue()
        # Second text input value
        val1 = self.func1Input2.GetValue()
        print(val, val1)
        sHD(sTP(val, val1))

    def f2OnClick(self, event):
        # First text input value
        val = self.func2Input1.GetValue()
        # Second text input value
        val1 = self.func2Input2.GetValue()
        # Third text input value
        val2 = self.func2Input3.GetValue()


    def f3OnClick(self, event):
        #This returns the index of the choice
        val = self.func3Choice.GetSelection()
        if (val == 0):
           ata(data, 'DAY_OF_WEEK')
        elif (val == 1):
           ata(data, 'LIGHT_CONDITION')
        elif (val == 2):
            ata(data, 'ALCOHOL_RELATED')
        elif (val == 3):
            ata(data, 'SEVERITY')
       
    def f4OnClick(self, event):
        # From category selector
        val = self.func4Choice.GetSelection()
        # From year selector
        val1= self.func4Choice1.GetSelection()
        if (val == 0):
            if (val1 == 0):
                mG(data, "SEVERITY", "2013")
            elif (val1 == 1):
                mG(data, "SEVERITY", "2014")
            elif (val1 == 2):
                mG(data, "SEVERITY", "2015")
            elif (val1 == 3):
                mG(data, "SEVERITY", "2016")
            elif (val1 == 4):
                mG(data, "SEVERITY", "2017")
            elif (val1 == 5):
                mG(data, "SEVERITY", "2018")
        elif (val == 1):
            if (val1 == 0):
                mG(data, "ALCOHOL_RELATED", "2013")
            elif (val1 == 1):
                mG(data, "ALCOHOL_RELATED", "2014")
            elif (val1 == 2):
                mG(data, "ALCOHOL_RELATED", "2015")
            elif (val1 == 3):
                mG(data, "ALCOHOL_RELATED", "2016")
            elif (val1 == 4):
                mG(data, "ALCOHOL_RELATED", "2017")
            elif (val1 == 5):
                mG(data, "ALCOHOL_RELATED", "2018")
        elif (val == 2):
            if (val1 == 0):
                mG(data, "HIT_RUN_FLAG", "2013")
            elif (val1 == 1):
                mG(data, "HIT_RUN_FLAG", "2014")
            elif (val1 == 2):
                mG(data, "HIT_RUN_FLAG", "2015")
            elif (val1 == 3):
                mG(data, "HIT_RUN_FLAG", "2016")
            elif (val1 == 4):
                mG(data, "HIT_RUN_FLAG", "2017")
            elif (val1 == 5):
                mG(data, "HIT_RUN_FLAG", "2018")
        
      

if __name__ == "__main__":
  app = wx.App()
  frame = myGui(None, -1, 'DAVCrash')
  app.MainLoop()
