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
    def _init_(self, name:str, lastname:str, telephone:int, salary:float):
        pass
    def addclient():
        pass
    def removeclient(): 
        pass
    def modclient():
        pass
    def modnum():
        pass
class user(admin, clientdata):
    def _init_(self, userid:int, mail:str, password:str, status:str, registerdate:str):
        pass
    def verifylogin():
        pass
    pass