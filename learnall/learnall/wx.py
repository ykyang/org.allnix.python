# https://wiki.wxpython.org/Getting%20Started#Building_a_simple_text_editor
import wx

class MyFrame(wx.Frame):
    """ We simply derive a new class of Frame. """
    def __init__(self, parent, title):
        ## First steps
        wx.Frame.__init__(self, parent, title=title, size=(600,400))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        
        ## Adding a menu bar
        self.CreateStatusBar()

        # Setting up the menu
        filemenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets
        filemenu.Append(wx.ID_ABORT, '&About', 'Information about this program')

        menubar = wx.MenuBar()
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Show(True)