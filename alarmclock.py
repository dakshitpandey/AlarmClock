from threading import Thread

from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
import pygame
import datetime
import time
from datetime import datetime
from pygame import mixer
from time import sleep

#colors
bg_color = '#ffffff'
col = '#566FC6'  #blue
col2= '#000000'  #black


#window
Window = Tk()
Window.title(" ")
Window.geometry("350x150")
Window.configure(bg=bg_color)


#frame up
frame_line= Frame(Window, width=400 ,height=5, bg=col)
frame_line.grid(row=0, column=0)


frame_body= Frame(Window, width=400 ,height=290, bg=bg_color)
frame_body.grid(row=1, column=0)

#configuring frame body
img=Image.open("clock1.png")
img.resize((100,100))
img= ImageTk.PhotoImage(img)

app_image=Label(frame_body,height=100,image=img,bg=bg_color)
app_image.place(x=10,y=10)



name = Label(frame_body,text="Alarm Clock",height=1,font=("Ivy 18 bold"),bg=bg_color)
name.place(x=125,y=10)


hour= Label(frame_body,text="Hour",height=1,font=("Ivy 10 bold"),fg=col,bg=bg_color)
hour.place(x=127,y=40)
c_hour=Combobox(frame_body,width=2,font=('arial 15'))
c_hour['values']=("00","01","02","03","04","05","06","07","08","09",
                 "10","11","12")
c_hour.current(0)
c_hour.place(x=130,y=58)


min= Label(frame_body,text="Min",height=1,font=("Ivy 10 bold"),fg=col,bg=bg_color)
min.place(x=177,y=40)
c_min=Combobox(frame_body,width=2,font=('arial 15'))
c_min['values']=("00","01","02","03","04","05","06","07","08","09",
                 "10","11","12","13","14","15","16","17","18","19",
                 "20","21","22","23","24","25","26","27","28","29",
                 "30","31","32","33","34","35","36","37","38","39",
                 "40","41","42","43","44","45","46","47","48","49",
                 "50","51","52","53","54","55","56","57","58","59","60")
c_min.current(0)
c_min.place(x=180,y=58)


sec= Label(frame_body,text="Sec",height=1,font=("Ivy 10 bold"),fg=col,bg=bg_color)
sec.place(x=227,y=40)
c_sec=Combobox(frame_body,width=2,font=('arial 15'))
c_sec['values']=("00","01","02","03","04","05","06","07","08","09",
                 "10","11","12","13","14","15","16","17","18","19",
                 "20","21","22","23","24","25","26","27","28","29",
                 "30","31","32","33","34","35","36","37","38","39",
                 "40","41","42","43","44","45","46","47","48","49",
                 "50","51","52","53","54","55","56","57","58","59","60")
c_sec.current(0)
c_sec.place(x=230,y=58)

Period= Label(frame_body,text="Period",height=1,font=("Ivy 10 bold"),fg=col,bg=bg_color)
Period.place(x=277,y=40)
c_Period=Combobox(frame_body,width=3,font=('arial 15'))
c_Period['values']=("AM","PM")
c_Period.current(0)
c_Period.place(x=280,y=58)

def activate_alarm():
    t=Thread(target=alarm)
    t.start( )

def deactivate_alarm():
    print("Deactivated alarm:",selected.get())
    mixer.music.stop()

selected= IntVar()


rad1= Radiobutton(frame_body,font=('aerial 10 bold'),value=1,text='Activate',bg=bg_color,command=activate_alarm,variable=selected)
rad1.place(x=125,y=95)

def sound_alarm():
    mixer.music.load("myalarm.mp3")
    mixer.music.play()
    selected.set(0)
    
    rad2= Radiobutton(frame_body,font=('aerial 10 bold'),value=2,text='Deactivate',bg=bg_color,command=deactivate_alarm,variable=selected)
    rad2.place(x=230,y=95)

def alarm():
    while True:
        control=selected.get()
        print(control)
        
        alarm_hour=c_hour.get()
        alarm_minute=c_min.get()
        alarm_sec=c_sec.get()
        alarm_period=c_Period.get()
        alarm_period= str(alarm_period).upper()

        now=datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")

        if control==1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time to take a break!")
                            sound_alarm()

        sleep(1)



mixer.init()









Window.mainloop()