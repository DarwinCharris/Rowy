import mysql.connector
from mysql.connector import Error



class plan:
    def ver():
        pass

    def pay():
        pass

    def vehicleTax():
        pass

    def soat():
        pass

    def tecnomaintence():
        pass


class plan1(plan):
    def complainmentRequest():
        pass

    def Maintence():
        pass


class plan2(plan):
    def Maintence():
        pass


class plan3(plan):
    pass


class client_car(plan):
    def _init_(self, licenseplate: str, numVIN: str, dateB: str, color: str, brand: str, origin: str):
        self.licenseplate = licenseplate
        self.numVIN =numVIN
        self.dateB = dateB
        self.color = color
        self.brand = brand
        self.origin = origin
        


class clientdata(client_car):
    def __init__(self, cedula: str, name: str, lastname: str, plan: str, telephone: str, paydate: str, cardnumber: str, expdate: str, cod: str, mail: str, password: str):
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
    

        def carmod():
            pass

        def modcard():
            pass

        def modnum():
            pass


class admin:
    # Ingreso de los atributos de la base de datos
    def __init__(self, cc: str, name: str, lastname: str, mail: str, password: str):
        self.cc = cc
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password

    def addclient(salf, name: str, lastname: str, email: str, password: str, cedula: str, telephone: str, plan: str, cardnumber: str, expdate: str, csv: str):
        try:
            conexion = mysql.connector.connect(
            host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
    )
        except Error as ex:
            print("Error de conexión", ex)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Clientes (cedula,name,lasName, mail,password,plan,telephone,payDate,cardNumber,expDate,cod,licensePlate,NumVIN,dateB,color,brand,origin) VALUES ('" + cedula +
                       "','"+name+"','"+lastname+"','"+email+"','"+password+"','"+plan+"','"+telephone+"','10','"+cardnumber+"','"+expdate+"','"+csv+"','ab4-32','34325A','10-10','red','mazda','colombia')")
        conexion.commit()
        print("Cliente agregado")
        if conexion.is_connected():
            conexion.close()
            

    def removeclient(self, cc:str):
        try:
            conexion = mysql.connector.connect(
            host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
    )
        
        except Error as ex:
            print("Error de conexión", ex)
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Clientes WHERE cedula='"+cc+"'")
        conexion.commit()
        print("reg eliminado")
        if conexion.is_connected():
            conexion.close()
    def modclient():
        pass


class user(admin, clientdata):
    def _init_(self, userid: int, mail: str, password: str, status: str, registerdate: str):
        pass

    def verifylogin():
        pass
    pass
