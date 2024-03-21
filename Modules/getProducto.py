import os
from tabulate import tabulate 
#import json 
import requests


#import Storage.producto as pr
#gama ornametales
def getAllData():
     peticion = requests.get("http://154.38.171.54:5008/productos")
     data = peticion.json()
     return data
 
def getProductoId(id):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{id}")
    return [peticion.json()] if peticion.ok else []

 
def getProductoCodigo(codigo):
    peticion = requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    return [peticion.json()] if peticion.ok else []


def getAllProveedorr (): 
    Nombre_proveedor =[ ]  
    for val in getProductoCodigo():
       if(val.get("proveedor")=="Murcia Seasons"):
           Nombre_proveedor.append(val)
    return Nombre_proveedor

    

def getAllStockPriceGama(gama, stock):
    condiciones = []
    for val in getProductoCodigo():
        if (val.get("gama") == gama and val.get("cantidad_en_stock")>= stock):
         condiciones.append(val)
    
    def price(val):
        return val.get("precio_venta")
    condiciones.sort(key=price, reverse = True)
    for i,val in enumerate(condiciones):
        if(condiciones[i].get ("descripcion")):
            condiciones[i]["descripcion"]= f'{condiciones[i]["descripcion"][: 5]}...¡'

            condiciones[i] = {
                "codigo": val.get("codigo_producto"),
                "venta" : val.get("precio_venta"),
                "nombre": val.get("nombre"),
                "gama" : val.get("gama"),
                "dimensiones": val.get("dimensiones"),
                "Proveedor" :val.get("proveedor"),
                "descripcion":f'{val.get("descripccion")[:5]}...' if condiciones[i].get ("descripcion") else None ,
                "stock": val.get("cantidad_en_stock"),
                "base":val.get("precio_proveedor"),
              
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
            opcion = int(input("seleccione una de las opciones: "))
        
    
      
            if (opcion == 1):
                    print(tabulate(getAllProveedorr(), headers="keys", tablefmt="github"))
                        
            
            elif (opcion == 2):
                    gama = (input("ingrese la gama que desea filtrar: "))
                    stock =int(input("ingrese las unidades de stock.  "))
                    print(tabulate(getAllStockPriceGama(gama, stock), headers="keys", tablefmt="github"))

            elif (opcion == 0 ):
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