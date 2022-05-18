
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
imagen2_31 = PhotoImage(file = "2_31.png")
btndeleteok = PhotoImage(file= "deleteok.png")
imagen2_22 = PhotoImage(file="2_22.png")
imagen2_3 = PhotoImage(file ="2_3.png")

# Objeto cliente y admin
administrator = cs.admin(None, None, None, None, None)
# Objeto cliente
client = cs.clientdata(None, None, None, None, None,
                       None, None, None, None, None, None, None, None, None, None, None, None)


# Pagína principal


def Mainmenu():

    
    # Lanzar la ventana Admin
    def Admin():
        def agregarClient():
            # Lanzar a la sig pagina
            def add2_2():
                def add_3():
                    def next3 ():
                        def validatedef():
                            #Limpiar Lables 
                            ErrorLplate.config(text="")
                            ErrorVinN.config(text="")
                            ErrorCdate.config(text="")
                            ErrorColor.config(text="")
                            ErrorBrand.config(text="")
                            #LLaves
                            keylincese = False
                            keyVin = False
                            keyCdate = False
                            keyColor = False
                            keyBrand = False
                            #Comenzar a validar
                            #Validar lisencia
                            if(license == ""):
                                ErrorLplate.config(text="")
                                ErrorLplate.config(text="Empty field")
                            else:
                                keylincese = True
                            #Validar Num VIN
                            if(Vin == ""):
                                ErrorVinN.config(text="")
                                ErrorVinN.config(text="Empty field")
                            else:
                                keyVin = True
                            #Validar monto de dinero
                            if(Cdate == ""):
                                ErrorCdate.config(text="")
                                ErrorCdate.config(text="Empty field")
                            else:
                                monto = int(Cdate)
                                if(monto<10000):
                                    ErrorCdate.config(text="")
                                    ErrorCdate.config(text="Isn't sufficient money")
                                else:
                                    keyCdate = True
                            #Validar color
                            if(color == ""):
                                ErrorColor.config(text="")
                                ErrorColor.config(text="Empty field")
                            else:
                                keyColor = True
                            #Validar marca
                            if(brand == ""):
                                ErrorBrand.config(text="")
                                ErrorBrand.config(text="Empty field")
                            else:
                                keyBrand = True
                            #Si todo está bien guardar datos y agregar
                            if(keylincese == True and keyVin == True and keyCdate == True and keyColor == True 
                                    and keyBrand == True):
                                client.licenseplate = license
                                client.numVIN = Vin
                                client.dateB = Cdate
                                client.color = color
                                client.brand = brand
                                #Metodo agregar cliente 
                                administrator.addclient(client.name, client.lastname, client.mail, client.password,
                                    client.cedula, client.telephone, client.plan, client.cardnumber, client.expdate, 
                                    client.cod,client.licenseplate, client.numVIN, client.dateB, client.color, client.brand)
                                Admin()

                        license = txtLplate.get()
                        Vin = txtVinN.get()
                        Cdate = txtCdate.get()
                        color = txtColor.get()
                        brand = txtBrand.get()
                        validatedef()
                    for ele in app.winfo_children():
                        ele.destroy()
                    interfaz = Canvas(app)
                    interfaz.pack()
                    background2_2 = Label(interfaz, image=imagen2_3)
                    background2_2.pack()
                    #Campos de text
                    def validate_cc(text: str):
                        return text.isdecimal()
                    txtLplate = Entry(app, bg="grey89")
                    txtLplate.place(x=245, y=220, width=275, height=55)
                    txtVinN = Entry(app, bg="grey89")
                    txtVinN.place(x=557, y=220, width=275, height=55)
                    txtCdate = Entry(app, bg="grey89")
                    txtCdate.place(x=245, y=339, width=275, height=55)
                    txtColor = Entry(app, bg="grey89")
                    txtColor.place(x=557, y=339, width=275, height=55)
                    txtBrand = Entry(app, bg="grey89")
                    txtBrand.place(x=245, y=448, width=275, height=55)
                    #Botones laterales
                    botonMod = Button(image=btnModi, command=modificarCliente)
                    botonMod.place(x=23, y=267, height=53, width=168)
                    botonMod.configure(borderwidth=0)
                    botonDelete = Button(image=btnDele, command=eliminarCliente)
                    botonDelete.place(x=22, y=355, height=53, width=176)
                    botonDelete.configure(borderwidth=0)
                    botonBack1 = Button(text="Back", image=botonBack, command=add2_2)
                    botonBack1.place(x=46, y=450, height=41, width=105)
                    botonBack1.configure( borderwidth=0)
                    #Label para errores
                    ErrorLplate = Label(app, text="", font=20,
                                    fg="#E41111", bg="#FAFBFD")
                    ErrorLplate.place(x=245, y=276)
                    ErrorVinN = Label(app, text="", font=20,
                                    fg="#E41111", bg="#FAFBFD")
                    ErrorVinN.place(x=557, y=276)
                    ErrorCdate = Label(app, text="", font=20,
                                        fg="#E41111", bg="#FAFBFD")
                    ErrorCdate.place(x=245, y=400)
                    ErrorColor = Label(app, text="", font=20,
                                    fg="#E41111", bg="#FAFBFD")
                    ErrorColor.place(x=557, y=400)
                    ErrorBrand = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
                    ErrorBrand.place(x=245, y=505)
                    #Boton ok
                    btnOK = Button(image=btnnext, command=next3)
                    btnOK.place(x=630, y=448, height=41, width=105)
                    btnOK.configure(borderwidth=0)

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
                            # Buscar en base de datos
                            cursor = conexion.cursor()
                            cursor.execute(
                                "SELECT mail FROM Clientes WHERE telephone='"+phone+"'")
                            tele = cursor.fetchone()
                            if(tele != None): #El numero ya existe
                                ErrorPhone.config(text="")
                                ErrorPhone.config(text="Telephone already exist")
                            else:
                                keyPhone = True
                        # Validar plan
                        if(plan == ""):
                            ErrorPlan.config(text="")
                            ErrorPlan.config(text="Empty field")
                        else:
                            planv = int(plan)
                            if(planv<1 and planv>3):
                                ErrorPlan.config(text="")
                                ErrorPlan.config(text="Invalid plan")
                            else:
                                keyPlan = True
                        #Validad card number
                        if(cnumber == ""):
                            ErrorCnumber.config(text="")
                            ErrorCnumber.config(text="Empty field")
                        else:
                            if(len(cnumber)!= 16):
                                ErrorCnumber.config(text="")
                                ErrorCnumber.config(text="Incorrect value")
                            else:
                                keyCnumber = True
                        #Validar expedition date
                        if(edate == ""):
                            ErrorEdate.config(text="")
                            ErrorEdate.config(text="Emprty field")
                        else:
                            if(len(edate)!= 5):
                                ErrorEdate.config(text="")
                                ErrorEdate.config(text="Incorrect value")
                            else:
                                if search( "-", edate):
                                    keyEdate = True
                                else:
                                    ErrorEdate.config(text="")
                                    ErrorEdate.config(text="Date should have -")
                                
                        #Validar csv
                        if(csv == ""):
                            ErrorCSV.config(text="")
                            ErrorCSV.config(text="Emprty field")
                        else:
                            if(len(csv)!= 3):
                                ErrorCSV.config(text="")
                                ErrorCSV.config(text="Incorrect value")
                            else:
                                keycvs = True
                        #Si todo está bien, pasa al siguiente apartado
                        if(keyPhone == True and keyPlan == True and keyCnumber == True and keyEdate == True and keycvs == True):
                            client.telephone = phone
                            client.plan = plan
                            client.cardnumber = cnumber
                            client.expdate = edate
                            client.cod = csv
                            #Lanzar la sig interfaz
                            add_3()
                            #administrator.addclient(client.name, client.lastname, client.mail, client.password, client.cedula,
                             #               client.telephone, client.plan, client.cardnumber, client.expdate, client.cod)
                            #Admin()
                        
                   

                    phone = txtphone.get()
                    plan = txtPlan.get()
                    cnumber = txtCnumber.get()
                    edate = txtEdate.get()
                    csv = txtCSV.get()
                    validate()
                

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
                txtCnumber = Entry(app, bg="grey89",validate="key",
                                 validatecommand=(app.register(validate_cc), "%S"))
                txtCnumber.place(x=245, y=339, width=275, height=55)
                txtEdate = Entry(app, bg="grey89")
                txtEdate.place(x=557, y=339, width=275, height=55)
                txtCSV = Entry(app, bg="grey89", validate="key", validatecommand=(
                    app.register(validate_cc), "%S"), show="*")
                txtCSV.place(x=245, y=448, width=275, height=55)
                # Boton next2
                
                btnNext2 = Button(image=btnnext, command=next2)
                btnNext2.place(x=630, y=448, height=41, width=105)
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
                #Botones laterales
                botonMod = Button(image=btnModi, command=modificarCliente)
                botonMod.place(x=23, y=267, height=53, width=168)
                botonMod.configure(borderwidth=0)
                botonDelete = Button(image=btnDele, command=eliminarCliente)
                botonDelete.place(x=22, y=355, height=53, width=176)
                botonDelete.configure(borderwidth=0)
                botonBack1 = Button(text="Back", image=botonBack, command=agregarClient)
                botonBack1.place(x=46, y=450, height=41, width=105)
                botonBack1.configure( borderwidth=0)
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
            botonMod = Button(image=btnModi, command=modificarCliente)
            botonMod.place(x=23, y=267, height=53, width=168)
            botonMod.configure(borderwidth=0)
            botonDelete = Button(image=btnDele, command=eliminarCliente)
            botonDelete.place(x=22, y=355, height=53, width=176)
            botonDelete.configure(borderwidth=0)
            botonBack1 = Button(text="Back", image=botonBack, command=Admin)
            botonBack1.place(x=46, y=450, height=41, width=105)
            botonBack1.configure( borderwidth=0)
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
            btnNext.place(x=630, y=448, height=41, width=105)
            btnNext.configure(borderwidth=0)
            
        def eliminarCliente():
            def validate_delete():
                #Falta validad
                key1 = False
                key2 = False
                txt1 =txtCC.get()
                txt2 = txtcontraseña.get()
                #Validar cedula
                if(txt1 == ""): #Campos vacios
                    ErrorCC.config(text="")
                    ErrorCC.config(text="Emprty field")
                else:#Buscar en la base
                    cursor = conexion.cursor()
                    cursor.execute(
                        "SELECT mail FROM Clientes WHERE cedula='"+txt1+"'")
                    cedula = cursor.fetchone()
                    if(cedula == None): #None = no existe
                        ErrorCC.config(text="")
                        ErrorCC.config(text="Cedula doesn't exist")
                    else:
                        key1 = True
                if(key1 == True):#Si hay cedula que busque la contraseña
                    if(txt2 == ""):
                        ErrorPP.config(text="")
                        ErrorPP.config(text="Empty field")
                    else: #Buscar en la db
                        cursor = conexion.cursor()
                        cursor.execute(
                            "SELECT mail FROM Clientes WHERE password='"+txt2+"'AND cedula='"+txt1+"'")
                        pword = cursor.fetchone()
                        if(pword == None): #No es su contraseña
                            ErrorPP.config(text="")
                            ErrorPP.config(text="Incorrect password")
                        else: #Si todo fue correcto ya lo elimina
                            administrator.removeclient(txt1) 
                            Admin()   
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            background2 = Label(interfaz, image=imagen2_31)
            background2.pack()
            
            #Campos de texto
            #cedula
            def validate_cc(text: str):
                return text.isdecimal()
            txtCC = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"))
            txtCC.place(x=241, y=244, width=275, height=55)
            #Contraseña
            txtcontraseña = Entry(app, bg="grey89", show="*")
            txtcontraseña.place(x=241, y=379, width=275, height=55)
            #Boton eliminar
            
            #Botón para avanzar
            btnok = Button(image=btndeleteok, command=validate_delete) #Comando de la clase admin
            btnok.place(x=700, y=448, height=51, width=136)
            btnok.configure(borderwidth=0)
            #Botón para regresar
            botonBack1 = Button(text="Back", image=botonBack, command=Admin)
            botonBack1.place(x=46, y=450, height=41, width=105)
            botonBack1.configure( borderwidth=0)
            #botones del panel lateral
            botonAdd = Button(image=botonAdd1, command=agregarClient)
            botonAdd.place(x=20, y=191, height=54, width=181)
            botonAdd.configure(borderwidth=0)
            botonMod = Button(image=btnModi, command=modificarCliente)
            botonMod.place(x=23, y=267, height=53, width=168)
            botonMod.configure(borderwidth=0)
            #Label de error
            ErrorCC = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorCC.place(x=241, y=300)
            ErrorPP = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorPP.place(x=241, y=436)
        def modificarCliente():
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            background2 = Label(interfaz, image=imagen2_22)
            background2.pack()
            #Boton back
            botonBack1 = Button(text="Back", image=botonBack, command=Admin)
            botonBack1.place(x=46, y=450, height=41, width=105)
            botonBack1.configure(borderwidth=0)
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        background2 = Label(interfaz, image=imagen2)
        background2.pack()
        botonBack1 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack1.place(x=46, y=450, height=41, width=105)
        botonBack1.configure(borderwidth=0)
        botonAdd = Button(image=botonAdd1, command=agregarClient)
        botonAdd.place(x=20, y=191, height=54, width=181)
        botonAdd.configure(borderwidth=0)
        botonMod = Button(image=btnModi, command=modificarCliente)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        botonDelete = Button(image=btnDele, command=eliminarCliente)
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
        botonBack2.place(x=813, y=420, height=41, width=105)
        botonBack2.config(borderwidth=0)

    # Comando boton Login
    def login():
        # Validar cliente
        def validarClient(c1: Str, c2: Str):
            def instanciar ():
                #Nombre
                cursor.execute("SELECT name FROM Clientes WHERE mail='"+c1+"'")
                client.name = cursor.fetchone()
                #Apellido
                cursor.execute("SELECT lasName FROM Clientes WHERE mail='"+c1+"'")
                client.lastname = cursor.fetchone()
                #Plan
                cursor.execute("SELECT plan FROM Clientes WHERE mail='"+c1+"'")
                client.plan = cursor.fetchone()
                #telefono
                cursor.execute("SELECT telephone FROM Clientes WHERE mail='"+c1+"'")
                client.telephone = cursor.fetchone()
                #Placa
                cursor.execute("SELECT licensePlate FROM Clientes WHERE mail='"+c1+"'")
                client.licenseplate = cursor.fetchone()
                #numero VIn
                cursor.execute("SELECT numVIN FROM Clientes WHERE mail='"+c1+"'")
                client.numVIN = cursor.fetchone()
                #Fecha/modelo
                cursor.execute("SELECT dateB FROM Clientes WHERE mail='"+c1+"'")
                client.dateB = cursor.fetchone()
                #Color
                cursor.execute("SELECT color FROM Clientes WHERE mail='"+c1+"'")
                client.color = cursor.fetchone()
                #Marca
                cursor.execute("SELECT brand FROM Clientes WHERE mail='"+c1+"'")
                client.brand = cursor.fetchone()
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
                    #Instanciar obj cliente
                    instanciar()
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
    boton.place(x=813, y=420, height=41, width=105)

    boton.configure( borderwidth=0)

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
