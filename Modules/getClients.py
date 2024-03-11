import  Storage.cliente as cli
from tabulate import tabulate

def getAllClientsName():
    clienteName = list()
    for val in cli.cliente:
        codigoName = dict({
              "codigo_cliente": val.get('codigo_cliente'),
              "codigo_cliente": val.get('nombre_cliente')
         })
        clienteName.append(codigoName)  
    return clienteName 

def getOneClienteCodigo(codigo):
    for val in cli.cliente:
        if(val.get('codigo_cliente') == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'), 
                "nombre_cliente": val.get('nombre_cliente')
             } 
             
  
def getAllClientPaisRegionCiudad(pais,region=None, ciudad=None): 
    clientZone = list()
    for val in cli.cliente:
        if(val.get('pais') == pais):
            
            if((region != None or val.get('region') == region)):
                clientZone.append(val) 
            elif((region != None and val.get('region') == region)): 
                clientZone.append(val)     
    return clientZone



#punto 6
def getNombreClientesEspañoles():
    getNombreClientesEspañoles = []
    for val in cli.clientes:
        if val.get('pais') == "Spain":
            getNombreClientesEspañoles.append(
                {
                    "nombre_cliente": val.get("nombre_cliente")
                }
            )  
    return getNombreClientesEspañoles






def menu():
    while True: 
        print("""  
    ____                        __                   __        __                   ___            __           
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   _____/ (_)__  ____  / /____  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / ___/ / / _ \/ __ \/ __/ _ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  / /__/ / /  __/ / / / /_/  __(__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/_/\___/_/ /_/\__/\___/____/  
         
         1. Obtener nombres de los clientes 
         2. Obtener codigo del cliente
         3. Obtener region. pais y ciudad del cliente
         4. obenter clientes españoles
         5. Salir
""")
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(getAllClientsName(), headers="keys", tablefmt="github"))
        elif(opcion == 2):
            print(tabulate(getOneClienteCodigo(), headers="keys", tablefmt="github"))
        elif(opcion == 3):
            print(tabulate(getAllClientPaisRegionCiudad(), headers="keys", tablefmt="github"))
        elif(opcion == 4):
            print(tabulate( getNombreClientesEspañoles(), headers="keys", tablefmt="github"))
        elif(opcion == 5):
            break
        else:
            print("elija una opcion valida")
            
     
        
        

