
from ast import Str
from cgitb import text
from multiprocessing.spawn import old_main_modules
from queue import Empty
from tkinter import *  # seleccionar lo que necesitamos
from tkinter.font import Font
from msilib.schema import CheckBox, Error
from xml.dom.xmlbuilder import DOMEntityResolver
import mysql.connector
from mysql.connector import Error
from re import search

from setuptools import Command
import Classes as cs
# Conectar a la base de datos
try:
    conexion = mysql.connector.connect(
        host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
    )
except Error as ex:
    print("Error de conexión", ex)
# ventana principal
app = Tk()
app.title("Rowy")
app.geometry("960x540")
app.resizable(height=False, width=False)

# Fondos
imagen = PhotoImage(file="imagenes/1.png")
imagen2 = PhotoImage(file="imagenes/2.png")
imagen3 = PhotoImage(file="imagenes/3.png")
imagen2_1 = PhotoImage(file="imagenes/2_1.png")
btnnext = PhotoImage(file="imagenes/next.png")
imagen2_2 = PhotoImage(file="imagenes/2_2.png")
imagen2_31 = PhotoImage(file = "imagenes/2_31.png")
imagen2_22 = PhotoImage(file="imagenes/2_22.png")
imagen2_3 = PhotoImage(file ="imagenes/2_3.png")
imagen3_addMoney = PhotoImage(file="imagenes/3_pay.png")
imagenmaint = PhotoImage(file="imagenes/mechanic.png")
imagenComplaint = PhotoImage(file="imagenes/complaint.png")
imagen3_Config = PhotoImage(file="imagenes/3_Config.png")
imagen3_Modicar = PhotoImage(file="imagenes/3_modicar.png")
#Botones
botonLogin = PhotoImage(file="imagenes/boton.png")
botonBack = PhotoImage(file="imagenes/back.png")
paybtn = PhotoImage(file="imagenes/pay.png")
btnModi = PhotoImage(file="imagenes/Mod.png")
btnDele = PhotoImage(file="imagenes/Delete.png")
botonAdd1 = PhotoImage(file="imagenes/AddClient.png")
btndeleteok = PhotoImage(file= "imagenes/deleteok.png")
btnaddmoney = PhotoImage(file="imagenes/addmoney.png")
btnrequest = PhotoImage(file="imagenes/request.png")
btnmaintence = PhotoImage(file="imagenes/maintence.png")
btncancel = PhotoImage(file="imagenes/cancel.png")
btnaccept = PhotoImage(file="imagenes/accept.png")
btnconfigure = PhotoImage(file="imagenes/configure.png")
btnCar = PhotoImage(file="imagenes/car.png")
btnPays = PhotoImage(file="imagenes/pays.png")
btnChangeP = PhotoImage(file="imagenes/ChangePw.png")
btnChangeT = PhotoImage(file="imagenes/ChangeTele.png")
btnChangeCar = PhotoImage(file = "imagenes/ChangeCar.png")
btnChange = PhotoImage(file="imagenes/btnChange.png")
# Objeto cliente y admin
administrator = cs.Admin(None, None, None, None, None)
# Objeto cliente
client = cs.Clientdata(None, None, None, None, None,
                       None, None, None, None, None, None, None, None, None, None, None, None)

# Pagína principal
def Mainmenu(): 
    # Conectar a la base de datos
    try:
        conexion = mysql.connector.connect(
            host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
        )
    except Error as ex:
        print("Error de conexión", ex)
    # ventana principal   
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
                    txtLplate = Entry(app, bg="grey89",font=30)
                    txtLplate.place(x=245, y=220, width=275, height=55)
                    txtVinN = Entry(app, bg="grey89",font=30)
                    txtVinN.place(x=557, y=220, width=275, height=55)
                    txtCdate = Entry(app, bg="grey89",font=30)
                    txtCdate.place(x=245, y=339, width=275, height=55)
                    txtColor = Entry(app, bg="grey89",font=30)
                    txtColor.place(x=557, y=339, width=275, height=55)
                    txtBrand = Entry(app, bg="grey89",font=30)
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
                                 validatecommand=(app.register(validate_cc), "%S"),font=30)
                txtphone.place(x=245, y=220, width=275, height=55)
                txtPlan = Entry(app, bg="grey89", validate="key",
                                validatecommand=(app.register(validate_cc), "%S"),font=30)
                txtPlan.place(x=557, y=220, width=275, height=55)
                txtCnumber = Entry(app, bg="grey89",validate="key",
                                 validatecommand=(app.register(validate_cc), "%S"),font=30)
                txtCnumber.place(x=245, y=339, width=275, height=55)
                txtEdate = Entry(app, bg="grey89",font=30)
                txtEdate.place(x=557, y=339, width=275, height=55)
                txtCSV = Entry(app, bg="grey89", validate="key", validatecommand=(
                    app.register(validate_cc), "%S"), show="*",font=30)
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
            txtname = Entry(app, bg="grey89",font=30)
            txtname.place(x=245, y=220, width=275, height=55)
            txtLname = Entry(app, bg="grey89",font=30)
            txtLname.place(x=557, y=220, width=275, height=55)
            txtEmail = Entry(app, bg="grey89",font=30)
            txtEmail.place(x=245, y=339, width=275, height=55)
            txtPword = Entry(app, bg="grey89", show="*",font=30)
            txtPword.place(x=557, y=339, width=275, height=55)

            def validate_cc(text: str):
                return text.isdecimal()
            txtID = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"),font=30)
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
                #Laves para confirmar si los datos son correctos
                key1 = False
                key2 = False
                #Obtener lo escrtio en el campo cedula
                txt1 =txtCC.get()
                #Obtener lo escrito en el campo constraseña
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
            #lanzar la nueva interfaz
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            #Fondo de  pantalla
            background2 = Label(interfaz, image=imagen2_31)
            background2.pack()
            
            #Campos de texto
            #cedula
            #Bloquear caracteres diferentes a los numeros
            def validate_cc(text: str):
                return text.isdecimal()
            txtCC = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"),font=30)
            txtCC.place(x=241, y=244, width=275, height=55)
            #Contraseña
            txtcontraseña = Entry(app, bg="grey89", show="*",font=30)
            txtcontraseña.place(x=241, y=379, width=275, height=55)
            #Boton eliminar
            btnok = Button(image=btndeleteok, command=validate_delete) #Comando de la clase admin
            btnok.place(x=700, y=448, height=41, width=105)
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
            def Change():
                #Obetener los campos de texto
                cedula =txtCedula.get()
                plan =txtPlan.get()
                mail =txtmail.get()
                #labels de error
                ErrorPlan.config(text="")
                ErrorCedula.config(text="")
                ErrorMail.config(text="")
                #Llaves
                keyced = False
                keymail = False
                keyPlan = False
                #Validar la cedula 
                if(cedula == ""):
                    #Campos vacios
                    ErrorCedula.config(text="")
                    ErrorCedula.config(text="Empty field")
                else:
                    #Validar que la cedula exista en la db
                    cursor = conexion.cursor()
                    # Ver si esto funciona pq ced es numero
                    cursor.execute(
                        "SELECT cedula FROM Clientes WHERE cedula='"+cedula+"'")
                    ced = cursor.fetchone()
                    if(ced == None):
                        #No existe el cliente
                        ErrorCedula.config(text="")
                        ErrorCedula.config(text="Is not a client")
                    else:
                        keyced = True
                        
                if(keyced ==True):
                    if(plan !=""):
                        #Si va a  digitar algo en plan hay que validar
                        if(plan == "1" or plan=="2" or plan == "3"):
                            #Ver si es uno de los planes
                            keyPlan=True
                            pass
                        else:
                            ErrorPlan.config(text="")
                            ErrorPlan.config(text="Is not a plan")
                    else:
                        keyPlan = True
                    if(mail != ""):
                        #Si va a cambiar el mail validar
                        if search("@rowy.com", mail):
                            ErrorMail.config(text="")
                            ErrorMail.config(text="Mail not available")
                        # Comprobar si el email está ocupado
                        else:
                            cursor = conexion.cursor()
                            cursor.execute(
                                "SELECT mail FROM Clientes WHERE mail='"+mail+"'")
                            email = cursor.fetchone()
                            if(email != None):
                                ErrorMail.config(text="")
                                ErrorMail.config(text="Mail not available")
                            else:
                                # comprobar si tiene alguno de los dominios validos
                                if(search("@gmail.com", mail) or search("@hotmail.com", mail) or search("@outlook.com", mail) or search("@yahoo.com", mail)):
                                    keymail = True
                                else:
                                    ErrorMail.config(text="")
                                    ErrorMail.config(text="Mail not available")
                    else:
                        keymail=True
                if(keyced == True and keyPlan == True and keymail ==True):
                    administrator.modclient(cedula, plan, mail)   
                    Admin()
            #interfaz modificar cliente
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            #Fondo de pantalla
            background2 = Label(interfaz, image=imagen2_22)
            background2.pack()
            #Boton back
            botonBack1 = Button(text="Back", image=botonBack, command=Admin)
            botonBack1.place(x=46, y=450, height=41, width=105)
            botonBack1.configure(borderwidth=0)
            #Botones laterales
            #Agregar cliente
            botonAdd = Button(image=botonAdd1, command=agregarClient)
            botonAdd.place(x=20, y=191, height=54, width=181)
            botonAdd.configure(borderwidth=0)
            #Eliminar cliente
            botonDelete = Button(image=btnDele, command=eliminarCliente)
            botonDelete.place(x=22, y=355, height=53, width=176)
            botonDelete.configure(borderwidth=0)
            #Campos de texto
            #cedula
            #Bloquear caracteres diferentes a los numeros
            def validate_cc(text: str):
                return text.isdecimal()
            txtPlan = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"),font=30)
            txtPlan.place(x=241, y=246, width=275, height=55)
            txtCedula = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"),font=30)
            txtCedula.place(x=563, y=246, width=275, height=55)
            #Contraseña
            txtmail = Entry(app, bg="grey89",font=30)
            txtmail.place(x=241, y=379, width=275, height=55)
            #Label de error
            ErrorPlan = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorPlan.place(x=241, y=300)
            ErrorCedula = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorCedula.place(x=563, y=300)
            ErrorMail = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorMail.place(x=241, y=436)
            #Boton para hacer cambios
            btnok = Button(image=btnChange, command=Change) #Comando de la clase admin
            btnok.place(x=700, y=448, height=41, width=111)
            btnok.configure(borderwidth=0)
        #Pagina principal de administradores
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        #Fondo de pantalla
        background2 = Label(interfaz, image=imagen2)
        background2.pack()
        #Boton para regresar
        botonBack1 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack1.place(x=46, y=450, height=41, width=105)
        botonBack1.configure(borderwidth=0)
        #Botones laterales
        #Agregar cliente
        botonAdd = Button(image=botonAdd1, command=agregarClient)
        botonAdd.place(x=20, y=191, height=54, width=181)
        botonAdd.configure(borderwidth=0)
        #Modificar cliente
        botonMod = Button(image=btnModi, command=modificarCliente)
        botonMod.place(x=23, y=267, height=53, width=168)
        botonMod.configure(borderwidth=0)
        #Eliminar cliente
        botonDelete = Button(image=btnDele, command=eliminarCliente)
        botonDelete.place(x=22, y=355, height=53, width=176)
        botonDelete.configure(borderwidth=0)
        

    def Client():
        def configure():
            def modPassword():
                ErrorNP.config(text="")
                ErrorCP.config(text="")
                ErrorOP.config(text="")
                new = txtNpassword.get()
                old = txtOldP.get()
                confirm =txtConfirmP.get()
                key1= False
                key2= False
                key3 = False
                #Validar nueva contraseña
                if(new == ""):
                    ErrorNP.config(text="")
                    ErrorNP.config(text="Empty field")
                else:
                    key1 = True
                #Validar confirmar
                if(confirm == ""):
                    ErrorCP.config(text="")
                    ErrorCP.config(text="Empty field")
                else:
                    if(new == confirm):
                        key2 = True
                    else:
                        ErrorCP.config(text="")
                        ErrorCP.config(text="Is not the same Password")
                #Validar contraseña vieja
                if(old == ""):
                    ErrorOP.config(text="")
                    ErrorOP.config(text="Empty field")
                else:
                    #Descomponer la cedula porque el string tiene ('...',)
                    fin = len(client.cedula)-4
                    sub = str(client.cedula)
                    ced = sub[2:fin]
                    cursor =conexion.cursor()
                    #Comando para buscar la contraseña en su cedula
                    cursor.execute("SELECT password FROM Clientes WHERE cedula='"+ced+"'")
                    comprobar = cursor.fetchone()
                    if(search(old, str(comprobar))):
                        key3 =True
                    else:
                        ErrorOP.config(text="")
                        ErrorOP.config(text="Incorrect password")
                #Si todo está bien actualizar la contraseña
                if(key1 == True and key2==True and key3 ==True):
                    client.modPassword(ced, new)
                    Client()
            def modPhone():
                ErrorTel.config(text="")
                tel = txtNtelephone.get()
                if(tel == ""):
                    ErrorTel.config(text="")
                    ErrorTel.config(text="Empty field")
                else:
                    if(len(tel)==10):
                        fin = len(client.cedula)-4
                        sub = str(client.cedula)
                        ced = sub[2:fin]
                        client.modnum(ced, tel)
                    else:
                        ErrorTel.config(text="")
                        ErrorTel.config(text="Incorrect value")
            #Pagina de configuración
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            #Fondo
            backgroundC = Label(interfaz, image=imagen3_Config)
            backgroundC.pack()
            #Botones laterales
            #Boton car
            btncar = Button(app, image=btnCar, borderwidth=0, command=Car)
            btncar.place(x=0, y = 335, height=87, width=222)
            #Boton pay
            btncar = Button(app, image=btnPays, borderwidth=0, command=Client)
            btncar.place(x=0, y = 179, height=56, width=222)
            #Boton de modificar contraseña
            btnCPassword = Button(app, image= btnChangeP, borderwidth=0, command=modPassword)
            btnCPassword.place(x=237, y=465, height=42, width=111)
            #Boton de modificar telefono
            btnCTelephone = Button(app, image=btnChangeT, borderwidth=0, command=modPhone)
            btnCTelephone.place(x=773, y=379, height=41, width=111)
            #Campos de texto
            #nueva contraseña
            txtNpassword = Entry(app, bg="grey89",font=30,show="*")
            txtNpassword.place(x=241, y=223, width=275, height=55)
            #Confirmar contraseña
            txtConfirmP = Entry(app, bg="grey89",font=30,show="*")
            txtConfirmP.place(x=241, y=310, width=275, height=55)
            #Contraseña antigua
            txtOldP = Entry(app, bg="grey89",font=30,show="*")
            txtOldP.place(x=241, y=397, width=275, height=55)
            #Telefono nuevo
            def validate_cc(text: str):
                return text.isdecimal()
            txtNtelephone = Entry(app, bg="grey89",font=30, validate="key",
                        validatecommand=(app.register(validate_cc), "%S"))
            txtNtelephone.place(x=609, y=223, width=275, height=55)
            #Laber Errores
            #Error new password
            ErrorNP = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorNP.place(x=394, y=195)
            #Error Confirm password
            ErrorCP = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorCP.place(x=424, y=283)
            #Error Old Password
            ErrorOP = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorOP.place(x=380, y=369)
            #Error telephone
            ErrorTel = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorTel.place(x=765, y=195)
        def Car():
            def modify():
                #Limpiar Lables 
                ErrorLplate.config(text="")
                ErrorVinN.config(text="")
                ErrorColor.config(text="")
                ErrorBrand.config(text="")
                #Tomar la información
                license = txtLplate.get()
                Vin = txtVinN.get()
                color = txtColor.get()
                brand = txtBrand.get()
                #LLaves
                keylincese = False
                keyVin = False
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
                if(keylincese == True and keyVin == True and keyColor == True 
                                    and keyBrand == True):
                     #Descomponer la cedula porque el string tiene ('...',)
                    fin = len(client.cedula)-4
                    sub = str(client.cedula)
                    ced = sub[2:fin]
                    client.carmod(ced,license, Vin, color, brand)
                    Client()
            #Pagina de modificación del carro
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            #Fondo
            backgroundC = Label(interfaz, image=imagen3_Modicar)
            backgroundC.pack()
            #Botones laterales
            #Boton configuración
            btnconfig = Button(app, image=btnconfigure, borderwidth=0,command=configure)
            btnconfig.place(x=0, y = 235, height=87, width=222)
            #Boton pay
            btncar = Button(app, image=btnPays, borderwidth=0, command=Client)
            btncar.place(x=0, y = 179, height=56, width=222)
            #Campos de text
            txtLplate = Entry(app, bg="grey89",font=30)
            txtLplate.place(x=245, y=220, width=275, height=55)
            txtVinN = Entry(app, bg="grey89",font=30)
            txtVinN.place(x=557, y=220, width=275, height=55)
            txtBrand = Entry(app, bg="grey89",font=30)
            txtBrand.place(x=245, y=339, width=275, height=55)
            txtColor = Entry(app, bg="grey89",font=30)
            txtColor.place(x=557, y=339, width=275, height=55)
            #Label para errores
            ErrorLplate = Label(app, text="", font=20,
                            fg="#E41111", bg="#FAFBFD")
            ErrorLplate.place(x=245, y=276)
            ErrorVinN = Label(app, text="", font=20,
                            fg="#E41111", bg="#FAFBFD")
            ErrorVinN.place(x=557, y=276)
            ErrorBrand = Label(app, text="", font=20,
                                fg="#E41111", bg="#FAFBFD")
            ErrorBrand.place(x=245, y=400)
            ErrorColor = Label(app, text="", font=20,
                            fg="#E41111", bg="#FAFBFD")
            ErrorColor.place(x=557, y=400)
            #Boton de modificar telefono
            btnCTelephone = Button(app, image=btnChangeCar, borderwidth=0, command=modify)
            btnCTelephone.place(x=246, y=433, height=41, width=111)
        def addMoney():
            def payM():
                ErrorCVV.config(text="")
                ErrorDIN.config(text="")
                Key1 = False
                Key2 = False
                #Entradas de texto
                monto= txtAmount.get()
                cvv = txtCVV.get()
                #Validar campos vacios
                if(monto == ""):
                    ErrorDIN.config(text="")
                    ErrorDIN.config(text="Empty Field")
                else:
                    Key1= True
                if(cvv == ""):
                    ErrorCVV.config(text="")
                    ErrorCVV.config(text="Empty Field")
                else:
                    Key2 = True
                if(Key1 == True and Key2 == True):
                    #Validar monto 
                    if(len(monto)>20):
                        print ("Error monto")
                        ErrorDIN.config(text="")
                        ErrorDIN.config(text="The informatiojn is too long")
                    else:
                        #Validar el CVV
                        #Descomponer la cedula para quitar los ('...,')
                        fin = len(client.cedula)-4
                        sub = str(client.cedula)
                        client.cedula = sub[2:fin]
                        #Buscar el CVV si la cedula es correcta
                        cursor =conexion.cursor()
                        #Comando para buscar el cvv en su cedula
                        cursor.execute("SELECT cod FROM Clientes WHERE cedula='"+client.cedula+"'")
                        comprobar = cursor.fetchone()
                        #Si el resultado es none significa que no la encontró, es decir no existe
                        if (comprobar == None):
                            ErrorCVV.config(text="")
                            ErrorCVV.config(text="CVV is not correct")
                            #Volver a mandar la cedula como string de la base de datos 
                            cursor.execute("SELECT cedula FROM Clientes WHERE cedula='"+client.cedula+"'")
                            client.cedula = cursor.fetchone()
                        else:
                            if search(cvv, str(comprobar)):
                                #Descomponer el atributo dinero para sumarlo al digitado por el usuario
                                #Hacer un sub string al atributo del dinero porque se encuentra de la forma "('xxxx, ')"
                                fin = len(client.dateB)-4
                                sub = str(client.dateB)
                                sub = sub[2:fin]
                                #Parsear el dinero obtenido
                                dinero = int(sub)
                                #Sumar el dinero que tiene el cliente con lo añadido
                                dinero = dinero + int(monto)
                                #Ejecutar el metodo add money de la clase plan 
                                client.addmoney(str(dinero), client.cedula)
                                #Cambiar el atributo del dinero en cliente
                                cursor =conexion.cursor()
                                cursor.execute("SELECT dateB FROM Clientes WHERE cedula='"+client.cedula+"'")
                                client.dateB = cursor.fetchone()
                                #Volver a mandar la cedula como string de la base de datos 
                                cursor.execute("SELECT cedula FROM Clientes WHERE cedula='"+client.cedula+"'")
                                client.cedula = cursor.fetchone()
                                #Lanzar la página de clientes
                                Client()
                            else:
                                ErrorCVV.config(text="")
                                ErrorCVV.config(text="CVV is not correct")
                                #Volver a mandar la cedula como string de la base de datos 
                                cursor.execute("SELECT cedula FROM Clientes WHERE cedula='"+client.cedula+"'")
                                client.cedula = cursor.fetchone()
            #Lanzar pagina para agregar dinero
            for ele in app.winfo_children():
                ele.destroy()
            interfaz = Canvas(app)
            interfaz.pack()
            #Fondo
            background2_2 = Label(interfaz, image=imagen3_addMoney)
            background2_2.pack()
            #Cantidad de dinero
            #Bloquear caracteres diferentes a los numeros
            def validate_cc(text: str):
                return text.isdecimal()
            txtAmount = Entry(app, bg="grey89", validate="key",
                        validatecommand=(app.register(validate_cc), "%S"),font=30)
            txtAmount.place(x=241, y=244, width=275, height=55)
            #CVV
            txtCVV = Entry(app, bg="grey89", show="*",validate="key",
                        validatecommand=(app.register(validate_cc), "%S"), font=30)
            txtCVV.place(x=241, y=379, width=275, height=55)
            #Boton de aceptar
            btnok = Button(image=btnaddmoney, command=payM)
            btnok.place(x=700, y=448, height=41, width=105)
            btnok.configure(borderwidth=0)
            #Label para error de CVV
            ErrorCVV = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorCVV.place(x=241, y=436)
            #Label para error en en el dienero 
            ErrorDIN = Label(app, text="", font=20, fg="#E41111", bg="#FAFBFD")
            ErrorDIN.place(x=241, y=300)
            #Botones laterales
            #Boton configuración
            btnconfig = Button(app, image=btnconfigure, borderwidth=0,command=configure)
            btnconfig.place(x=0, y = 235, height=87, width=222)
            #Boton car
            btncar = Button(app, image=btnCar, borderwidth=0, command=Car)
            btncar.place(x=0, y = 335, height=87, width=222)
            #Boton pay
            btncar = Button(app, image=btnPays, borderwidth=0, command=Client)
            btncar.place(x=0, y = 179, height=56, width=222)
        #metodo cuando se utiliza el boton pagar
        def pay():
            def paga(dinero:int):
                #acumular el dinero de los checkbutton
                #Soat
                sot = 0
                #Tecnomecanica
                tec= 0
                #Impuesto vehicular
                tx = 0
                #Hacer las sumatorias
                if(varSoat.get() == 1):
                    sot = 1000000
                if(varTech.get()==1):
                    tec = 220000
                if(varTax.get()==1):
                    tx = 500000
                sum = sot+tec+tx
                #Comprobar si el dinero es suficiente para pagar
                if(sum>dinero):
                    infor.config(text="")
                    infor.config(text="There is not enough money", fg="#E41111")
                else:
                    #Le quitamos al dinero lo que se sumó
                    dinero = dinero-sum
                    #Pasarlo al atribtuto del cliente
                    client.dateB = str(dinero)
                    #Hacer un subString de la cedula porque es de la forma "('xxxx, ')"
                    fin = len(client.cedula)-4
                    sub = str(client.cedula)
                    client.cedula = sub[2:fin]
                    #LLamamos al metodo de pagar que es heredado del plan
                    client.pay(client.dateB, client.cedula)
                    #volver a rescatar las varables de cedula y dinero para que vuelvan a tener los parentesis
                    cursor =conexion.cursor()
                    cursor.execute("SELECT dateB FROM Clientes WHERE cedula='"+client.cedula+"'")
                    client.dateB = cursor.fetchone()
                    cursor.execute("SELECT cedula FROM Clientes WHERE cedula='"+client.cedula+"'")
                    client.cedula = cursor.fetchone()
                    #Label que dice que se hizo el pago
                    infor.config(text="")
                    infor.config(text="Successful payment", fg="#000000")
            #Llamar al metodo de pago
            paga(dinero)
        def maint():
            def cerrar():
                maintence.destroy()
            def agendar():
                #Hacer un sub string al atributo del dinero porque se encuentra de la forma "('xxxx, ')"
                fin = len(client.dateB)-4
                sub = str(client.dateB)
                sub = sub[2:fin]
                #Parsear el dinero obtenido
                dinero = int(sub)
                if(dinero<40000):
                    LabelError = Label(maintence, text="THERE IS NOT ENOUGH MONEY",fg="#E41111", bg="#FAFBFD", font=50)
                    LabelError.place(x=67, y=73)
                else:
                    dinero = dinero-40000
                    #Hacer un subString de la cedula porque es de la forma "('xxxx, ')"
                    fin = len(client.cedula)-4
                    sub = str(client.cedula)
                    client.cedula = sub[2:fin]
                    client.Maintence(str(dinero), client.cedula)
                    #Cambiar el atributo del dinero en cliente
                    cursor =conexion.cursor()
                    cursor.execute("SELECT dateB FROM Clientes WHERE cedula='"+client.cedula+"'")
                    client.dateB = cursor.fetchone()
                    #Volver a mandar la cedula como string de la base de datos 
                    cursor.execute("SELECT cedula FROM Clientes WHERE cedula='"+client.cedula+"'")
                    client.cedula = cursor.fetchone()
                    maintence.destroy()
            maintence = Toplevel()
            maintence.title("Rowy/Maintence")
            maintence.geometry("400x200")
            maintence.resizable(height=False, width=False)
            backgroundm = Label(maintence, image=imagenmaint)
            backgroundm.pack()
            botonAccept = Button(maintence, image=btnaccept, command=agendar, borderwidth=0)
            botonAccept.place(x=70, y=162, height=27, width=73)
            botonCancel = Button(maintence, image=btncancel, command=cerrar, borderwidth=0)
            botonCancel.place(x=255, y=162, height=27, width=73)
        def complaint():
            def cerrar():
                complaintpg.destroy()
            complaintpg = Toplevel()
            complaintpg.title("Rowy/Complaint Request")
            complaintpg.geometry("400x200")
            complaintpg.resizable(height=False, width=False)
            backgroundm = Label(complaintpg, image=imagenComplaint)
            backgroundm.pack()
            botonAccept = Button(complaintpg, image=btnaccept, command=cerrar, borderwidth=0)
            botonAccept.place(x=70, y=162, height=27, width=73)
            botonCancel = Button(complaintpg, image=btncancel, command=cerrar, borderwidth=0)
            botonCancel.place(x=255, y=162, height=27, width=73)
        for ele in app.winfo_children():
            ele.destroy()
        interfaz = Canvas(app)
        interfaz.pack()
        #Fondo de pantalla
        background3 = Label(interfaz, image=imagen3)
        background3.pack()
        #Botón para retroceder
        botonBack2 = Button(text="Back", image=botonBack, command=Mainmenu)
        botonBack2.place(x=51, y=450, height=41, width=105)
        botonBack2.config(borderwidth=0)
        
        #Metodo que permite mostrar en un label cuanto es la suma de lo que seleccionón en los checkbuttom
        def a():
            #acumuladores 
            #Soat
            sot = 0
            #Tecnomecanica
            tec= 0
            #Impuesto vehicular
            tx = 0
            #Hacer las sumatorias si se seleccionaron
            if(varSoat.get() == 1):
                sot = 1000000
            if(varTech.get()==1):
                tec = 220000
            if(varTax.get()==1):
                tx = 500000
            #Sumar todo
            sum = sot+tec+tx
            #pars String
            out= str(sum)
            #Mostrar el label con el resultado
            total.config(text="$"+out)
        #Hacer un sub string al atributo del dinero porque se encuentra de la forma "('xxxx, ')"
        fin = len(client.dateB)-4
        sub = str(client.dateB)
        sub = sub[2:fin]
        #Parsear el dinero obtenido
        dinero = int(sub) 
        #Label que mostrará el dinero a pagar dependiendo la selección de los checkbox  
        total = Label(app, text="$0", bg="#D9DFDB", font=30)
        total.place(x= 662, y=192)
        #Variables que conseguiran el valor de los checkbuttom, 1 para seleccionado y 0 para no seleccionado
        #Para el soat
        varSoat = IntVar()
        #Para la tecnomecanica
        varTech = IntVar()
        #Para el impuesto vehicular
        varTax = IntVar()
        #CheckButtom para el soat
        action = Checkbutton(app,text="$1.000.000", variable=varSoat, onvalue=1, offvalue=0, command=a,  bg="#FAFBFD")
        action.place(x=447, y=180)
        #CheckButtom para la tecnomecanica
        tech = Checkbutton(app, text="$220.000",variable=varTech, onvalue=1, offvalue=0, command=a,  bg="#FAFBFD")
        tech.place(x=447, y= 241)
        #CheckButtom para el impuesto vehicular
        tax = Checkbutton(app, text="$500.000", variable=varTax, onvalue=1, offvalue=0, command=a,  bg="#FAFBFD")
        tax.place(x=447, y = 306)
        #Boton para pagar lo que seleccionó con los checkbuttom
        buttonpay = Button(text="Back", image=paybtn ,command=pay)
        buttonpay.place(x=751, y=232, height=30, width=80)
        buttonpay.config(borderwidth=0)
        infor= Label(app, text="", font=40, fg="#E41111", bg="#FAFBFD")
        infor.place(x= 260, y= 148)
        #Boton para agregar dinero
        botonAMoney = Button(image=btnaddmoney, command=addMoney)
        botonAMoney.place(x=258, y=400, height=41, width=105)
        botonAMoney.config(borderwidth=0)
        #Boton Hacer denuncias 
        if search("1", str(client.plan)):
            botonRequest = Button(image=btnrequest, command=complaint)
            botonRequest.place(x=530, y=400, height=41, width=105)
            botonRequest.config(borderwidth=0)
        if(search("1", str(client.plan)) or search("2",str(client.plan))):
            botonMaintence = Button(image=btnmaintence, command=maint)
            botonMaintence.place(x=750, y=400, height=41, width=105)
            botonMaintence.config(borderwidth=0)
        #Botones laterales
        #Boton configuración
        btnconfig = Button(app, image=btnconfigure, borderwidth=0,command=configure)
        btnconfig.place(x=0, y = 235, height=87, width=222)
        #Boton car
        btncar = Button(app, image=btnCar, borderwidth=0, command=Car)
        btncar.place(x=0, y = 335, height=87, width=222)
    # Comando boton Login
    def login():
        # Validar cliente
        def validarClient(c1: Str, c2: Str):
            def instanciar ():
                #Nombre
                cursor.execute("SELECT name FROM Clientes WHERE mail='"+c1+"'")
                client.name = cursor.fetchone()
                #cedula
                cursor.execute("SELECT cedula FROM Clientes WHERE mail='"+c1+"'")
                client.cedula = cursor.fetchone()
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
                #dinero
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
                if(passw != None):
                    #Instanciar obj cliente
                    instanciar()
                    # Lanzar Admin page
                    Client()
                else:
                    #Mandar error que la constrasela es invalidad
                    Error.config(text="")
                    Error.config(text="Invalid password")
            else:
                #Mandar error que el correo es invalido/no existe
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
                    #Conseguir la cedula
                    cursor.execute(
                        "SELECT cedula FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                    cedula = cursor.fetchone()
                    #Conseguir el nombre
                    cursor.execute(
                        "SELECT name FROM Admin WHERE mail='"+c1+"' AND password='"+c2+"'")
                    name = cursor.fetchone()
                    #Conseguir el apellido
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
                    #La constraseña no es validad
                    Error.config(text="")
                    Error.config(text="Invalid password")
            else:
                #El correo es invalido/ no existe
                Error.config(text="")
                Error.config(text="Invalid mail")
        Error.config(text="")
        #Obtener lo que está escrito en los campos de texto
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
    txt1 = Entry(app, bg="grey89",font=30)
    txt1.place(x=514, y=200, width=400, height=54)
    txt2 = Entry(app, bg="grey89", show="*",font=30)
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