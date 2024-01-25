import tkinter
from tkinter import messagebox
import time as mtime
import datetime

message = input("Enter Message: ")
time = input("At Time (Format: 23:09): ")

#Time & Messsage checker
if len(message) < 1 or len(time) < 5:
    print("==========Error==========")
    print("Invalid mesage or time. Please check again. (Check: length check)")
    exit(None)
try:
    int(time[0:2])
except:
    print("==========Error==========")
    print("Invalid time. Please check again.(Check: int time)")
    exit(None)
if not int(time[0:2]) < 25 or not int(time[3:5]) < 60:  #Check if it's a valid time
    print("==========Error==========")
    print("Invalid time. Please check again. (Check: if time in 24h range)")
    exit(None)
elif int(time[0:2]) == 24 and int(time[3:5]) > 0:
    print("==========Error==========")
    print("Invalid time. Please check again. (Check: if time is 24 and minute > 0)")
    exit(None)

def show_message(message):
    root = tkinter.Tk()
    root.wm_attributes("-topmost", 1)
    root.withdraw()
    tkinter.messagebox.showinfo("MessageAlarm", message, parent=root)
    root.destroy()

current_time = datetime.datetime.now()

ntime = ""
if time[0] == "0" or time[3] == "0":
    ntime = time.replace("0", "")
else:
    ntime = time

def condition(ntime, current):
    if current.hour == int(ntime[0:ntime.find(":")]) and current.minute == int(ntime[(ntime.find(":")+1):(len(ntime))]):
        return True
    return False
mtime.sleep(0.5)
print("==========Information==========")
mtime.sleep(0.5)
print("Alarm set!")
mtime.sleep(0.5)
print("If alarm's not working, press Ctrl + C in console to stop the program (also please report that bug to Github in README)")
try:
    while not condition(ntime, current_time):
        current_time = datetime.datetime.now()
        mtime.sleep(0.5)
except KeyboardInterrupt:
    print("==========Error===========")
    print("Keyboard Interrupt")
    exit(None)

show_message(message)