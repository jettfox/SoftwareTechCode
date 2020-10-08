import wx
import matplotlib
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class RightPanel(wx.Panel):
    def __init__(self, parent):
      wx.Panel.__init__(self, parent = parent)
      self.figure = Figure()
      self.axes = self.figure.add_subplot(111)
      self.canvas = FigureCanvas(self, -1, self.figure)
      self.sizer = wx.BoxSizer(wx.VERTICAL)
      #Add canvas to sizer
      self.sizer.Add(self.canvas, 1, wx.EXPAND)
      self.SetSizer(self.sizer)
      #Typical labels for graph (probably not needed)
      self.axes.set_xlabel("Time")
      self.axes.set_ylabel("A/D Counts")
  
    def draw(self):
        x = np.arange(0, 3, 0.01)
        y = np.sin(np.pi*x)
        self.axes.plot(x, y)
        
    def changeAxes(self, min, max):
        self.axes.set_ylim(float(min), float(max))
        self.canvas.draw()
        


class LeftPanel(wx.Panel):
    def __init__(self, parent, right):
      wx.Panel.__init__(self, parent = parent)
      
      #Because the left panel is called after the right panel (L103-104), you can refrerence
      #the panel that comes first, this allows you pass data between panels (LeftPanel / RightPanel)
      self.graph = right
      
      #Start button
      self.togglebuttonStart = wx.ToggleButton(self, id = -1, label = "Start", pos=(10, 10))
      self.togglebuttonStart.Bind(wx.EVT_TOGGLEBUTTON, self.OnStartClick)
      #Label for checkbox
      labelChannels = wx.StaticText(self, -1, "Analogue Inputs", pos=(10,60))
      #Checkbox options
      self.cb1 = wx.CheckBox(self, -1, "A0", pos=(120, 60))
      self.cb2 = wx.CheckBox(self, -1, "A1", pos=(120, 75))
      self.cb3 = wx.CheckBox(self, -1, "A2", pos=(120, 90))
      self.cb4 = wx.CheckBox(self, -1, "A3", pos=(120, 105))
      #Bind the checkbox to an event (OnChecked function)
      self.Bind(wx.EVT_CHECKBOX, self.OnChecked)
      
      #Single text input
      self.textboxSampleTime = wx.TextCtrl(self, -1, "1000", pos=(50, 150), size=(50,-1))
      #Button for sending text input
      self.buttonSend = wx.Button(self, -1, "Send", pos=(105, 150), size=(50,-1))
      #Bind the button for text input to even (OnSend)
      self.buttonSend.Bind(wx.EVT_BUTTON, self.OnSend)
      
      #MinY text input
      lablMinY = wx.StaticText(self, -1, "Min Y", pos=(60, 200))
      self.textboxMinYAxis = wx.TextCtrl(self, -1, "0", pos=(60, 220))
      #MaxY text input
      lablMaxY = wx.StaticText(self, -1, "Max Y", pos=(60, 250))
      self.textboxMaxYAxis = wx.TextCtrl(self, -1, "1024", pos=(60, 270))
      #Make button and set event (SetButtonRange)
      self.buttonRange = wx.Button(self, -1, "Set Y Axis", pos=(60, 300))
      self.buttonRange.Bind(wx.EVT_BUTTON, self.SetButtonRange)
      
    def SetButtonRange(self, event):
        #Fetches the value from textboxMinYAxis / textboxMaxYAxis then passes these values following
        #this method:
        #self.graph (L34) -> changeAxes (L24)
        min = self.textboxMinYAxis.GetValue()
        max = self.textboxMaxYAxis.GetValue()
        self.graph.changeAxes(min, max)
      
      
    def OnSend(self, event):
        #Sends value on button event to console
        val = self.textboxSampleTime.GetValue()
        print(val)
      
      
    def OnChecked(self, event):
        #Sends value on button event to console
        cb = event.GetEventObject()
        print("%s is clicked" % (cb.GetLabel()))
      
    def OnStartClick(self, event):
        #Is the toggle button, allows the button to be swapped from 'Start' to 'Stop'
        val = self.togglebuttonStart.GetValue()
        if (val == True):
            self.togglebuttonStart.SetLabel("Stop")
        else:
            self.togglebuttonStart.SetLabel("Start")
      





class Main(wx.Frame):
    def __init__(self):
      wx.Frame.__init__(self, parent=None, title="DAVCrash", size=(1000, 800))
      #Split window in 'half'
      splitter = wx.SplitterWindow(self)
      #Call right first so that it can be initialised in left panel (talking between panels)
      right = RightPanel(splitter)
      left = LeftPanel(splitter, right)
      #Align splitter vertically, call panels in order of how they should appear L -> R
      splitter.SplitVertically(left, right)
      #Sets minimum panel size so that on init the panel isn't a single pixel wide
      splitter.SetMinimumPaneSize(300)
      right.draw()


if __name__ == "__main__":
  app = wx.App()
  frame = Main()
  frame.Show()
  app.MainLoop()