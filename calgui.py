from Tkinter import *
import tkMessageBox
import Tkinter



top = Tkinter.Tk()

L1 = Label(top, text="Enter Unit of Length")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = LEFT)



CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

C1 = Checkbutton(top, text = "Inches", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(top, text = "Feet", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

C3 = Checkbutton(top, text = "Centimeters", variable = CheckVar3, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)

C4 = Checkbutton(top, text = "Meters", variable = CheckVar4, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)


C1.pack()
C2.pack()
C3.pack()
C4.pack()
top.mainloop()

top = Tk()

top.mainloop()
