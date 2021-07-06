import pyautogui
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
    
    pyautogui.hotkey("ctrl", 'z')
    #pyautogui.write("(declare +x | sed -r 's/^/export /' && declare -x) > /tmp/env.txt")
    pyautogui.write("(declare +x && declare -x) > /tmp/env.txt")
    pyautogui.press('enter')

    pyautogui.write("fg")
    pyautogui.press('enter')

    updateGUI()


def updateGUI():
    '''Force update of GTK mainloop during a long-running process'''
    while Gtk.events_pending():
        Gtk.main_iteration()

