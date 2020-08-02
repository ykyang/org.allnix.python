"""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html#grid

@author: Yi-Kun Yang <ykyang@gmail.com>
"""


# Grid.attach()
# Grid.attach_next_to()

import gi
gi.require_version('Gtk', '3.0')
import gi.repository.Gtk as Gtk

class GridWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Grid Example')
        
        grid = Gtk.Grid()
        self.add(grid)
        
        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")
        
        grid.add(button1)
        grid.attach(button2, 1, 0, 2, 1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach(button5, 1, 2, 1, 1)
        grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)
        
win = GridWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
