import os
import keyboard
import threading
import time
import win32api
import win32gui

IS_RUN = True
WM_APPCOMMAND = 0x319
APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
IS_MUTED = False

def init():
    try:
      os.system("pip install keyboard")
      os.system("pip install pywin32")
    except:
      print('An exception occurred')


def handleMute(e):
    global IS_RUN,IS_MUTED
    if keyboard.is_pressed('ctrl'):
            hwnd_active = win32gui.GetForegroundWindow()
            win32api.SendMessage(hwnd_active, WM_APPCOMMAND, None, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
            if IS_MUTED is True:
                print("Mic Enable")
                IS_MUTED = False
            elif IS_MUTED != True:
                print("Mic Disable")
                IS_MUTED = True

def keyBind():
    global IS_RUN,IS_MUTED
    keyboard.on_release_key("b", handleMute)
    while IS_RUN:
        if keyboard.is_pressed('ctrl+q'):
            IS_RUN = False
            # pas

def clear_screen(delay):
    while IS_RUN:
        time.sleep(delay)
        os.system("cls")

def main():
    os.system("cls")
    
    #bind
    print("Bind is running!")
    keyBind()    
    pass    


if __name__ == '__main__':
    init()
    main()
    