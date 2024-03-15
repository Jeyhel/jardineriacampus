from tabulate import tabulate
from datetime import datetime, timedelta
import requests

def getFechaPago():
    peticion = requests.get("http://172.16.100.144:5869")
    data = peticion.json
    return data 

def getAllPagoFecha():
    estadoPedido = set()
    for val in getAllPagoFecha():
        estadoPedido = val.get ('estado')
        estadoPedido.add(estadoPedido)
    return estadoPedido






#punto 8
def getFechaPago():
    clientesPago= set()
    for val in getAllPagoFecha():
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPago.add(val.get("codigo_cliente"))

    return clientesPago


#punto 13
def getAllPagoFecha():
    pagoFecha = []
    for val in getAllPagoFecha():
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            pagoFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagoFecha = sorted(pagoFecha, key=lambda x: x ["total"], reverse=True)

    return pagoFecha


         
#punto 14
def getAllFormaDePago():
    Paypal = set ()
    for val in pag.pago:
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal 



def menu():
     while True: 
         print("""   
               
               REPORTES 
               DE PAGO 
               
          1. Obtener fecha y pago 2008
          2. Obtener pago y fecha 2008 mediante Paypal
          3. Obtener forma de pago en la tabla pago
          4. Salir
""")
         opcion = int(input("\nSeleccione una de las opciones: "))
         if(opcion ==1):
            print(getFechaPago(), )
         elif(opcion == 2):
            print(getAllPagoFecha(), )
         elif(opcion == 3):
            print(getAllFormaDePago(), )
         elif(opcion == 4):
            break
         else:
            print("elija una opcion valida") 
