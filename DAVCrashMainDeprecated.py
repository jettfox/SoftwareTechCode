try:
  import wx
except ImportError:
  raise ImportError("The Python wx module is required to run this program")

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

    # First set of functions
    self.panelDef1 = wx.Panel(
        self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
    sizerPanelDef1 = wx.BoxSizer(wx.VERTICAL)
    # Add title via text control & set a background colour
    self.function1Title = wx.TextCtrl(
        self.panelDef1, wx.ID_ANY, "function1", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
    self.function1Title.SetBackgroundColour(
        wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
    # Expand title to full grid width
    sizerPanelDef1.Add(self.function1Title, 0, wx.ALL | wx.EXPAND, 5)
    # Add description of what this function will do
    self.function1Desc = wx.TextCtrl(self.panelDef1, wx.ID_ANY, "This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
    self.function1Desc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
    # Add function1 description to panelDef1
    sizerPanelDef1.Add(self.function1Desc, 0, wx.ALL | wx.EXPAND, 5)
    # Add horizontal sizer to bottom of function1 panel
    sizerFunc1 = wx.BoxSizer(wx.HORIZONTAL)
    # Add function selector
    function1SelectorChoices = ['Day of the week', 'Light condition', 'Alcohol related', 'Severity']
    self.function1Selector = wx.Choice(self.panelDef1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, function1SelectorChoices, 0)
    self.function1Selector.SetSelection(0)
    sizerFunc1.Add(self.function1Selector, 0, wx.ALL, 5)
    # Add selection button to execute the function
    self.function1Button = wx.Button(self.panelDef1, wx.ID_ANY, 'Generate', wx.DefaultPosition, wx.DefaultSize, 0)
    sizerFunc1.Add(self.function1Button, 0, wx.ALL | wx.SHAPED, 5)
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
    self.function2Title = wx.TextCtrl(self.panelDef2, wx.ID_ANY, "function2",
      wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
    # Function
    self.function2Title.SetBackgroundColour(
      wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
    # Add function 2 Title to sizerFunction2
    sizerPanelDef2.Add(self.function2Title, 0, wx.ALL | wx.EXPAND, 5)
    # Create function 2 description and add background colour
    self.function2Desc = wx.TextCtrl(self.panelDef2, wx.ID_ANY, "This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
    self.function2Desc.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))
    # Add function 2 description into sizerFunc2
    sizerPanelDef2.Add(self.function2Desc, 0, wx.ALL | wx.EXPAND, 5)

    sizerFunc2 = wx.BoxSizer(wx.HORIZONTAL)

    function2SelectorChoices = ["Day of the week",
      "Light condition", "Alcohol related", "Severity"]
    self.function2Selector = wx.Choice(
      self.panelDef2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, function2SelectorChoices, 0)
    self.function2Selector.SetSelection(0)
    sizerFunc2.Add(self.function2Selector, 0, wx.ALL, 5)

    self.function2Button = wx.Button(
      self.panelDef2, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
    sizerFunc2.Add(self.function2Button, 0, wx.ALL | wx.SHAPED, 5)

    sizerPanelDef2.Add(sizerFunc2, 1, wx.EXPAND, 5)

    self.panelDef2.SetSizer(sizerPanelDef2)
    self.panelDef2.Layout()
    sizerPanelDef2.Fit(self.panelDef2)
    gSizerMain.Add(self.panelDef2, 1, wx.EXPAND | wx.ALL, 5)

    self.panelDef3 = wx.Panel(self.panelMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
    sizerPanelDef3 = wx.BoxSizer(wx.VERTICAL)

    self.alcoholTimeTitle = wx.TextCtrl(self.panelDef3, wx.ID_ANY, "Alcohol Time Analyser",
      wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
    self.alcoholTimeTitle.SetBackgroundColour(
      wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

    sizerPanelDef3.Add(self.alcoholTimeTitle, 0, wx.ALL | wx.EXPAND, 5)

    self.alcoholTimeDescription = wx.TextCtrl(self.panelDef3, wx.ID_ANY, u"This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
    self.alcoholTimeDescription.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

    sizerPanelDef3.Add(self.alcoholTimeDescription, 0, wx.ALL | wx.EXPAND, 5)

    sizerFunc3 = wx.BoxSizer(wx.HORIZONTAL)


    alcoholTimeSelectorChoices = [
      u"Day of the week", u"Light condition", u"Alcohol related", u"Severity"]
    self.alcoholTimeSelector = wx.Choice(self.panelDef3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, alcoholTimeSelectorChoices, 0)
    self.alcoholTimeSelector.SetSelection(0)

    sizerFunc3.Add(self.alcoholTimeSelector, 0, wx.ALL, 5)


    self.alcoholTimeGraphButton = wx.Button(
      self.panelDef3, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
    sizerFunc3.Add(self.alcoholTimeGraphButton, 0, wx.ALL | wx.SHAPED, 5)

    sizerPanelDef3.Add(sizerFunc3, 1, wx.EXPAND, 5)


    self.panelDef3.SetSizer(sizerPanelDef3)
    self.panelDef3.Layout()
    sizerPanelDef3.Fit(self.panelDef3)
    gSizerMain.Add(self.panelDef3, 1, wx.EXPAND | wx.ALL, 5)

    # Function 4
    self.panelDef4 = wx.Panel(self.panelMain, wx.ID_ANY,
      wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
    sizerPanelDef4 = wx.BoxSizer(wx.VERTICAL)


    self.mapGeneratorTitle = wx.TextCtrl(
      self.panelDef4, wx.ID_ANY, u"Map Generator", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
    self.mapGeneratorTitle.SetBackgroundColour(
      wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

    sizerPanelDef4.Add(self.mapGeneratorTitle, 0, wx.ALL | wx.EXPAND, 5)

    self.mapGeneratorDescription = wx.TextCtrl(self.panelDef4, wx.ID_ANY, "This dataset will generate a map that presents the data based on the following selectable categories:\n\nSeverity: The severity of injuries sustained by perons involved in each incident.\n\nAlcohol related: If alcohol was a critical factor as a cause of the incident.\n\nHit and run: If the incident was classified as a hit and run.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
    self.mapGeneratorDescription.SetBackgroundColour(
      wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

    sizerPanelDef4.Add(self.mapGeneratorDescription, 0, wx.ALL | wx.EXPAND, 5)

    sizerFunc4 = wx.BoxSizer(wx.HORIZONTAL)


    mapGeenratorCategorySelectorChoices = [
      "Severity", "Alcohol related", "Hit and run"]
    self.mapGeenratorCategorySelector = wx.Choice(
      self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mapGeenratorCategorySelectorChoices, 0)
    self.mapGeenratorCategorySelector.SetSelection(0)
    sizerFunc4.Add(self.mapGeenratorCategorySelector, 0, wx.ALL, 5)

    mapGeneratorYearSelectorChoices = [
      "Day of the week", "Light condition", "Alcohol related", "Severity"]
    self.mapGeneratorYearSelector = wx.Choice(
      self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mapGeneratorYearSelectorChoices, 0)
    self.mapGeneratorYearSelector.SetSelection(0)
    sizerFunc4.Add(self.mapGeneratorYearSelector, 0, wx.ALL, 5)

    self.mapGeneratorButton = wx.Button(
      self.panelDef4, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
    sizerFunc4.Add(self.mapGeneratorButton, 0, wx.ALL | wx.SHAPED, 5)

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


    # # Connect Events
    # self.Bind(wx.EVT_MENU, self.menuItemFileNewOnMenuSelection,
    #   id=self.menuItemFileAbout.GetId())
    # self.Bind(wx.EVT_MENU, self.menuItemFileOpenOnMenuSelection,
    #   id=self.menuItemFileHelp.GetId())
    # self.Bind(wx.EVT_MENU, self.menuItemFileExitOnMenuSelection,
    #   id=self.menuItemFileExit.GetId())

if __name__ == "__main__":
  app = wx.App()
  frame = myGui(None, -1, 'My App')
  app.MainLoop()
