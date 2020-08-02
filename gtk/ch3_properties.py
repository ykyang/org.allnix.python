"""

https://python-gtk-3-tutorial.readthedocs.io/en/latest/basics.html#properties

@author: Yi-Kun Yang <ykyang@gmail.com>
"""

import gi
gi.require_version('Gtk', '3.0')
import gi.repository.Gtk as Gtk

win = Gtk.Window(title='Properties')

label = Gtk.Label(label='Hello World!', angle=25, halign=Gtk.Align.END)

# Or this way
# label = Gtk.Label()
# label.set_label("Hello World")
# label.set_angle(25)
# label.set_halign(Gtk.Align.END)

# Or this way
# label.props.label = 'Hello World!'

# Show what is available in a widget
widget = Gtk.Box()
print(dir(widget.props))

win.add(label)
win.show_all()
Gtk.main()


