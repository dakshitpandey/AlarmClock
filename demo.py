import pygame
import datetime
import time
from tkinter.ttk import *
from tkinter import *
from datetime import datetime
from pygame import mixer
from time import sleep

#window
Window=Tk()
Window.title("")
Window.geometry("350x150")

def sound_alarm():
    mixer.music.load("myalarm.mp3")
    mixer.music.play()

def alarm():
    while true:
        control=1
        alarm_hour='11'
        alarm_minute='39'
        alarm_sec='00'
        alarm_period='PM'.upper()

        now=datetime.now

        hour=now.strftime("%I")
        minute=now.strftime("%M")
        second=now.strftime("%S")
        period=now.strftime("%p")

        if control==1:
            if alarm_period==period:
                if alarm_hour==hour:
                    if alarm_minute==minute:
                        if alarm_sec==second:
                            print("Time to take a break!")
                            sound_alarm()

        sleep(1)



mixer.init()
sound_alarm()






Window.mainloop()

