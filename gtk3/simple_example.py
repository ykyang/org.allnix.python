#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:47:31 2020

@author: ykyang
"""

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

win = Gtk.Window(title='Hello World')
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()
