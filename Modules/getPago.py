from tabulate import tabulate
from datetime import datetime, timedelta
import requests

def getAllPago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json
    return data 

def getPagoId(id):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id}")
    return [peticion.json()] if peticion.ok else []

def getcodigoPago(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo}")
    return [peticion.json()] if peticion.ok else []

def getAllformapago(forma_pago):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{forma_pago}")
    return [peticion.json()] if peticion.ok else []

def getAllITransaId(id_transaccion):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{id_transaccion}")
    return [peticion.json()] if peticion.ok else []


def getProductoCodigos(codigo):
    peticion = requests.get(f"http://154.38.171.54:5006/pagos/{codigo.upper()}")
    data = peticion.json()
    if(data)== 0:
        data=None
    return data


#punto 8
def getFechaPago():
    clientesPago= set()
    for val in getAllPago():
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPago.add(val.get("codigo_cliente"))

    return clientesPago


#punto 13
def getAllPagoFecha():
    pagoFecha = []
    for val in getAllPago():
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
    for val in  getAllPago():
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal 


def getFormasDePago(formas):
    FormasPago = list()
    for val in getAllPago():
        if val.get("forma_pago") == formas: 
            FormasPago.append(val)
    return FormasPago




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
