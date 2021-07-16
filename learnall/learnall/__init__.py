import os

def hello():
    import wx
    app = wx.App(False)
    print(app)
    x = 'Hello World from learnall/{}'.format(os.path.basename(__file__))
    return x
