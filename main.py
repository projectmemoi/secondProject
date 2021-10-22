from tkinter import *
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

buttonAdd=Button(tkinter, text='+', font=FONT)
buttonAdd.place(x=150, y=360, relwidth=0.11, relheight=0.1)

buttonSub=Button(tkinter, text='-', font=FONT)
buttonSub.place(x=242, y=360, relwidth=0.11, relheight=0.1)

buttonMul=Button(tkinter, text='x', font=FONT)
buttonMul.place(x=334, y=360, relwidth=0.11, relheight=0.1)

buttonDiv=Button(tkinter, text='/', font=FONT)
buttonDiv.place(x=428, y=360, relwidth=0.11, relheight=0.1)


tkinter.config(bg=BG)
tkinter.geometry('500x433+200+150')
tkinter.title=('Operations App')
tkinter.mainloop()