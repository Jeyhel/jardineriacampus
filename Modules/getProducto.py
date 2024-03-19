import os
from tabulate import tabulate 
#import json 
import requests


#import Storage.producto as pr
#gama ornametales
def getAllData():
     peticion = requests.get(" http://154.38.171.54:5008/productos")
     data = peticion.json()
     return data
 
 
def getProductoCodigo(codigo):
    peticion = requests.get("http://154.38.171.54:5008/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []
    

def getAllStocksPriceGama(gama, stock): 
    condiciones = []
    for val in getAllData():
        if(val.get("gama") == gama and val.get("precio_venta") >= stock):  
            condiciones.append(val)
        def price(val):
            return val.get("precio_venta")
        condiciones.sort(key= price)
    for i, val in enumerate(condiciones):
        if(condiciones[i].get("descripcion")):
            condiciones [i]["descripcion"] = f'{val.get("descripcion")[:5]}...'
        condiciones [i] = {
                "Codigo": val.get("codigo_producto"),   
                "Venta": val.get("precio_venta"),
                "Nombre": val.get("Nombre"),
                "Gama": val.get("Gama"),
                "Dimensiones": val.get("Dimensiones"),
                "Proveedor": val.get("Proveedor"),
                "Descripcion": f'{val.get( "Descripcion")[:5]}...' if condiciones[i].get("descripcion") else None, 
                "Stock": val.get("Cantidad_en_stock"),
                "Base": val.get("Precio_proveedor") 
            }
        return condiciones
    
def menu():
        while True:
            os.system("clear")
            print("""  
                  
                  REPORTES 
                  DE LOS 
                  PRODUCTOS
                                                 
          1.Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior (ejemplo: Ornamentales)
          0.Regresar al menu principal 
          
        """)
            opcion = int(input("\nSelecione una de las opciones: "))
            if(opcion == 1):
                gama = input("Ingrese la gama que deseas filtrar: ")
                stock = int(input("Ingrese las unidades que seas mostrar: "))
                print(tabulate(getAllStocksPriceGama(gama, stock ), headers="keys", tablefmt="github"))
            elif(opcion == 0):
                break
                
        
            
        
        
    






# def menu():
    
#     0.Regresar 
#     1. Obtener lista de todos los productos del proveedor
    
  
#     try:
#     opcion = int(input("seleccione una de las opciones: "))
#         except KeyboardInterrupt:
#             os.system("clear")
#             print("Has salido exitosamente!")
#             break
#     else:
#         if (opcion == 1):
#             print(tabulate(getAllStocksPriceGama))