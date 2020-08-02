"""
https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html#boxes

@author: Yi-Kun Yang <ykyang@gmail.com>
"""



import gi
gi.require_version('Gtk', '3.0')
import gi.repository.Gtk as Gtk


class MyWindow(Gtk.Window):
    def __init__(me):
        
        Gtk.Window.__init__(me, title='Hello World')

        box = me.box = Gtk.HBox(spacing=6)
        me.add(box)

        # Gtk.Box.pack_start() # Pack from left
        # Gtk.Box.pack_end() # Pack from right

        button1 = me.button1 = Gtk.Button(label='Hello')
        button1.connect('clicked', me.button1_clicked)
        box.pack_start(button1, True, True, 0)

        button2 = me.button2 = Gtk.Button(label='Goodbye')
        button2.connect('clicked', me.button2_clicked)
        box.pack_start(button2, True, True, 0)
           
        

    def button1_clicked(me, widget):
        print('Hello')

    def button2_clicked(me, widget):
        print('Goodbye')

win = MyWindow()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()

