# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class frameMain
###########################################################################


class frameMain (wx.Frame):

	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"DAVCrash", pos=wx.DefaultPosition,
		                  size=wx.Size(1000, 800), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

		self.menuBarMain = wx.MenuBar(0)
		self.menuFile = wx.Menu()
		self.menuItemFileAbout = wx.MenuItem(
			self.menuFile, wx.ID_ANY, u"About", u"Details about this program.", wx.ITEM_NORMAL)
		self.menuFile.AppendItem(self.menuItemFileAbout)

		self.menuItemFileHelp = wx.MenuItem(
			self.menuFile, wx.ID_ANY, u"Help", u"Access documentation for this program", wx.ITEM_NORMAL)
		self.menuFile.AppendItem(self.menuItemFileHelp)

		self.menuFile.AppendSeparator()

		self.menuItemFileExit = wx.MenuItem(
			self.menuFile, wx.ID_ANY, u"Exit", u"Exit DAVCrash", wx.ITEM_NORMAL)
		self.menuFile.AppendItem(self.menuItemFileExit)

		self.menuBarMain.Append(self.menuFile, u"File")

		self.SetMenuBar(self.menuBarMain)

		self.m_statusBar = self.CreateStatusBar(1, wx.ST_SIZEGRIP, wx.ID_ANY)
		FrameMainSizer = wx.BoxSizer(wx.VERTICAL)

		MainFrameSizer = wx.BoxSizer(wx.VERTICAL)

		self.panelMain = wx.Panel(
			self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		self.panelMain.SetBackgroundColour(wx.Colour(47, 56, 61))

		gSizerMain = wx.GridSizer(2, 2, 0, 0)

		self.panelDef1 = wx.Panel(self.panelMain, wx.ID_ANY,
		                          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		sizerPanelDef1 = wx.BoxSizer(wx.VERTICAL)

		self.function1Title = wx.TextCtrl(self.panelDef1, wx.ID_ANY, u"function1",
		                                  wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
		self.function1Title.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerPanelDef1.Add(self.function1Title, 0, wx.ALL | wx.EXPAND, 5)

		self.function1Desc = wx.TextCtrl(self.panelDef1, wx.ID_ANY, u"This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
		self.function1Desc.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerPanelDef1.Add(self.function1Desc, 0, wx.ALL | wx.EXPAND, 5)

		sizerFunc1 = wx.BoxSizer(wx.HORIZONTAL)

		function1SelectorChoices = [u"Day of the week",
                              u"Light condition", u"Alcohol related", u"Severity"]
		self.function1Selector = wx.Choice(
			self.panelDef1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, function1SelectorChoices, 0)
		self.function1Selector.SetSelection(0)
		sizerFunc1.Add(self.function1Selector, 0, wx.ALL, 5)

		self.function1Button = wx.Button(
			self.panelDef1, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
		sizerFunc1.Add(self.function1Button, 0, wx.ALL | wx.SHAPED, 5)

		sizerPanelDef1.Add(sizerFunc1, 1, wx.EXPAND, 5)

		self.panelDef1.SetSizer(sizerPanelDef1)
		self.panelDef1.Layout()
		sizerPanelDef1.Fit(self.panelDef1)
		gSizerMain.Add(self.panelDef1, 1, wx.EXPAND | wx.ALL, 5)

		self.panelDef2 = wx.Panel(self.panelMain, wx.ID_ANY,
		                          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		sizerFunc2 = wx.BoxSizer(wx.VERTICAL)

		self.function2Title = wx.TextCtrl(self.panelDef2, wx.ID_ANY, u"function2",
		                                  wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
		self.function2Title.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc2.Add(self.function2Title, 0, wx.ALL | wx.EXPAND, 5)

		self.function2Desc = wx.TextCtrl(self.panelDef2, wx.ID_ANY, u"This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
		self.function2Desc.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc2.Add(self.function2Desc, 0, wx.ALL | wx.EXPAND, 5)

		bSizer593 = wx.BoxSizer(wx.HORIZONTAL)

		function2SelectorChoices = [u"Day of the week",
                              u"Light condition", u"Alcohol related", u"Severity"]
		self.function2Selector = wx.Choice(
			self.panelDef2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, function2SelectorChoices, 0)
		self.function2Selector.SetSelection(0)
		bSizer593.Add(self.function2Selector, 0, wx.ALL, 5)

		self.function2Button = wx.Button(
			self.panelDef2, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer593.Add(self.function2Button, 0, wx.ALL | wx.SHAPED, 5)

		sizerFunc2.Add(bSizer593, 1, wx.EXPAND, 5)

		self.panelDef2.SetSizer(sizerFunc2)
		self.panelDef2.Layout()
		sizerFunc2.Fit(self.panelDef2)
		gSizerMain.Add(self.panelDef2, 1, wx.EXPAND | wx.ALL, 5)

		self.panelDef3 = wx.Panel(self.panelMain, wx.ID_ANY,
		                          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		sizerFunc3 = wx.BoxSizer(wx.VERTICAL)

		self.alcoholTimeTitle = wx.TextCtrl(self.panelDef3, wx.ID_ANY, u"Alcohol Time Analyser",
		                                    wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
		self.alcoholTimeTitle.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc3.Add(self.alcoholTimeTitle, 0, wx.ALL | wx.EXPAND, 5)

		self.alcoholTimeDescription = wx.TextCtrl(self.panelDef3, wx.ID_ANY, u"This dataset will generate a graph based upon whether a crash occured in a high alcohol time period.\n\nDay of the week: Number of crashes by day of the week.\n\nLight condition: Number of crashes related to light conditions.\n\nAlcohol related: Number of crashes where alcohol was related.\n\nSeverity: Crashes categories by the severity of the incident.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
		self.alcoholTimeDescription.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc3.Add(self.alcoholTimeDescription, 0, wx.ALL | wx.EXPAND, 5)

		bSizer59 = wx.BoxSizer(wx.HORIZONTAL)

		alcoholTimeSelectorChoices = [
			u"Day of the week", u"Light condition", u"Alcohol related", u"Severity"]
		self.alcoholTimeSelector = wx.Choice(
			self.panelDef3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, alcoholTimeSelectorChoices, 0)
		self.alcoholTimeSelector.SetSelection(0)
		bSizer59.Add(self.alcoholTimeSelector, 0, wx.ALL, 5)

		self.alcoholTimeGraphButton = wx.Button(
			self.panelDef3, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer59.Add(self.alcoholTimeGraphButton, 0, wx.ALL | wx.SHAPED, 5)

		sizerFunc3.Add(bSizer59, 1, wx.EXPAND, 5)

		self.panelDef3.SetSizer(sizerFunc3)
		self.panelDef3.Layout()
		sizerFunc3.Fit(self.panelDef3)
		gSizerMain.Add(self.panelDef3, 1, wx.EXPAND | wx.ALL, 5)

		self.panelDef4 = wx.Panel(self.panelMain, wx.ID_ANY,
		                          wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
		sizerFunc4 = wx.BoxSizer(wx.VERTICAL)

		self.mapGeneratorTitle = wx.TextCtrl(
			self.panelDef4, wx.ID_ANY, u"Map Generator", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTRE | wx.TE_READONLY)
		self.mapGeneratorTitle.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc4.Add(self.mapGeneratorTitle, 0, wx.ALL | wx.EXPAND, 5)

		self.mapGeneratorDescription = wx.TextCtrl(self.panelDef4, wx.ID_ANY, u"This dataset will generate a map that presents the data based on the following selectable categories:\n\nSeverity: The severity of injuries sustained by perons involved in each incident.\n\nAlcohol related: If alcohol was a critical factor as a cause of the incident.\n\nHit and run: If the incident was classified as a hit and run.", wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE | wx.TE_READONLY)
		self.mapGeneratorDescription.SetBackgroundColour(
			wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

		sizerFunc4.Add(self.mapGeneratorDescription, 0, wx.ALL | wx.EXPAND, 5)

		bSizer591 = wx.BoxSizer(wx.HORIZONTAL)

		mapGeenratorCategorySelectorChoices = [
			u"Severity", u"Alcohol related", u"Hit and run"]
		self.mapGeenratorCategorySelector = wx.Choice(
			self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mapGeenratorCategorySelectorChoices, 0)
		self.mapGeenratorCategorySelector.SetSelection(0)
		bSizer591.Add(self.mapGeenratorCategorySelector, 0, wx.ALL, 5)

		mapGeneratorYearSelectorChoices = [
			u"Day of the week", u"Light condition", u"Alcohol related", u"Severity"]
		self.mapGeneratorYearSelector = wx.Choice(
			self.panelDef4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, mapGeneratorYearSelectorChoices, 0)
		self.mapGeneratorYearSelector.SetSelection(0)
		bSizer591.Add(self.mapGeneratorYearSelector, 0, wx.ALL, 5)

		self.mapGeneratorButton = wx.Button(
			self.panelDef4, wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer591.Add(self.mapGeneratorButton, 0, wx.ALL | wx.SHAPED, 5)

		sizerFunc4.Add(bSizer591, 1, wx.EXPAND, 5)

		self.panelDef4.SetSizer(sizerFunc4)
		self.panelDef4.Layout()
		sizerFunc4.Fit(self.panelDef4)
		gSizerMain.Add(self.panelDef4, 1, wx.EXPAND | wx.ALL, 5)

		self.panelMain.SetSizer(gSizerMain)
		self.panelMain.Layout()
		gSizerMain.Fit(self.panelMain)
		MainFrameSizer.Add(self.panelMain, 1, wx.EXPAND, 0)

		FrameMainSizer.Add(MainFrameSizer, 1, wx.EXPAND, 0)

		self.SetSizer(FrameMainSizer)
		self.Layout()

		self.Centre(wx.BOTH)

		# Connect Events
		self.Bind(wx.EVT_MENU, self.menuItemFileNewOnMenuSelection,
		          id=self.menuItemFileAbout.GetId())
		self.Bind(wx.EVT_MENU, self.menuItemFileOpenOnMenuSelection,
		          id=self.menuItemFileHelp.GetId())
		self.Bind(wx.EVT_MENU, self.menuItemFileExitOnMenuSelection,
		          id=self.menuItemFileExit.GetId())
		self.function1Button.Bind(
			wx.EVT_BUTTON, self.alcoholTimeGraphButtonOnButtonClick)
		self.function2Button.Bind(
			wx.EVT_BUTTON, self.alcoholTimeGraphButtonOnButtonClick)
		self.alcoholTimeGraphButton.Bind(
			wx.EVT_BUTTON, self.alcoholTimeGraphButtonOnButtonClick)
		self.mapGeneratorButton.Bind(
			wx.EVT_BUTTON, self.mapGeneratorButtonOnButtonClick)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def menuItemFileNewOnMenuSelection(self, event):
		event.Skip()

	def menuItemFileOpenOnMenuSelection(self, event):
		event.Skip()

	def menuItemFileExitOnMenuSelection(self, event):
		event.Skip()

	def alcoholTimeGraphButtonOnButtonClick(self, event):
		event.Skip()

	def mapGeneratorButtonOnButtonClick(self, event):
		event.Skip()
