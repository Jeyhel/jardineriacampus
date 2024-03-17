import json
import requests
import os
from tabulate import tabulate

def postEmpleado():
    empleado = {
            "codigo_empleado": int(input("Ingrese el codigo de empleado: ")),
            "nombre": input("Ingrese el nombre de empleado: "),
            "apellido1": input("Ingrese el primer apellido del empleado: "),
            "apellido2": input("Ingrese el segundo apellido del empleado: "),
            "extension": input("Ingrese la extension del empleado: "),
            "email": input("Ingrese el email del empleado: "),
            "codigo_oficina": input("Ingrese el codigo de oficina del empleado: "),
            "codigo_jefe": int(input("Ingrese el codigo del jefe del empleado: ")),
            "puesto": input("Ingrese el puesto asignado al empleado: "),
        }
    peticion = requests.post("http://172.16.103.33:5526", data = json.dumps(empleado, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res]

    def menu():
      while True:
       os.system("clear")
       print(""" 

       A D M I N I S T R A R 
       D A T O S   D E    L O S 
       E M P L E A D O S

       1. Guardar un nuevo empleado
       0. Salir
""")
opcion= int(input("\nSeleccione una de las opciones: "))
if(opcion == 1):
     print(tabulate(postEmpleado(), headers="keys", tablefmt="github"))
     input("Presione Enter para continuar... ")

elif(opcion==0):
    break
else:
    print("Elija una opcion correcta: ")

