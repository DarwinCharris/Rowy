
from ast import Str
from cgitb import text
from queue import Empty
from tkinter import *  # seleccionar lo que necesitamos
from tkinter.font import Font
from msilib.schema import Error
import mysql.connector
from mysql.connector import Error
from re import search
import Classes as cs
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
botonAdd1 = PhotoImage(file="AddClient.png")
btnModi = PhotoImage(file="Mod.png")
btnDele = PhotoImage(file="Delete.png")
imagen2_1 = PhotoImage(file="2_1.png")
btnnext = PhotoImage(file="next.png")
imagen2_2 = PhotoImage(file="2_2.png")

# Objeto cliente y admin
administrator = cs.admin(None, None, None, None, None)
# Agregar un objeto cliente con todos sus atributos nulos
client = cs.clientdata(None, None, None, None, None,
                       None, None, None, None, None, None)


# Pagína principal


def Mainmenu():

    def agregarClient():
        # Lanzar a la sig pagina
        def add2_2():
            def next2():
                def validate():
                    ErrorPhone.config(text="")
                    ErrorPlan.config(text="")
                    ErrorCnumber.config(text="")
                    ErrorEdate.config(text="")
                    ErrorCSV.config(text="")
                    # Llaves para validar
                    keyPhone = False
                    keyPlan = False
                    keyCnumber = False
                    keyEdate = False
                    keycvs = False
                    # Validar telefono
                    if(phone == ""):
                        ErrorPhone.config(text="")
                        ErrorPhone.config(text="Empty field")
                    else:
                        # Buscar en base de datos [Pendiente]
                        keyPhone = True
                    # Validar plan
                    if(plan == ""):
                        ErrorPlan.config(text="")
                        ErrorPlan.config(text="Empty field")
                    else:
                        if(plan < 1 or plan > 3):
                            ErrorPlan.config(text="")
                            ErrorPlan.config(text="Invalid plan")
                        else:
                            keyPlan = True
                    # Validar Cnumber
                    # Ver como se valida eso
                    # continuarrr

                phone = txtphone.get()
                plan = txtPlan.get()
                cnumber = txtCnumber.get()
                edate = txtEdate.get()
                csv = txtCSV.get()
                client.telephone = phone
                client.plan = plan
                client.cardnumber = cnumber
                client.expdate = edate
                client.cod = csv
                administrator.addclient(client.name, client.lastname, client.mail, client.password, client.password,
                                        client.telephone, client.plan, client.cardnumber, client.expdate, client.cod)  # todos los parametros

            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            background2_2 = Label(interfaz, image=imagen2_2)
            background2_2.pack()
            # Campos de texto

            def validate_cc(text: str):
                return text.isdecimal()
            txtphone = Entry(app, bg="grey89", validate="key",
                             validatecommand=(app.register(validate_cc), "%S"))
            txtphone.place(x=245, y=220, width=275, height=55)
            txtPlan = Entry(app, bg="grey89", validate="key",
                            validatecommand=(app.register(validate_cc), "%S"))
            txtPlan.place(x=557, y=220, width=275, height=55)
            txtCnumber = Entry(app, bg="grey89")
            txtCnumber.place(x=245, y=339, width=275, height=55)
            txtEdate = Entry(app, bg="grey89")
            txtEdate.place(x=557, y=339, width=275, height=55)
            txtCSV = Entry(app, bg="grey89", validate="key", validatecommand=(
                app.register(validate_cc), "%S"), show="*")
            txtCSV.place(x=245, y=448, width=275, height=55)
            # Boton next2
            # agregar metodo de validaciones
            btnNext2 = Button(image=btnnext, command=next2)
            btnNext2.place(x=630, y=448, height=51, width=136)
            btnNext2.configure(borderwidth=0)
            # Label error
            ErrorPhone = Label(app, text="", font=20,
                               fg="#E41111", bg="#FAFBFD")
            ErrorPhone.place(x=245, y=276)
            ErrorPlan = Label(app, text="", font=20,
                              fg="#E41111", bg="#FAFBFD")
            ErrorPlan.place(x=557, y=276)
            ErrorCnumber = Label(app, text="", font=20,
                                 fg="#E41111", bg="#FAFBFD")
            ErrorCnumber.place(x=245, y=400)
            ErrorEdate = Label(app, text="", font=20,
                               fg="#E41111", bg="#FAFBFD")
            ErrorEdate.place(x=557, y=400)
            ErrorCSV = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorCSV.place(x=245, y=505)
        # Metodo del boton next

        def next1():
            # Validación de campos
            def val2_1():

                ErrorName.config(text="")
                ErrorLName.config(text="")
                ErrorMail.config(text="")
                ErrorPword.config(text="")
                ErrorID.config(text="")
                # Metodo que permite validar los campos
                # creación de 5 llaves para poder avanzar
                keyN = 0
                KeyLN = 0
                KeyM = 0
                KeyP = 0
                KeyI = 0
                # Validación nombre
                if(sname == ""):
                    ErrorName.config(text="")
                    ErrorName.config(text="Empty Field")
                else:
                    keyN = 1
                # Validar Apellido
                if(sLname == ""):
                    ErrorLName.config(text="")
                    ErrorLName.config(text="Empty Field")
                else:
                    KeyLN = 1
                # validar Correo
                if(smail == ""):
                    ErrorMail.config(text="")
                    ErrorMail.config(text="Empty Field")
                else:
                    # No permitir que el correo tenga el dominio de la empresa
                    if search("@rowy.com", smail):
                        ErrorMail.config(text="")
                        ErrorMail.config(text="Mail not available")
                    # Comprobar si el email está ocupado
                    else:
                        cursor = conexion.cursor()
                        cursor.execute(
                            "SELECT mail FROM Clientes WHERE mail='"+smail+"'")
                        mail = cursor.fetchone()
                        if(mail != None):
                            ErrorMail.config(text="")
                            ErrorMail.config(text="Mail not available")
                        else:
                            # comprobar si tiene alguno de los dominios validos
                            if(search("@gmail.com", smail) or search("@hotmail.com", smail) or search("@outlook.com", smail) or search("@yahoo.com", smail)):
                                KeyM = 1
                            else:
                                ErrorMail.config(text="")
                                ErrorMail.config(text="Mail not available")
                # Validar Contrasela
                if(spword == ""):
                    ErrorPword.config(text="")
                    ErrorPword.config(text="Empty Field")
                else:
                    KeyP = 1
                # Validar Cedula
                if(sid == ""):
                    ErrorID.config(text="")
                    ErrorID.config(text="Empty Field")
                else:
                    # Validar si está en la base de datos
                    cursor = conexion.cursor()
                    # Ver si esto funciona pq ced es numero
                    cursor.execute(
                        "SELECT cedula FROM Clientes WHERE cedula='"+sid+"'")
                    ced = cursor.fetchone()
                    if(ced != None):
                        ErrorID.config(text="")
                        ErrorID.config(text="The client already exists")
                    else:
                        if(len(sid) != 10):
                            ErrorID.config(text="")
                            ErrorID.config(text="Invalid CC")
                        else:
                            KeyI = 1
                    # condicion todas las llaves son correctas lance la pagina de los datos secundarios

                if(keyN == 1 and KeyLN == 1 and KeyM == 1 and KeyP == 1 and KeyI == True):
                    # Acá toca rescatar las variables, meterlas en un objeto de la calse clientdata para al final meterla a la db
                    # Colocar las variables obtenidas como atributos del objeto cliente
                    client.name = sname
                    client.lastname = sLname
                    client.mail = smail
                    client.password = spword
                    client.cedula = sid
                    add2_2()
            sname = txtname.get()
            sLname = txtLname.get()
            smail = txtEmail.get()
            spword = txtPword.get()
            sid = txtID.get()
            val2_1()

        # Agregar el fondo
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background2_1 = Label(interfaz, image=imagen2_1)
        background2_1.pack()
        # botones del panel lateral
        botonMod = Button(image=btnModi)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        botonDelete = Button(image=btnDele)
        botonDelete.place(x=22, y=355, height=53, width=176)
        botonDelete.configure(borderwidth=0)
        # Campos de texto
        txtname = Entry(app, bg="grey89")
        txtname.place(x=245, y=220, width=275, height=55)
        txtLname = Entry(app, bg="grey89")
        txtLname.place(x=557, y=220, width=275, height=55)
        txtEmail = Entry(app, bg="grey89")
        txtEmail.place(x=245, y=339, width=275, height=55)
        txtPword = Entry(app, bg="grey89", show="*")
        txtPword.place(x=557, y=339, width=275, height=55)

        def validate_cc(text: str):
            return text.isdecimal()
        txtID = Entry(app, bg="grey89", validate="key",
                      validatecommand=(app.register(validate_cc), "%S"))
        txtID.place(x=245, y=448, width=275, height=55)
        # Obtener la info de los campos de texto
        sname = txtname.get()
        sLname = txtLname.get()
        smail = txtEmail.get()
        spword = txtPword.get()
        sid = txtID.get()

        # Label para errores
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
        # Botón next
        btnNext = Button(image=btnnext, command=next1)
        btnNext.place(x=630, y=448, height=51, width=136)
        btnNext.configure(borderwidth=0)
        print(administrator.lastname)

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
        botonAdd = Button(image=botonAdd1, command=agregarClient)
        botonAdd.place(x=20, y=191, height=54, width=181)
        botonAdd.configure(borderwidth=0)
        botonMod = Button(image=btnModi)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        botonDelete = Button(image=btnDele)
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

    # Comando boton Login
    def login():
        # Validar cliente
        def validarClient(c1: Str, c2: Str):
            # Conseguir el email en la base de datos
            cursor = conexion.cursor()
            cursor.execute("SELECT mail FROM Clientes WHERE mail='"+c1+"'")
            mail = cursor.fetchone()

            # validar si está, si no es none, significa que está
            if(mail != None):
                # Comporbar si la contraseña está bien
                cursor.execute(
                    "SELECT password FROM Clientes WHERE mail='"+c1+"' AND password='"+c2+"'")
                passw = cursor.fetchone()
                # validar si la contraseña es correcta
                contraseña = "('"+c2+"',)"
                if(passw != None):

                    # Lanzar Admin page
                    Client()
                else:
                    Error.config(text="")
                    Error.config(text="Invalid password")
            else:
                Error.config(text="")
                Error.config(text="Invalid mail")
        # validad admin

        def validarAdmin(c1: Str, c2: Str):
            # Conseguir el email en la base de datos
            cursor = conexion.cursor()
            cursor.execute("SELECT mail FROM Admin WHERE mail='"+c1+"'")
            mail = cursor.fetchone()

            # validar si está, si no es none, significa que está
            if(mail != None):

                # Comporbar si la contraseña está bien
                cursor.execute(
                    "SELECT password FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                passw = cursor.fetchone()

                # validar si la contraseña es correcta

                if(passw != None):

                    cursor.execute(
                        "SELECT cedula FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                    cedula = cursor.fetchone()

                    cursor.execute(
                        "SELECT name FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                    name = cursor.fetchone()
                    cursor.execute(
                        "SELECT lasName FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                    Aped = cursor.fetchone()
                    # Se agregan los atributos del objeto administrator
                    administrator.cc = cedula
                    administrator.name = name
                    administrator.lastname = Aped
                    administrator.mail = mail
                    administrator.password = passw
                    # Lanzar Admin page
                    Admin()

                else:

                    Error.config(text="")
                    Error.config(text="Invalid password")
            else:

                Error.config(text="")
                Error.config(text="Invalid mail")

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
    # Label de error
    Error = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
    Error.place(x=514, y=400)


# Lanzar ventana principal
Mainmenu()
app.mainloop()
# Cerrar la base de datos
if conexion.is_connected():
    conexion.close()
    print("bye")
