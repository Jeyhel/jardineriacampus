import json 
import os 
from tabulate import tabulate 
import requests 
import Modules.getGamas as gG


def postProducto(producto):
    producto = { 
        "codigo_producto": input("Ingrese el codigo del producto: "),
        "nombre": input("Ingrese el nombre del nombre: "),
        "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
        "dimensiones": input("Ingrese a gama del prodcuto: "),
        "proveedor": input("Ingrese el proveedor del producto: "),
        "descripcion": input("Ingrese la descripcion del producto: "),
        "cantidad_en_stock" : int(input("Ingrese la cantidad en stock: ")),
        "precio_venta": int(input("Ingrese el precio de ventas: ")),
        "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
        
    peticion = requests.post("http://172.16.100.144:5869", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"  
    return [res]

def menu():
    while True:
        os.system ("clear")
        print("""   
              
              
              
    ___       __          _       _      __                         __      __                    __                             __           __            
   /   | ____/ /___ ___  (_)___  (_)____/ /__________ ______   ____/ /___ _/ /_____  _____   ____/ /__     ____  _________  ____/ /_  _______/ /_____  _____
  / /| |/ __  / __ `__ \/ / __ \/ / ___/ __/ ___/ __ `/ ___/  / __  / __ `/ __/ __ \/ ___/  / __  / _ \   / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / ___ / /_/ / / / / / / / / / / (__  ) /_/ /  / /_/ / /     / /_/ / /_/ / /_/ /_/ (__  )  / /_/ /  __/  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/  |_\__,_/_/ /_/ /_/_/_/ /_/_/____/\__/_/   \__,_/_/      \__,_/\__,_/\__/\____/____/   \__,_/\___/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
                                                                                                       /_/                                                  
              1. Guardar un producto nuevo 
              0. Atras
              
           """)
        opcion = int(input("\nSeleccion una de las opciones: "))
        if(opcion == 1):
            print(tabulate(postProducto??(), headers="keys", tablefmt="github"))
            input("Precione una ecla para continuar...")
        elif(opcion == 0):
            break


    