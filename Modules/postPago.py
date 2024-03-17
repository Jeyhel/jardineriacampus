import json
import requests
import os
from tabulate import tabulate 

def postPago():
    pago = {
        "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
        "forma_pago": input("Ingrese la forma de pago: "),
        "id_transaccion": input("Ingrese el id de la transaccion: "),
        "fecha_pago": input("Ingrese la fecha de pago (Año/Mes/dia): "),
        "total": int(input("Ingrese el total: ")),
        }
    peticion = requests.post("http://172.16.103.33:5529", data = json.dumps(pago, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]

def menu():
    while True:
        os.system("clear")
        print(""" 

        A D M I N I S T R A R 
        D A T O S   D E    L O S
        P A G O S
        
        1. Guardar un nuevo registro de pago
        0. Salir 
""")
opcion= int(input("\nSeleccione una de las opciones: "))
if(opcion == 1):
    print(tabulate(postPago(), headers="keys", tablefmt="github"))
    input("Presione Enter para continuar... ")

elif(opcion==0):
    break
else:
    print("Elija una opcion correcta: ")

           