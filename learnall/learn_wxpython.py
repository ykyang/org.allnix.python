import wx
import learnall.wx

app = wx.App(False)
frame = learnall.wx.MyFrame(None, 'Small editor')
app.MainLoop()

