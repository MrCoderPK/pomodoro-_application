from tkinter import *
import time
from tkinter.font import BOLD
Red="#FF6347"
green="#9ACD32"
skyblue="#87CEEB"
yellow="#FFD700"
indigo="#4B0082"
work_min=25
short_break=5
long_break=20
reps=0
font_name="Courier"
timer=None

def reset_timer():
    window.after_cancel(timer)    #stop the timer
    canvas.itemconfig(timer_label1,text="00:00")
    timer_label.config(text="Timer",fg="black")
    tick.config(text="")
    global reps
    reps=0

def count_down(count):
    count_min=count//60
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{count_sec}"
    elif count_min<10:
        count_min=f"0{count_min}"
    if count>0:
        global timer
        canvas.itemconfig(timer_label1,text=f"{count_min}:{count_sec}")
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            tick.config(text="✔"* (reps//2))


def start_timer():
    global reps
    reps+=1
    if (reps==1 or reps==3 or reps==5 or reps==7):
        count_down(work_min*60)
        timer_label.config(text="Work",fg=indigo)
    elif (reps==2 or reps==4 or reps==6):
        count_down(short_break*60)
        timer_label.config(text="Break",fg=Red) 
    elif reps>8:
        timer_label.config(text="You have completed it \n ...........Yay!",fg=Red)
        canvas.itemconfig(timer_label1, text="00:00")
        reps=0
        tick.config(text="")
        window.after_cancel(timer)
    else:
        count_down(long_break*60)
        timer_label.config(text="Long Break",fg=Red)

#UI setup

window=Tk()
window.config(padx=100,pady=50,bg=skyblue)   

timer_label=Label(text="Timer",font=(font_name,50,BOLD),bg=skyblue,fg="black")
timer_label.grid(row=0,column=1)

canvas=Canvas(width= 348,height=348,bg=skyblue,highlightthickness=0)
tomato=PhotoImage(file=r"E:\Pomodoro_GUI\TOMATO.png")
canvas.create_image(174,174,image=tomato)
timer_label1=canvas.create_text(170,190,text=f"00:00",font=(font_name,40,BOLD),fill="white") 
canvas.grid(row=1,column=1)

button=Button(text="Start",font=(font_name,10,BOLD),bg=yellow,fg="black",highlightthickness=0,command=start_timer)
button.grid(row=2,column=0)

reset=Button(text="Reset",font=(font_name,10,BOLD),bg=yellow,fg="black",highlightthickness=0,command=reset_timer)
reset.grid(row=2,column=2)

tick=Label(font=(font_name,20,BOLD),bg=skyblue,fg="red")
tick.grid(row=3,column=1)

window.mainloop()