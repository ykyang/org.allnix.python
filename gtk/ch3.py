"""


@author: Yi-Kun Yang <ykyang@gmail.com>
"""
# Connect signal
handler_id = widget.connect('event name', callback, data)

# Disconnect signal
widget.disconnect(handler_id)
widget.disconnect_by_func(callback)

# Terminate the application
# Calling Gtk.main_quit() makes the main loop inside of Gtk.main() return.
window.connect('destroy', Gtk.main_quit)
