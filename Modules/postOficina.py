import json
import requests
import os
from tabulate import tabulate

def postOficina():
    oficina = {
        "codigo_oficina": input("Ingrese el codigo de la oficina: "),
        "ciudad": input("Ingrese la ciudad de la oficina: "),
        "pais": input("Ingrese el pais de la oficina: "),
        "region": input("Ingrese la region de la oficina: "),
        "codigo_postal": input("Ingrese el codigo postal de la oficina: "),
        "telefono": input("Ingrese el numero de telefono de la oficina: "),
        "linea_direccion1": input("Ingrese la linea de direccion 1: "),
        "linea_direccion2": input("Ingrese la linea de direccion 2: ")
        }
    
    peticion = requests.post("http://172.16.103.33:5528", data = json.dumps(oficina, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]

def menu():
  while True:
    os.system("clear")
    print(""" 

    A D M I N I S T R A R 
    D A T O S   D E   L A S 
    O F I C I N A S
    
    1. Guardar un nuevo dato de oficina
    0. Salir
    
 """)
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postOficina(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")




