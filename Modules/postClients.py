import json
import requests
import os
from tabulate import tabulate 

def postClients():
    cliente = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "nombre_cliente": input("Ingrese el nombre del cliente: "),
        "nombre_contacto": input("Ingrese el nombre de contacto: "),
        "apellido_contacto": input("Ingrese el apellido de contacto: "),
        "telefono": input("Ingrese el telefono del cliente: "),
        "fax": input("Ingrese el fax cliente: "),
        "linea_direccion1": input("Ingrese la linea de direccion 1: "),
        "linea_direccion2": input("Ingrese la linea de direccion 2: "),
        "ciudad": input("Ingrese la ciudad del cliente: "),
        "region": input("Ingrese la region del cliente: "),
        "pais": input("Ingrese el pais del cliente: "),
        "codigo_postal": input("Ingrese el codigo postal del cliente: "),
        "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas del cliente: ")),
        "limite_credito": int(input("Ingrese el limite de credito del cliente: "))
        }
    peticion = requests.post("http://172.16.103.33:5525", data = json.dumps(cliente, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return[res]

def menu():
  while True:
    os.system("clear")
    print(""" 
    
    A D M I N I S T R A R 
    D A T O S   D E   L O S 
    C L I E N T E S

    1. Guardar un nuevo cliente 
    0. Salir 
    
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postCliente(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")


     