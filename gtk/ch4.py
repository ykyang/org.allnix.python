"""

https://python-gtk-3-tutorial.readthedocs.io/en/latest/unicode.html
"""
import gi
gi.require_version('Gtk', '3.0')
import gi.repository.Gtk as Gtk

# Demonstrate str into and str out of of Gtk are the same
label = Gtk.Label()
py_text = "Fu\u00dfb\u00e4lle"
label.set_text(py_text)
gtk_text = label.get_text()

print(type(gtk_text))
print(gtk_text == py_text)
