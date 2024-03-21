from tabulate import tabulate
import requests



def getAlldatacliente():
    peticion = requests.get(" http://154.38.171.54:5001/cliente")
    data = peticion.json()
    return data

def getAllEmpleado():
    peticion = requests.get("http://154.38.171.54:5003/empleados")
    data = peticion.json()
    return data

def getFechaPago():
    peticion = requests.get("http://154.38.171.54:5006/pagos")
    data = peticion.json
    return data 

def getClientsId(id):
    peticion = requests.get(f"http://154.38.171.54:5003/cliente/{id}")
    return [peticion.json()] if peticion.ok else []

def getClientsId(codigo):
    peticion = requests.get(f"http://154.38.171.54:5003/cliente/{codigo}")
    return [peticion.json()] if peticion.ok else []



def getAllClientsName():
    clienteName = list()
    for val in getAlldatacliente():
        codigoName = dict({
              "codigo_cliente": val.get('codigo_cliente'),
              "codigo_cliente": val.get('nombre_cliente')
         })
        clienteName.append(codigoName)  
    return clienteName 



def getOneClienteCodigo(codigo):
    for val in getAlldatacliente():
        if(val.get('codigo_cliente') == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'), 
                "nombre_cliente": val.get('nombre_cliente')
             } 
        
def getAllTelefono(telefono):
    for val in getAlldatacliente():
        if val.get("telefono") == telefono:
            return [val]

             
  
#def getAllClientePaisRegionCiudad(pais,region=None, ciudad=None): 
 #  clientZone = list()
  #for val in getAlldatacliente():
   #     if(val.get('pais') == pais):
  #          
   #         if((region != None or val.get('region') == region)):
  #              clientZone.append(val) 
  #          elif((region != None and val.get('region') == region)): 
  #              clientZone.append(val)     
 #       return clientZone



def getAllClientName():
    clienteName=list()
    for val in getAlldatacliente():
        CodigoName=dict({
        
            "codigo_cliente": val.get('codigo_cliente'),
            "nombre_cliente": val.get('nombre_cliente'),
        })
        clienteName.append(CodigoName)
    return clienteName

#punto 6
def getNombreClientesEspañoles():
    getNombreClientesEspañoles = []
    for val in getAlldatacliente():
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
    for val in getAlldatacliente():
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
         3. Obtener todos los clientes, codigo y nombre
         4. Salir
        """)
            opcion = int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                print(tabulate(getNombreClientesEspañoles(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                print(tabulate(getAllClienteCiudadDeMadrid(), headers="keys", tablefmt="github"))
            elif(opcion == 3):
                print(tabulate(getAllClientName(), headers="keys", tablefmt="github"))
            elif(opcion == 4):
                break
            else:
                print("elija una opcion valida")
            
     
        
        

