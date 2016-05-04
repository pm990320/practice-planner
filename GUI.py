import wx

from Scales import *

class Frame(wx.Frame):
    scales = Scales()

    def OnExit(self, event):
        self.Destroy()

    def Populate(self, panel):
        posy = 20
        wx.StaticText(panel, label='Scales: ', pos=(20, 20), style=wx.TE_LEFT)

        i = 0
        while i != 5: 
            posy += 20
            wx.StaticText(panel, label=str(self.scales.getScale()), pos=(30, posy), style=wx.TE_LEFT)
            i += 1

        posy += 40
        wx.StaticText(panel, label='Arpeggios:', pos=(20, posy), style=wx.LEFT)

        i = 0
        while i != 5:
            posy += 20
            wx.StaticText(panel, label=self.scales.getArpeggio(), pos=(30, posy), style=wx.TE_LEFT)
            i += 1

        posy += 40
        wx.StaticText(panel, label='Contrary Motions:', pos=(20, posy), style=wx.LEFT)

        i = 0
        while i != 2:
            posy += 20
            wx.StaticText(panel, label=self.scales.getContraryMotion(), pos=(30, posy), style=wx.TE_LEFT)
            i += 1

        posy += 40
        wx.StaticText(panel, label='Chromatics:', pos=(20, posy), style=wx.LEFT)

        i = 0
        while i != 2:
            posy += 20
            wx.StaticText(panel, label=self.scales.getChromatic(), pos=(30, posy), style=wx.TE_LEFT)
            i += 1

        posy += 40
        wx.StaticText(panel, label='Other Technical Exercises:', pos=(20, posy), style=wx.LEFT)

        i = 0
        while i != 2:
            posy += 20
            wx.StaticText(panel, label=self.scales.getTechnicalExercise(), pos=(30, posy), style=wx.TE_LEFT)
            i += 1

    def __init__(self, parent, title):
        self.frame = wx.Frame.__init__(self, parent, title=title, size=(500, 600), pos=(40, 40))
        self.EnableCloseButton(True)

        panel = wx.Panel(self)
        
        self.Populate(panel)

        self.Show(True)

app = wx.App()
frame = Frame(None, "Practice Planner")
app.MainLoop()