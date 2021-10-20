import tkinter as tk
BG='gray70'
FONT_TITLE=('locuda console', 22, 'bold')
FONT=('locuda console', 22)
main=tk.Tk()
main.geometry('500x433+124+122')
main.title=('Operations App')

frame=tk.Frame(main, bg=BG).place(relwidth=1, relheight=1)

labelTitle=tk.Label(frame, text='Operation App', bg=BG, font=FONT_TITLE).place(x=150, y=20)
labelX=tk.Label(frame, text='X', bg=BG, font=FONT).place(x=30, y=60)
entryX=tk.Entry(frame)
entryX.place(x=150, y=60, relwidth=0.66, relheight=0.09)

labelY=tk.Label(frame, text='Y', bg=BG, font=FONT).place(x=30, y=160)
entryY=tk.Entry(frame)
entryY.place(x=150, y=160, relwidth=0.66, relheight=0.09)

labelResult=tk.Label(frame, text='Result', bg=BG, font=FONT).\
    place(x=30, y=260)
entryResult=tk.Entry(frame)
entryResult.place(x=150, y=260, relwidth=0.66, relheight=0.09)

buttonPlus=tk.Button(frame, text='+', font=FONT)
buttonPlus.place(x=150, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=tk.Button(frame, text='-', font=FONT)
buttonPlus.place(x=242, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=tk.Button(frame, text='x', font=FONT)
buttonPlus.place(x=334, y=360, relwidth=0.11, relheight=0.1)

buttonPlus=tk.Button(frame, text='/', font=FONT)
buttonPlus.place(x=428, y=360, relwidth=0.11, relheight=0.1)
main.mainloop()