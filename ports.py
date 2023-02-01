import os
from os import path
from tkinter import messagebox as mgbx
from time import sleep

usb = "D:/"

def usbconx(path, time):
    timers = int(time)
    if path == usb:
        if os.path.exists(usb):
            mgbx.showinfo("USB", "USB connected")
            sleep(timers)

def headphones(path, time):
    auphone = path
    timers = int(time)
    if os.path.exists(auphone):
        mgbx.showinfo("Headphone", "Headphones connected")
        sleep(timers)