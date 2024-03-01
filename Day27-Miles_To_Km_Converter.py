from tkinter import *

#Screen
screen=Tk()
screen.title("Miles to Km Converter")
screen.minsize(width=300,height=150)

#Entry

entry=Entry()
entry.grid(column=1,row=0,padx=10,pady=10)

#Label

miles_label=Label(text="Miles",font=("Serif",10,"bold"))
miles_label.grid(column=2,row=0,padx=10,pady=10)

#Text

simple_text=Label(text="is equal to",font=("Serif",10))
simple_text.grid(column=0,row=1,padx=10,pady=10)

#Answer

answer=Label(text="",font=("Serif",10))
answer.grid(column=1,row=1,padx=10,pady=10)

#Answer label

answer_label=Label(text="Km",font=("Serif",10,"bold"))
answer_label.grid(column=2,row=1,padx=10,pady=10)

#Button
def get_answer():
    miles=int(entry.get())
    km=1.609344*miles
    answer.config(text=f"{round(km,2)}")

button=Button(text="Calculate",command=get_answer)
button.grid(column=1,row=2,padx=10,pady=10)

screen.mainloop()