import mysql.connector
from mysql.connector import Error
try:
    conexion = mysql.connector.connect(
        host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
    )


except Error as ex:
    print("Error de conexión", ex)


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
        pass


class clientdata(client_car):
    def __init__(self, cedula: int, name: str, lastname: str, plan: int, telephone: int, paydate: str, cardnumber: str, expdate: str, cod: int):
        pass

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

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Clientes (cedula,name,lasName, mail,password,plan,telephone,payDate,cardNumber,expDate,cod,licensePlate,NumVIN,dateB,color,brand,origin) VALUES ('" + cedula +
                       "','"+name+"','"+lastname+"','"+email+"','"+password+"','"+plan+"','"+telephone+"','10','"+cardnumber+"','"+expdate+"','"+csv+"','ab4-32','34325A','10-10','red','mazda','colombia')")
        conexion.commit()
        print("listo")

    def removeclient():
        pass

    def modclient():
        pass


class user(admin, clientdata):
    def _init_(self, userid: int, mail: str, password: str, status: str, registerdate: str):
        pass

    def verifylogin():
        pass
    pass
