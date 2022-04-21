
from ast import Str
from cgitb import text
from queue import Empty
from tkinter import *
from tkinter.font import Font


# ventana principal
app = Tk()
app.title("Rowy")
app.geometry("960x540")
app.resizable(height=False, width=False)

# Fondos
imagen = PhotoImage(file="1.png")
imagen2 = PhotoImage(file="2.png")
botonLogin = PhotoImage(file="boton.png")
imagen3 = PhotoImage(file="3.png")
botonBack = PhotoImage(file="back.png")
# Pagína principal


def Mainmenu():
    # Lanzar la ventana Admin
    def Admin():
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background2 = Label(interfaz, image=imagen2)
        background2.pack()
        botonBack1 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack1.place(x=813, y=420, height=50, width=105)
        botonBack1.configure(height=2,
                             width=12)

    def Client():
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background3 = Label(interfaz, image=imagen3)
        background3.pack()
        botonBack2 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack2.place(x=813, y=420, height=50, width=105)

    # Comando boton Login
    def login():

        Error.config(text="")
        c1 = txt1.get()
        c2 = txt2.get()
        key = "admin"
        key2 = "client"
        if(c1 == "" or c2 == ""):  # Campos vacios
            Error.config(text="Empty fields")
        else:
            if(c1 == key):
                Admin()
            else:
                if(c1 == key2):
                    Client()
                else:
                    Error.config(text="")
                    Error.config(text="Invalid command")

    # Fondo ventana principal, botones y campos de textos
    # Fondo
    background = Label(image=imagen, text="fondo")
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Boton login
    boton = Button(text="Login", image=botonLogin, command=login)
    boton.place(x=813, y=420, height=58, width=105)

    boton.configure(height=2,
                    width=12)

    # Campos de texto
    txt1 = Entry(app, bg="grey89")
    txt1.place(x=514, y=200, width=400, height=54)
    txt2 = Entry(app, bg="grey89", show="*")
    txt2.place(x=514, y=326, width=400, height=54)
    Error = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
    Error.place(x=514, y=400)


# Lanzar ventana principal
Mainmenu()
app.mainloop()
