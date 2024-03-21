from tabulate import tabulate
from datetime import datetime, timedelta
import requests
import json

def getAllOfi():
    peticion = requests.get("http://154.38.171.54:5005/oficinas")
    data = peticion.json()
    return data 

def getAllOfiId(id):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{id}")
    return [peticion.json()] if peticion.ok else []

def getAllOficina(codigo):
    peticion = requests.get(f"http://154.38.171.54:5005/oficinas/{codigo}")
    return [peticion.json()] if peticion.ok else []




#punto 1
def getCodigoOfiCiudadName():
    CodigoOfCiudad = list()
    for val in  getAllOfi():
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfCiudad.append(codigoNames)
    return CodigoOfCiudad
    
    
#punto 2
def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in getAllOfi():
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
