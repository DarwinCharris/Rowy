from tkinter import * 
 
monto = "1000000"
identificacion = "hola"
myTuple = ("UPDATE Clientes SET dateB = '", monto, "' WHERE cedula = '", identificacion,"'")
comando = "".join(myTuple)
print(comando)