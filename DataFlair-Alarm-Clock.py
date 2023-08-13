import tkinter as tk #import th required libraries
from tkinter import *
from tkinter import messagebox
import os,time,winsound

create=tk.Tk()#create window
create.title("ALARM CLOCK")
create.geometry("400x150")#set geometry

def createWidget():
    label1=Label(create,text='Enter the time in hh:mm',bg='black',fg='white')
    label1.grid(row=0,column=0,padx=5,pady=2)

    global entry1
    entry1=Entry(create,width=10,bg='black',fg='white')#Entry box to enter time in 24 hour format
    entry1.grid(row=0,column=1)

    label2=Label(create,text='Enter the message of alarm',fg='white',bg='dark blue')
    label2.grid(row=1,column=0,padx=5,pady=2)

    global entry2
    entry2=Entry(create,width=25,fg='white',bg='dark blue')#Entry box to input message of alarm
    entry2.grid(row=1,column=1)

    but=Button(create,text="submit",width=10,command=submit)
    but.grid(row=2,column=1)

    global label3
    label3=Label(create,text=" ",bg='green')#empty space to configure the text difference
    label3.grid(row=4,column=0)

def message1():
    global entry1,label3
    Alarm_time_lable=entry1.get()#the alarm time input will be stored
    label3.config(text='The alarm is counting')
    messagebox.showinfo('Alarm Clock',f'The Alarm time is{Alarm_time_lable}')

def submit():

    global entry1,entry2,labe3
    Alarm_time=entry1.get()
    message1()#calling message function
    current_time=time.strftime("%H:%M")#gets the current time
    alarm_message=entry2.get()
    print('The alarm time is:',Alarm_time)
    while Alarm_time!=current_time:#infinite loop
        current_time=time.strftime('%H:%M')
        time.sleep(1)#waits for one second
    if Alarm_time==current_time:#checks whether set alarm time is equal to current time
        print('playing alarm sound')
        winsound.PlaySound('sound.wav',winsound.SND_ALIAS)

        label3.config(text='Alarm Sound Playing<<<<<<')
        messagebox.showinfo("Alarm Message",f'the message is:{alarm_message}')


createWidget()#call the function

create.mainloop()
