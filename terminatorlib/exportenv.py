import os
import time
from gi.repository import Gtk

cloningMode = False

def setCloningMode(value):
    global cloningMode
    cloningMode = value

def getCloningMode():
    return cloningMode

def exportEnv():
    if not getCloningMode():
        return

    cmd = '''
    xdotool key Control_L+z
    xdotool type 'set | sed -r ';
    xdotool keydown apostrophe;
    xdotool keyup apostrophe;
    xdotool type 's/^/export /';
    xdotool keydown apostrophe;
    xdotool keyup apostrophe;
    xdotool type ' > /tmp/env.txt';
    xdotool key KP_Enter;
    xdotool type 'fg';
    xdotool key KP_Enter;
    '''
    os.system(cmd)
    
    setCloningMode(False)

    updateGUI()

def updateGUI():
    '''Force update of GTK mainloop during a long-running process'''
    while Gtk.events_pending():
        Gtk.main_iteration()

