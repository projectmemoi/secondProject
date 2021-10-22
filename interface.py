from tkinter import *
root = Tk()

#هنا تكتب الكود انتاعك
#nameVariable =TypeVariable(خصائص المتغير)
#nameVariable.place(حجم و الموضع المتغير)
#مثال

labelX= Label(root, show=None, text='lable', font=('Arial', 20))
labelX.place(x=180, y=160, relwidth=0.3, relheight=0.1)

root.title("  X+Y=Z  interface !")
root.geometry('600x500')
root.mainloop()