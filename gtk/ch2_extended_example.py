"""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html#extended-example

@author: Yi-Kun Yang <ykyang@gmail.com>
"""

import gi as gi

gi.require_version('Gtk', '3.0')
import gi.repository.Gtk as Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Hello World')
        
        button = Gtk.Button(label='Click Here')
        self.button = button
        button.connect('clicked', self.button_clicked)
        self.add(button)
        
    def button_clicked(self, widget):
        print('Hello World')
        
        
win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
