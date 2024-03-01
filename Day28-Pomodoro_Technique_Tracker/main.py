
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_program():
    window.after_cancel(timer)
    global reps
    reps=0
    label.config(text="Timer",fg=GREEN)
    tick_canvas.config(text="")
    canvas.itemconfig(canva_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def trigger_start():
    global reps
    reps+=1

    if reps>8:
        reset_program()
        return

    if reps!=8 and reps%2==0:
        seconds = SHORT_BREAK_MIN * 60
        ticks = ""
        for x in range(0, reps // 2):
            ticks += "✓"
        tick_canvas.config(text=ticks)
        label.config(text="Short Break",fg=PINK)
    elif reps%8==0:
        seconds = LONG_BREAK_MIN * 60
        ticks = ""
        for x in range(0, reps // 2):
            ticks += "✓"
        tick_canvas.config(text=ticks)
        label.config(text="Long Break",fg=RED)
    else:
        seconds=WORK_MIN*60
        label.config(text="Work Time")
    count_time(seconds)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_time(count):
    global timer
    hr=count//60
    min=count%60
    if min<10:
        min="0"+str(min)
    canvas.itemconfig(canva_text,text=f"{hr}:{min}")
    if count>0:
        timer=window.after(1000,count_time,count-1)
    else:
        trigger_start()

# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window=Tk()
window.title("Pomodoro Technique")
window.config(padx=100,pady=50,bg=YELLOW)

#Label

label=Label(text="Timer",font=(FONT_NAME,50,"bold"))
label.config(bg=YELLOW,fg=GREEN)
label.grid(column=1,row=0)

#Canvas
tomato=PhotoImage(file="tomato.png")
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato)
canva_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,35,"bold"),fill="white")
canvas.grid(column=1,row=1)

#Start Button

start_btn=Button(text="Start",font=(FONT_NAME,8),command=trigger_start)
start_btn.grid(column=0,row=2)

#Tick Marks

tick_canvas=Label(text="",fg=GREEN,bg=YELLOW,font=("Arial",15,"bold"))
tick_canvas.grid(column=1,row=3)

#Reset Button

reset_btn=Button(text="Reset",font=(FONT_NAME,8),command=reset_program)
reset_btn.grid(column=2,row=2)


window.mainloop()