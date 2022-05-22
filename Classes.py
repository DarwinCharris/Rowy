from datetime import date
import mysql.connector
from mysql.connector import Error


class Plan1():
    def complainmentRequest():
        pass


class Plan2():
    def Maintence(self, dinero:str, cedula:str):
        # Conectar a la base de datos
        try:
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )
        except Error as ex:
            print("Error de conexión", ex)
        # Cursor para ejecutar comando
        cursor = conexion.cursor()
        # Modificar el dinero del cliente en la base de datos
        cursor.execute("UPDATE Clientes SET dateB ='" +
                       dinero+"' WHERE cedula='"+cedula+"'")
        # Enviar el resultado a la base de datos
        conexion.commit()
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()


class Plan3():
    pass


class Plan(Plan1, Plan2, Plan3):
    # Init
    def __init__(self) -> None:
        super().__init__()

    # Hacer el pago de los impeustos básicos, soat, tecnomecanica, impuesto vehicular

    def pay(self, monto: str, identificacion: str):
        # Conectar a la base de datos
        try:
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )
        except Error as ex:
            print("Error de conexión", ex)
        # Cursor para ejecutar comando
        cursor = conexion.cursor()
        # Modificar el dinero del cliente en la base de datos
        cursor.execute("UPDATE Clientes SET dateB ='" +
                       monto+"' WHERE cedula='"+identificacion+"'")
        # Enviar el resultado a la base de datos
        conexion.commit()
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()

    def addmoney(self, dinero: str, cedula: str):
        # Conectar a la base de datos
        try:
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )
        except Error as ex:
            print("Error de conexión", ex)
        # Cursor para ejecutar comando
        cursor = conexion.cursor()
        # Modificar el dinero del cliente en la base de datos
        cursor.execute("UPDATE Clientes SET dateB ='" +
                       dinero+"' WHERE cedula='"+cedula+"'")
        # Enviar el resultado a la base de datos
        conexion.commit()
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()


class Client_car(Plan):  # Colocar que hereda de plan
    # Init de los datos del carro
    def __init__(self, licenseplate: str, numVIN: str, dateB: str, color: str, brand: str, origin: str) -> None:
        self.licenseplate = licenseplate
        self.numVIN = numVIN
        self.dateB = dateB
        self.color = color
        self.brand = brand
        self.origin = origin


class Clientdata(Client_car):
    # Init
    def __init__(self, cedula: str, name: str, lastname: str, plan: str, telephone: str, paydate: str, cardnumber: str, expdate: str, cod: str, mail: str, password: str, licenseplate: str, numVIN: str, dateB: str, color: str, brand: str, origin: str) -> None:
        self.cedula = cedula
        self.name = name
        self.lastname = lastname
        self.plan = plan
        self.telephone = telephone
        self.paydate = paydate
        self.cardnumber = cardnumber
        self.expdate = expdate
        self.cod = cod
        self.mail = mail
        self.password = password
        # Heredar el init de client_car
        # agregar los atributos de clientcar  al init de clientdata y meterlos como parametro de este intit y hacer lo de sef....
        super().__init__(licenseplate, numVIN, dateB, color, brand, origin)

    def carmod():
        pass

    def modcard():
        pass

    def modnum():
        pass


class Admin():
    # Ingreso de los atributos de la base de datos
    # Init para recibir los valores
    def __init__(self, cc: str, name: str, lastname: str, mail: str, password: str):
        self.cc = cc
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
    # Metodo agregar cliente

    def addclient(salf, name: str, lastname: str, email: str, password: str, cedula: str, telephone: str, plan: str,
                  cardnumber: str, expdate: str, csv: str, licenseplate: str,
                  numVIN: str, dateB: str, color: str, brand: str):
        try:  # Conectar a la Base de datos
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )
        except Error as ex:
            print("Error de conexión", ex)
        # Cursor para ejecutar un comando
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Clientes (cedula,name,lasName, mail,password,plan,telephone,payDate,cardNumber,expDate,cod,licensePlate,NumVIN,dateB,color,brand,origin) VALUES ('" + cedula +
                       "','"+name+"','"+lastname+"','"+email+"','"+password+"','"+plan+"','"+telephone+"','10','"+cardnumber+"','"+expdate+"','"+csv+"','" + licenseplate+"','"+numVIN+"','"+dateB+"','"+color+"','"+brand+"','colombia')")
        # Enviar el comando a la base de datos
        conexion.commit()
        print("Cliente agregado")
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()
    # Eliminar cliente

    def removeclient(self, cc: str):
        # Conectar a la base de datos
        try:
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )

        except Error as ex:
            print("Error de conexión", ex)
        # Cuersor para ejecutar comando
        cursor = conexion.cursor()
        # Comando para elimianr cliente
        cursor.execute("DELETE FROM Clientes WHERE cedula='"+cc+"'")
        # Enviar el resultado a la base de datos
        conexion.commit()
        print("reg eliminado")
        # Cerrar la base de datos
        if conexion.is_connected():
            conexion.close()

    def modclient():
        pass
