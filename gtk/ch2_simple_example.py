"""

https://python-gtk-3-tutorial.readthedocs.io/en/latest/introduction.html

@author: Yi-Kun Yang <ykyang@gmail.com>
"""

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# The next line creates an empty window.
win = Gtk.Window(title='Hello World')
# Followed by connecting to the window’s delete event to ensure that the
# application is terminated if we click on the x to close the window.
win.connect('destroy', Gtk.main_quit)
# In the next step we display the window.
win.show_all()
# Finally, we start the GTK+ processing loop which we quit when the window is closed (see line 6).
Gtk.main()
