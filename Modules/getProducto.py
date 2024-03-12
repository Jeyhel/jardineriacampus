# # import os
# from tabulate import tabulate 

import Storage.producto as pr
#gama ornametales

def getAllStocksPriceGama(gama, stock): 
    condiciones = []
    for val in pr.producto:
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
            print("""  
    ____                        __                   __        __                                   __           __            
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ____  _________  ____/ /_  _______/ /_____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / __ \/ ___/ __ \/ __  / / / / ___/ __/ __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /_/ / /  / /_/ / /_/ / /_/ / /__/ /_/ /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/  / .___/_/   \____/\__,_/\__,_/\___/\__/\____/____/  
          /_/                                                             /_/                                                  
          1.Obtener todos los productos de una categoria ordenando sus precios de venta, tambien que su cantidad de inventario sea superior (ejemplo: Ornamentales)
          0.Regresar al menu principal 
          
        """)
            opcion = int(input("\nSleccione una de las opciones"))
            if(opcion == 1):
                gama = input("Ingrese la gama que deseas filtrar")
                stock   = int(input("Ingrese  las unidades que deseas mostrar"))
                print(tabulate)
        
            
        
        
    






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