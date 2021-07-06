import os
import time
import pyautogui
from gi.repository import Gtk
from .util import dbg

cloningMode = False

def setCloningMode(value):
    global cloningMode
    cloningMode = value

def getCloningMode():
    return cloningMode

def exportEnvOLD():
    if not getCloningMode():
        return

    cmd = '''
    xdotool key Control_L+z;
    xdotool type '{declare +x ; declare -x;} | sed -r ';
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

    updateGUI()

def exportEnv():
    if not getCloningMode():
        return

    cmd = '''
    xdotool key Control_L+z;
    xdotool type '{declare +x ; declare -x;} | sed -r ';
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
    
    pyautogui.hotkey("command", 'z')

    pyautogui.write("(declare +x | sed -r 's/^/export /' && declare -x) > /tmp/env.txt")
    pyautogui.press('enter')

    pyautogui.write("fg")
    pyautogui.press('enter')

    updateGUI()

def updateGUI():
    '''Force update of GTK mainloop during a long-running process'''
    while Gtk.events_pending():
        Gtk.main_iteration()

