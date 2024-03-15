from tabulate import tabulate
import requests

def getAllcliente():
    peticion = requests.get
    

# def getAllClientsName():
#     clienteName = list()
#     for val in cli.cliente:
#         codigoName = dict({
#               "codigo_cliente": val.get('codigo_cliente'),
#               "codigo_cliente": val.get('nombre_cliente')
#          })
#         clienteName.append(codigoName)  
#     return clienteName 

# def getOneClienteCodigo(codigo):
#     for val in cli.cliente:
#         if(val.get('codigo_cliente') == codigo):
#             return {
#                 "codigo_cliente": val.get('codigo_cliente'), 
#                 "nombre_cliente": val.get('nombre_cliente')
#              } 
             
  
# def getAllClientePaisRegionCiudad(pais,region=None, ciudad=None): 
#     clientZone = list()
#     for val in cli.cliente:
#         if(val.get('pais') == pais):
            
#             if((region != None or val.get('region') == region)):
#                 clientZone.append(val) 
#             elif((region != None and val.get('region') == region)): 
#                 clientZone.append(val)     
#     return clientZone



#punto 6
def getNombreClientesEspañoles():
    getNombreClientesEspañoles = []
    for val in cli.cliente:
        if val.get('pais') == "Spain":
            getNombreClientesEspañoles.append(
                {
                    "nombre_cliente": val.get("nombre_cliente")
                }
            )  
    return getNombreClientesEspañoles

# #punto 16
def getAllClienteCiudadDeMadrid():
    ClienteCiudadDeMadrid = []
    for val in cli.cliente:
        if val.get("ciudad") == "Madrid":
            if val.get("codigo_empleado_rep_ventas") in [11, 30]:
                ClienteCiudadDeMadrid.append(
                    {
                        "codigoCliente": val.get("codigo_cliente"),
                        "nombreCliente": val.get("nombre_cliente"),
                        "ciudad": val.get("ciudad"),
                        "representante_de_ventas": val.get("codigo_empleado_rep_ventas")
                    }
                )
    return ClienteCiudadDeMadrid




# def getAllClienteAndRepresentante():
#     ClienteAndRepresentante = []
#     for val in cli.cliente:
#         if val.getf("nombre")
    
    
    
    
    

def menu():
        while True: 
            print(f"""   
                  
                  REPORTES 
                  DE LOS 
                  CLIENTES
                                                                                                              
         1. Obtener clientes españoles
         2. Obtener clientes de la ciudad de Madrid 
         3. Salir
        """)
            opcion = int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                print(tabulate( getNombreClientesEspañoles(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllClienteCiudadDeMadrid(), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                break
            else:
                print("elija una opcion valida")
            
     
        
        

