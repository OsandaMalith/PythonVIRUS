import win32gui
import win32con
import os

#Coded By B3mB4m
#http://sysfail.shost.ca/papers/basic_anti_debug/

"""
The first trick consists of finding the main window of olly 1 by using it's name.
For this, once again, the WinApi offers us a function called FindWindow().
Giving it a string identifying the parent window name, the function returns a 
window handle (HWND) on this window if it succeeds. Note that the string doesn't have 
to be case sensitive.
"""

def immunityANDollydbg():
	#I did try on Immunity Debugger and worked(2015)
	name = "Immunity Debugger - %s - [CPU - main thread, module %s]" % (os.path.basename(__file__),os.path.basename(__file__).split("exe")[0])
	name2 = "OllyDbg - %s - [CPU - main thread, module %s]" % (os.path.basename(__file__),os.path.basename(__file__).split("exe")[0])
	for x in [name,name2]:
		handle = win32gui.FindWindow(None, x)
		win32gui.PostMessage(handle,win32con.WM_CLOSE,0,0)
		if handle != 0:
			return True
	return False

