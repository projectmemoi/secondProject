from tkinter import *
BG='gray20'
FONT_TITLE=('locuda console', 22, 'bold')
FONT=('locuda console', 22)
main=Tk()
main.geometry('500x433+200+150')
main.title=('Operations App')

main.config(bg=BG)

labelTitle=Label(main, text='Operation App', bg=BG, font=FONT_TITLE).place(x=150, y=20)

labelX=Label(main, text='X', bg=BG, font=FONT).place(x=30, y=60)
entryX=Entry(main)
entryX.place(x=150, y=60, relwidth=0.66, relheight=0.09)

labelY=Label(main, text='Y', bg=BG, font=FONT).place(x=30, y=160)
entryY=Entry(main)
entryY.place(x=150, y=160, relwidth=0.66, relheight=0.09)

labelResult=Label(main, text='Result', bg=BG, font=FONT).\
    place(x=30, y=260)
entryResult=Entry(main)
entryResult.place(x=150, y=260, relwidth=0.66, relheight=0.09)

buttonPlus=Button(main, text='+', font=FONT)
buttonPlus.place(x=150, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=Button(main, text='-', font=FONT)
buttonPlus.place(x=242, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=Button(main, text='x', font=FONT)
buttonPlus.place(x=334, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=Button(main, text='/', font=FONT)
buttonPlus.place(x=428, y=360, relwidth=0.11, relheight=0.1)
main.mainloop()