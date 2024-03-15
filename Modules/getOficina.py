from tabulate import tabulate
from datetime import datetime, timedelta
import requests

def  getCodigoOfiCiudadName():
    peticion = requests.get("http://172.16.100.144:5869")
    data = peticion.json
    return data 

def getCiudadTelefonoEspaña():
    estadoPedido = set()
    for val in getCiudadTelefonoEspaña():
        estadoPedido = val.get ('estado')
        estadoPedido.add(estadoPedido)
    return estadoPedido




#punto 1
def getCodigoOfiCiudadName():
    CodigoOfCiudad = list()
    for val in of.oficina:
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfCiudad.append(codigoNames)
    return CodigoOfCiudad
    
    
#punto 2
def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in of.oficina:
        if val.get('pais') == "España" :
            ciudadTelefonoEspaña.append(
                {
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono")
                }
            )
    return ciudadTelefonoEspaña

def menu():
    while True: 
        print("""   
              
              REPORTES 
              DE LA 
              OFICINA

          
          1. Codigo de oficina y ciudad donde hay oficinas
          2. Ciudad y telefono de las oficinas de España
          3. Salir 
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getCodigoOfiCiudadName(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            print(tabulate(getCiudadTelefonoEspaña(), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            break
        else:
            print("elija una opcion valida") 
