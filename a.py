from tkinter import * 
root = Tk()
root.config(bd=15)

leche = IntVar()
azucar = IntVar()



frame = Frame(root).pack(side=RIGHT)
Label(frame, text="¿Cómo quieres el café?\n").pack(anchor=W)
Checkbutton(frame, text="Con leche", variable=leche, 
            onvalue=1, offvalue=0).pack(anchor=W)
Checkbutton(frame, text="Con azúcar", variable=leche, 
            onvalue=1, offvalue=0).pack(anchor=W)

root.mainloop()