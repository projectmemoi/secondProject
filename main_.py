from tkinter import *
from  filleFunction import *
tkinter=Tk()


BG='gray80'
FONT_TITLE=('locuda console', 22, 'bold')
FONT=('locuda console', 22)


labelTitle=Label(tkinter, text='Operation App', bg=BG, font=FONT_TITLE)
labelTitle.place(x=150, y=20)

labelX=Label(tkinter, text='X', bg=BG, font=FONT)
labelX.place(x=30, y=60)

labelY=Label(tkinter, text='Y', bg=BG, font=FONT)
labelY.place(x=30, y=160)

labelResult=Label(tkinter, text='Result', bg=BG, font=FONT)
labelResult.place(x=30, y=260)


entryX=Entry(tkinter)
entryX.place(x=150, y=60, relwidth=0.66, relheight=0.09)

entryY=Entry(tkinter)
entryY.place(x=150, y=160, relwidth=0.66, relheight=0.09)

entryResult=Entry(tkinter)
entryResult.place(x=150, y=260, relwidth=0.66, relheight=0.09)

def addActionBut():
    addition(entryX.get(),entryY.get())

buttonAdd=Button(tkinter, text='+', font=FONT,command=addActionBut)
buttonAdd.place(x=150, y=360, relwidth=0.11, relheight=0.1)


def subActionBut():
    subtraction(entryX.get(),entryY.get())
buttonSub=Button(tkinter, text='-', font=FONT,command=subActionBut)
buttonSub.place(x=242, y=360, relwidth=0.11, relheight=0.1)

def mulActionBut():
    multiplication(entryX.get(),entryY.get())
buttonMul=Button(tkinter, text='x', font=FONT,command=mulActionBut)
buttonMul.place(x=334, y=360, relwidth=0.11, relheight=0.1)

def divActionBut():
    division(entryX.get(),entryY.get())
buttonDiv=Button(tkinter, text='/', font=FONT,command=divActionBut)
buttonDiv.place(x=428, y=360, relwidth=0.11, relheight=0.1)



tkinter.config(bg=BG)
tkinter.geometry('500x433+200+150')
tkinter.title=('Operations App')
tkinter.mainloop()