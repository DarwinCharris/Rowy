
from ast import Str
from cgitb import text
from queue import Empty
from tkinter import *  # seleccionar lo que necesitamos
from tkinter.font import Font
from msilib.schema import Error
import mysql.connector
from mysql.connector import Error
from re import search
# Conectar a la base de datos
try:
    conexion = mysql.connector.connect(
        host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
    )
    if conexion.is_connected():  # Borrarlo ahorita
        print("Conexión exitosa")

except Error as ex:
    print("Error de conexión", ex)


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
botonAdd1 = PhotoImage(file = "AddClient.png")
btnModi = PhotoImage(file = "Mod.png")
btnDele = PhotoImage(file="Delete.png")
imagen2_1 = PhotoImage(file = "2_1.png")
# Pagína principal


def Mainmenu():
    
        
    def agregarClient ():
        def val2_1 (sname:str, sLname:str, smail:str, spword:str,sid:str):
            #Metodo que permite validar los campos
            #creación de 5 claves para poder avanzar
            keyN=False
            KeyLN= False
            KeyM = False
            KeyP = False
            KeyI=False
            #Validación nombre
            if(sname == ""):
                ErrorName.config(text="")
                ErrorName.config(text="Empty Field")
            else:
                KeyN = True
            #Validar Apellido
            if(sLname == ""):
                ErrorLName.config(text ="")
                ErrorLName.config(text="Empty Field")
            else:
                KeyLN = True
            #validar Correo
            if(smail == ""):
                ErrorMail.config(text="")
                ErrorMail.config(text="Empty Field")
            else:
                #No permitir que el correo tenga el dominio de la empresa
                if search("@rowy.com", smail):
                    ErrorMail.config(text="")
                    ErrorMail.config(text="Mail not available")
                #Comprobar si el email está ocupado 
                else:
                    cursor = conexion.cursor()
                    cursor.execute("SELECT mail FROM Clientes WHERE mail='"+smail+"'")
                    mail = cursor.fetchone()
                    print(mail)
                    if(mail != None):
                        ErrorMail.config(text="")
                        ErrorMail.config(text="Mail not available")
                    else:
                        KeyM = True
                        print("correo listooo")
            #Validar Contrasela
            if(spword == ""):
                ErrorPword.config(text="")
                ErrorPword.config(text="Empty Field")
            else:
                KeyP = True
            #Validar Cedula
            if(sid == ""):
                ErrorID.config(text="")
                ErrorID.config(text="Empty Field")
            else:
                #Validar si está en la base de datos
                cursor = conexion.cursor()
                cursor.execute("SELECT cedula FROM Clientes WHERE cedula="+sid)#Ver si esto funciona pq ced es numero
                ced = cursor.fetchone()
                if(ced != None):
                    ErrorID.config(text="")
                    ErrorID.config(text="The client already exists")
                else:
                    KeyI =True
                #condicion todas las llaves son correctas lance la pagina de los datos secundarios 
            

                
        #Agregar el fondo
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background2_1 = Label(interfaz, image=imagen2_1)
        background2_1.pack()
        #botones del panel lateral
        botonMod = Button(image= btnModi)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        botonDelete = Button(image= btnDele)
        botonDelete.place(x=22, y=355, height=53, width=176)
        botonDelete.configure(borderwidth=0)
        #Campos de texto
        txtname = Entry(app, bg="grey89")
        txtname.place(x=245, y=220, width=275, height=55)
        txtLname = Entry(app, bg="grey89")
        txtLname.place(x=557, y=220, width=275, height=55)
        txtEmail = Entry(app, bg="grey89")
        txtEmail.place(x=245, y=339, width=275, height=55)
        txtPword = Entry(app, bg="grey89")
        txtPword.place(x=557, y=339, width=275, height=55)
        txtID = Entry(app, bg="grey89")
        txtID.place(x=245, y=447, width=275, height=55)
        #Obtener la info de los campos de texto
        sname = txtname.get()
        sLname = txtLname.get()
        smail = txtEmail.get()
        spword = txtPword.get()
        sid = txtID.get()
        #Campos de texto para errores
        ErrorName = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
        ErrorName.place(x=245, y=276)
        ErrorLName = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
        ErrorLName.place(x=557, y=276)
        ErrorMail = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
        ErrorMail.place(x=245, y=400)
        ErrorPword = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
        ErrorPword.place(x=557, y=400)
        ErrorID = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
        ErrorID.place(x=245, y=505)
    
    # Lanzar la ventana Admin
    def Admin():
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background2 = Label(interfaz, image=imagen2)
        background2.pack()
        botonBack1 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack1.place(x=46, y=450, height=50, width=105)
        botonBack1.configure(height=2,
                             width=12)
        botonAdd = Button(image= botonAdd1, command=agregarClient)
        botonAdd.place(x=20, y=191, height=54, width=181)
        botonAdd.configure(borderwidth=0)
        botonMod = Button(image= btnModi)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        botonDelete = Button(image= btnDele)
        botonDelete.place(x=22, y=355, height=53, width=176)
        botonDelete.configure(borderwidth=0)

    def Client():
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background3 = Label(interfaz, image=imagen3)
        background3.pack()
        botonBack2 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack2.place(x=813, y=420, height=50, width=105)
    

    def validarAdmin(c1: Str, c2: Str):
        # Conseguir el email en la base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT mail FROM Admin WHERE mail='"+c1+"'")
        mail = cursor.fetchone()
        print(mail)  # Borrar despues
        # validar si está, si no es none, significa que está
        if(mail != None):
            print("hurra")
            # Comporbar si la contraseña está bien
            cursor.execute(
                "SELECT password FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
            passw = cursor.fetchone()
            print(passw)
            # validar si la contraseña es correcta

            if(passw != None):
                print("Contraseña correcta")
                # Lanzar Admin page
                Admin()
            else:
                print("COntraseña incorrecta")
                Error.config(text="")
                Error.config(text="Invalid password")
        else:
            print("email no existe")
            Error.config(text="")
            Error.config(text="Invalid mail")
    # Validar cliente

    def validarClient(c1: Str, c2: Str):
        # Conseguir el email en la base de datos
        cursor = conexion.cursor()
        cursor.execute("SELECT mail FROM Clientes WHERE mail='"+c1+"'")
        mail = cursor.fetchone()
        print(mail)
        # validar si está, si no es none, significa que está
        if(mail != None):
            print("hurra")
            # Comporbar si la contraseña está bien
            cursor.execute(
                "SELECT password FROM Clientes WHERE mail='"+c1+"' AND password='"+c2+"'")
            passw = cursor.fetchone()
            print(passw)
            # validar si la contraseña es correcta
            contraseña = "('"+c2+"',)"
            if(passw != None):
                print("Contraseña correcta")
                # Lanzar Admin page
                Client()
            else:
                print("COntraseña incorrecta")
                Error.config(text="")
                Error.config(text="Invalid password")

        else:
            print("email no existe")
            Error.config(text="")
            Error.config(text="Invalid mail")

    # Comando boton Login
    def login():

        Error.config(text="")
        c1 = txt1.get()
        c2 = txt2.get()

        if(c1 == "" or c2 == ""):  # Campos vacios
            Error.config(text="Empty fields")
        else:
            # Conseguir el email en la base de datos
            if search("@rowy.com", c1):
                validarAdmin(c1, c2)
            else:
                validarClient(c1, c2)

    # Fondo ventana principal, botones y campos de textos
    # Fondo
    background = Label(image=imagen, text="fondo")
    background.place(x=0, y=0, relwidth=1, relheight=1)

    # Boton login
    boton = Button(image=botonLogin, command=login)
    boton.place(x=813, y=420, height=58, width=105)

    boton.configure(height=2,
                    width=12)

    # Campos de texto
    txt1 = Entry(app, bg="grey89")
    txt1.place(x=514, y=200, width=400, height=54)
    txt2 = Entry(app, bg="grey89", show="*")
    txt2.place(x=514, y=326, width=400, height=54)
    #Label de error 
    Error = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
    Error.place(x=514, y=400)


# Lanzar ventana principal
Mainmenu()
app.mainloop()
# Cerrar la base de datos
if conexion.is_connected():
    conexion.close()
    print("bye")
