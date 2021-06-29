import os
import time
from gi.repository import Gtk


def exportEnv():
    #os.system("espeak dupa")
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

    wait_2s()
    #exit()


def updateGUI():
    '''Force update of GTK mainloop during a long-running process'''
    while Gtk.events_pending():
        Gtk.main_iteration()

def wait_2s():
    # for i in range(2):
    #     time.sleep(0.2)
    updateGUI()
