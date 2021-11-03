from tkinter import*
from pyautogui import*
import subprocess
import keyboard
import mouse
import time
import pyautogui
import random
import win32api, win32con


root = Tk()

##Label
Label_1 = Label(root, text="Python GUI", padx=20,pady=20, font=("arial", 30, "bold") )
Label_1.grid(row=0, column=1, )


## Click Function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.15) #This pauses the script for 0.15 seconds
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)






## Functions
def Script1():

    time.sleep(5)    
    
    time.sleep(0.1)
    WinLoc = pyautogui.locateOnScreen('Win_Logo.png', region=(0,0,1920,1080), confidence=0.6)
    time.sleep(0.1)
    print(WinLoc)

    time.sleep(0.1)
    WinPoint = pyautogui.center(WinLoc)
    time.sleep(0.1)
    print(WinPoint)

    time.sleep(0.1)
    Winx, Winy = WinPoint
    pyautogui.click(Winx, Winy)
    time.sleep(0.1)
    print("'Clicked Windows'")
    print(' ')


    time.sleep(1)


    ## Click Settings
    time.sleep(0.1)
    SetLoc = pyautogui.locateOnScreen('Settings_Logo.png', region=(0,0,1920,1080), confidence=0.5)
    time.sleep(0.1)
    print(SetLoc)

    time.sleep(0.1)
    SetPoint = pyautogui.center(SetLoc)
    time.sleep(0.1)
    print(SetPoint)

    time.sleep(0.1)
    Setx, Sety = SetPoint
    pyautogui.click(Setx, Sety)
    time.sleep(0.1)
    print("'Clicked Settings'")
    print(' ')


    time.sleep(1)


    ## Click Updates & Security
    time.sleep(0.1)
    UpdLoc = pyautogui.locateOnScreen('Update_Logo.png', region=(0,0,1920,1080), confidence=0.4)
    time.sleep(0.1)
    print(UpdLoc)

    time.sleep(0.1)
    UpdPoint = pyautogui.center(UpdLoc)
    time.sleep(0.1)
    print(UpdPoint)

    time.sleep(0.1)
    Updx, Updy = UpdPoint
    pyautogui.click(Updx, Updy)
    time.sleep(0.1)
    print("'Clicked Updates & Security'")
    print(' ')


    time.sleep(4)


    ## Click Check For Updates
    time.sleep(0.1)
    CheLoc = pyautogui.locateOnScreen('Check_Logo.png', region=(0,0,1920,1080), confidence=0.60)
    time.sleep(0.1)
    print(CheLoc)

    if CheLoc == None:
        print("Useless thing can't find Check for Updates Button!")

    time.sleep(0.1)
    ChePoint = pyautogui.center(CheLoc)
    time.sleep(0.1)
    print(ChePoint)

    time.sleep(0.1)
    Chex, Chey = ChePoint
    pyautogui.click(Chex, Chey)
    print("'Clicked Check for Updates'")
    print(' ')


    time.sleep(5)


    ## Click Restart Now
    time.sleep(0.1)
    NowLoc = pyautogui.locateOnScreen('Now_Logo.png', region=(0,0,1920,1080), confidence=0.55)
    time.sleep(0.1)
    print(NowLoc)

    if NowLoc == None:
        print("Useless thing can't find Restart now Button!")

    time.sleep(0.1)
    NowPoint = pyautogui.center(NowLoc)
    time.sleep(0.1)
    print(NowPoint)

    time.sleep(0.1)
    Nowx, Nowy = NowPoint
    pyautogui.click(Nowx, Nowy)
    print("'Clicked Restart now'")
    print(' ')


########## END OF FIRST SCRIPT
    

def Script2():

    time.sleep(5)

    ## Click windows
    time.sleep(0.1)
    Win2Loc = pyautogui.locateOnScreen('Win_Logo.png', region=(0,0,1920,1080), confidence=0.6)
    time.sleep(0.1)
    print(Win2Loc)

    time.sleep(0.1)
    Win2Point = pyautogui.center(Win2Loc)
    time.sleep(0.1)
    print(Win2Point)

    time.sleep(0.1)
    Win2x, Win2y = Win2Point
    pyautogui.click(Win2x, Win2y)
    print("'Clicked Windows2'")
    print(' ')


    time.sleep(1)


    ## Type compmgmt.msc
    time.sleep(0.5)
    pyautogui.write('compmgmt.msc', interval=0.12)
    
    time.sleep(0.75)
    pyautogui.press('enter')
    print("'Typed compmgmt.msc'")
    print(' ')


    time.sleep(1)


    ## Computer Manange Tab
    time.sleep(0.1)
    CompLoc = pyautogui.locateOnScreen('Comp_Logo.png', region=(1920,1080), confidence=0.5)
    print(CompLoc)

    time.sleep(0.1)
    CompPoint = pyautogui.center(CompLoc)
    print(CompPoint)

    time.sleep(0.1)
    Compx, Compy = CompPoint
    pyautogui.click(Compx, Compy)
    print("'Clicked Comp Manage Tab'")
    print(' ')


    time.sleep(1)


    ## Click Shared Folders
    time.sleep(0.1)
    SharedLoc = pyautogui.locateOnScreen('SharedFold_Logo.png', region=(0,0,1920,1080), confidence=0.5)
    print(SharedLoc)

    time.sleep(0.5)
    SharedPoint = pyautogui.center(SharedLoc)
    print(SharedPoint)

    time.sleep(0.5)
    Sharedx, Sharedy = SharedPoint
    pyautogui.click(Sharedx, Sharedy)
    print("'Clicked Shared folders'")
    print(' ')


########## END OF SECOND SCRIPT


def Script3():

    time.sleep(5)
    
    ## Click windows
    time.sleep(0.1)
    Win3Loc = pyautogui.locateOnScreen('Win_Logo.png', region=(0,0,1920,1080), confidence=0.6)
    print(Win3Loc)

    time.sleep(0.1)
    Win3Point = pyautogui.center(Win3Loc)
    print(Win3Point)

    time.sleep(0.1)
    Win3x, Win3y = Win3Point
    pyautogui.click(Win3x, Win3y)
    print("'Clicked Windows3'")
    print(' ')


    time.sleep(1)


    ## Type Control Panel
    time.sleep(0.5)
    pyautogui.write('Control Panel', interval=0.06)
    
    time.sleep(0.75)
    pyautogui.press('enter')
    print("'Typed Control Panel'")
    print(' ')

########## END OF THIRD SCRIPT


def Script4():

    time.sleep(5)

    ## Click windows
    time.sleep(0.1)
    Win4Loc = pyautogui.locateOnScreen('Win_Logo.png', region=(0,0,1920,1080), confidence=0.6)
    print(Win4Loc)

    time.sleep(0.1)
    Win4Point = pyautogui.center(Win4Loc)
    print(Win4Point)

    time.sleep(0.1)
    Win4x, Win4y = Win4Point
    pyautogui.click(Win4x, Win4y)
    print("'Clicked Windows4'")
    print(' ')


    time.sleep(1)


    ## Type Control Panel
    time.sleep(0.5)
    pyautogui.write('Control Panel', interval=0.08)
    
    time.sleep(0.75)
    pyautogui.press('enter')
    print("'Typed Control Panel'")
    print(' ')


    time.sleep(1)


    ## Click Category
    time.sleep(0.1)
    CateLoc = pyautogui.locateOnScreen('Category_Logo.png', region=(0,0,1920,1080), confidence=0.65)
    print(CateLoc)

    if CateLoc == None:
            ## Click User Accounts
            time.sleep(0.1)
            UserLoc = pyautogui.locateOnScreen('User_Logo.png', region=(0,0,1920,1080), confidence=0.6)
            print(UserLoc)

            time.sleep(0.1)
            UserPoint = pyautogui.center(UserLoc)
            print(UserPoint)

            time.sleep(0.1)
            Userx, Usery = UserPoint
            pyautogui.click(Userx, Usery)
            print("'Clicked Users'")
            print(' ')

    
    time.sleep(0.1)
    CatePoint = pyautogui.center(CateLoc)
    print(CatePoint)

    time.sleep(0.1)
    Catex, Catey = CatePoint
    pyautogui.click(Catex, Catey)
    print("'Clicked Categorys'")
    print(' ')


    time.sleep(1)












########## END OF FOURTH SCRIPT
    
####################### End of Scripts ###################################





## Define Button (Works With Place Button)
button_1 = Button(root, text= "Check For Updates", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script1)
button_2 = Button(root, text= "Open Shared Folders", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script2)
button_3 = Button(root, text= "Open Control Panel", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script3)
button_4 = Button(root, text= "Open User Accounts", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script4)
button_5 = Button(root, text= "Nil", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script4)
button_6 = Button(root, text= "Nil", padx= 50, pady= 50, font=("Consolas", 20, "bold"), command=Script4)

## Place Buttons (Works With Define Button)
button_1.grid(row=1, column=0 )
button_2.grid(row=1, column=1 )
button_3.grid(row=1, column=2 )
button_4.grid(row=2, column=0 )
button_5.grid(row=2, column=1 )
button_6.grid(row=2, column=2 )

root.mainloop()
