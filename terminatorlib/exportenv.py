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

    #xdotool click 1;
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


def exportEnvOLD():
    if not getCloningMode():
        return

    os.system("xdotool click 1") 

    os.system("xdotool key Control_L+z") 
    #os.system("%s xdotool key KP_Enter" % getXdotoolString("bg"))
    #exportCmd = "env | sed -r 's/^/export /' > /tmp/env.txt"
    exportCmd1 = "set | sed -r "
    os.system("xdotool type '%s'" % exportCmd1)
    os.system("xdotool keydown apostrophe")
    os.system("xdotool keyup apostrophe")

    os.system("xdotool type '%s'" % "s/^/export /")

    os.system("xdotool keydown apostrophe")
    os.system("xdotool keyup apostrophe")
    
    exportCmd2 = " > /tmp/env.txt"
    os.system("xdotool type '%s'" % exportCmd2)
    #exportCmd = "env  > /tmp/env.txt"
    #exportCmd = r'''env | awk '$0="export "$0' > /tmp/env.txt '''
   # os.system("xdotool type '%s'" % exportCmd)

    #xdotool keydown apostrophe    
    os.system("xdotool key KP_Enter")
    os.system("xdotool type '%s'" % "fg")
    os.system("xdotool key KP_Enter")
    #os.system("sed -i -e 's/^/export /' /tmp/env.txt")
    #exit()

    setCloningMode(False)

    updateGUI()


def updateGUI():
    '''Force update of GTK mainloop during a long-running process'''
    while Gtk.events_pending():
        Gtk.main_iteration()

def wait_2s():
    # for i in range(2):
    #     time.sleep(0.2)
    updateGUI()
