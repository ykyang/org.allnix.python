# https://wiki.wxpython.org/Getting%20Started#Building_a_simple_text_editor
import wx
import os

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
        # List of standard event identifiers: https://docs.wxwidgets.org/2.8.12/wx_stdevtid.html
        menu_open = filemenu.Append(wx.ID_OPEN, '&Open', 'Open file')
        menuabout = filemenu.Append(wx.ID_ABORT, '&About', ' Information about this program')
        filemenu.AppendSeparator()
        menuexit = filemenu.Append(wx.ID_EXIT, 'E&xit', ' Terminate the program')
        
        ## Event handling
        # List of events: https://wiki.wxpython.org/ListOfEvents
        self.Bind(wx.EVT_MENU, self.OnOpen, menu_open)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuabout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuexit)


        menubar = wx.MenuBar()
        menubar.Append(filemenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Show(True)

    def OnAbout(self, event):
        #dlg = wx.MessageDialog(self, 'A small text editor', 'About Simple Editor', wx.OK)
        dlg = wx.MessageDialog(self, 'A small text editor', 'About Simple Editor')
        dlg.ShowModal()
        dlg.Destroy()

    def OnExit(self, event):
        self.Close(True)
    
    def OnOpen(self, event):
        self.dirname = ''
        dlg = wx.FileDialog(self, 'Choose a file', self.dirname, '', '*.*', wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            f = open(os.path.join(self.dirname, self.filename), 'r')
            self.control.SetValue(f.read())
            f.close()
        dlg.Destroy()
    


