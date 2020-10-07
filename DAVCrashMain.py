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
    sizerFunc2 = wx.BoxSizer(wx.VERTICAL)
    # Function 2 title
    self.function2Title = wx.TextCtrl(self.panelDef2, wx.ID_ANY, "function2",
      wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
    # Function 
    self.function2Title.SetBackgroundColour(
      wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))













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


if __name__ == "__main__":
  app = wx.App()
  frame = myGui(None, -1, 'My App')
  app.MainLoop()
