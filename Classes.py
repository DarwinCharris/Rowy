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


class client_car(plan):#Colocar que hereda de plan
    def __init__(self, licenseplate: str, numVIN: str, dateB: str, color: str, brand: str, origin: str)-> None:
        self.licenseplate = licenseplate
        self.numVIN = numVIN
        self.dateB = dateB
        self.color = color
        self.brand = brand
        self.origin = origin
        super().__init__()
    


class clientdata(client_car):
    def __init__(self, cedula: str, name: str, lastname: str, plan: str, telephone: str, paydate: str, cardnumber: str, expdate: str, cod: str, mail: str, password: str, licenseplate: str, numVIN: str, dateB: str, color: str, brand: str, origin: str)-> None:
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
        # agregar los atributos de clientcar  al init de clientdata y meterlos como parametro de este intit y hacer lo de sef....
        super().__init__( licenseplate, numVIN, dateB, color, brand, origin)

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

    def addclient(salf, name: str, lastname: str, email: str, password: str, cedula: str, telephone: str, plan: str, 
                cardnumber: str, expdate: str, csv: str, licenseplate: str,
                     numVIN: str, dateB: str, color: str, brand: str):
        try:
            conexion = mysql.connector.connect(
                host='bpacqw5rvjfk010mockm-mysql.services.clever-cloud.com', user='ufmrybtwgkedeaka', password='q0i5Rasr9nIzRK4HN312', db='bpacqw5rvjfk010mockm'
            )
        except Error as ex:
            print("Error de conexión", ex)
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Clientes (cedula,name,lasName, mail,password,plan,telephone,payDate,cardNumber,expDate,cod,licensePlate,NumVIN,dateB,color,brand,origin) VALUES ('" + cedula +
                       "','"+name+"','"+lastname+"','"+email+"','"+password+"','"+plan+"','"+telephone+"','10','"+cardnumber+"','"+expdate+"','"+csv+"','"+ licenseplate+"','"+numVIN+"','"+dateB+"','"+color+"','"+brand+"','colombia')")
        conexion.commit()
        print("Cliente agregado")
        if conexion.is_connected():
            conexion.close()

    def removeclient(self, cc: str):
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
