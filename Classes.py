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
    def _init_(self, licenseplate:str, numVIN:str, dateB:str, color:str, brand:str, origin:str):
        pass

class clientdata(client_car):
    def __init__(self, cedula:int, name:str, lastname:str, plan:int, telephone:int, paydate:str, cardnumber:str, expdate:str, cod:int):
        pass
        def carmod():
            pass
        def modcard():
            pass
        def modnum():
            pass

class admin:
    #Ingreso de los atributos de la base de datos
    def __init__(self, cc:str, name: str, lastname:str, mail:str, password:str):
        self.cc = cc
        self.name = name
        self.lastname = lastname
        self.mail = mail
        self.password = password
        
    def addclient():
        pass
    def removeclient(): 
        pass
    def modclient():
        pass
class user(admin, clientdata):
    def _init_(self, userid:int, mail:str, password:str, status:str, registerdate:str):
        pass
    def verifylogin():
        pass
    pass
