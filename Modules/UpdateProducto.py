import json
import requests
import Modules.getProducto as getPro
from tabulate import tabulate
import os
import time


def updateProductoNombreee(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar el nombre?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["nombre"] = input("Ingrese el cambio para el nombre del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")
        

def updateProductoGamaa(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto en el que desea actualizar la gama?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["gama"] = input(f"""
                                                  Estas son las gamas ya establecidas:
                                                  
                                                  -Herbaceas
                                                  -Herramientas
                                                  -Aromáticas
                                                  -Frutales
                                                  -Ornamentales
                                                  -Herramientas
                                                  
                                                  Escriba la gama que desee, existente o inexistente: """)
                    
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")


def updateProductoDimensioness(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar las dimensiones??
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["dimensiones"] = input("ingrese las nuevas dimensiones del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")



def updateProductoProveedorr(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar el nombre del proveedor?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["proveedor"] = input("ingrese el nuevo nombre del proveedor: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")


def updateProductoDeDescripcion(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar la descripcion?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["descripcion"] = input("ingrese la nueva descripcion del producto: ")
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")


def updateProductoStockk(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar la cantidad en stock?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["cantidad_en_stock"] = int(input("ingrese la nueva cantidad en stock del producto: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")


def updateProductoPrecioVentaa(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar el precio de venta?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["precio_venta"] = int(input("ingrese la nueva cantidad del precio de venta: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")


def updateProductoPrecioProveedorr(codigo):
    while True:
        if(codigo != None):
            producto= getPro.getProductoCodigos((codigo))
            if (producto):
                print(tabulate(producto, headers="keys", tablefmt="github"))
                jml=int(input("""
                    ¿Este es el producto que desea actualizar la cantidad del precio de proveedor?
                            1. Si
                            2. No
                """))
                if(jml):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    producto[0]["precio_proveedor"] = int(input("ingrese la nueva cantidad del precio de proveedor: "))
                    peticion = requests.put(f'http://154.38.171.54:5008/productos/{producto[0].get("id")}', headers= headers, data= json.dumps(producto[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el producto {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del producto")





def menu():
  while True:
    os.system("clear")
    print("""
          
          E D I T O R 
          I N F O R M A C I O N 
          D E    L O S 
          P R O D U C T O S 
          
             1. Nombre
             2. Gama
             3. Dimensiones
             4. Proveedor
             5. Descripcion
             6. Cantidad en Stock
             7. Precio de venta
             8. Precio de proveedor
             0. Salir

""")
    
    try:
        opcion= int(input("\nSeleccione el dato que quiera editar: "))
        codigoProducto = input(("Ingrese el codigo del producto al que deseas actualizar los datos: "))
        if (opcion == 1):
            print(tabulate(updateProductoNombreee(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==2):
            print(tabulate(updateProductoGamaa(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==3):
            print(tabulate(updateProductoDimensioness(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==4):
            print(tabulate(updateProductoProveedorr(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==5):
            print(tabulate(updateProductoDeDescripcion(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==6):
            print(tabulate(updateProductoStockk(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==7):
            print(tabulate(updateProductoPrecioVentaa(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==8):
            print(tabulate(updateProductoPrecioProveedorr(codigoProducto), headers="keys", tablefmt="github"))
        elif (opcion ==0):
            break    
        else:
                print("Elija algun número disponible del 0 al 8 ")
                time.sleep(3)
    except ValueError: 
         print("Caracteres incorrectos, elija una jmlion del 0 al 8")
         time.sleep(3)