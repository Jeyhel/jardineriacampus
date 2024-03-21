import json
import requests
import os
from tabulate import tabulate
import re 
import Modules.getOficina as getOfi
import Modules.UpdateOficina as upOfi

def guardarOficina():
    oficina = dict()
    while True:
        try:
            
            
            #CODIGO OFICINA
            if not oficina.get("codigo_oficina"):
                codigo_oficina = input(f"Ingrese codigo de la oficina: ")
                if re.match(r'^[A-Z]{3}-[A-Z]{2,3}$', codigo_oficina) is not None:
                    GOGOGO = getOfi.getAllOficina(codigo_oficina)
                    if GOGOGO:
                        raise Exception("Codigo de oficina ya existente.")
                    else:
                        oficina["codigo_oficina"] = codigo_oficina
                else:
                    raise Exception("Codigo no valido")
                
            #CIUDAD
            if not oficina.get("ciudad"):
                ciudad=input("ingrese la ciudad")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', ciudad) is not None:
                    oficina["ciudad"] = ciudad
                else:
                    raise Exception ("la ciudad no es valida ,por favor inicie todas las palabras con mayusculas")
            
            #PAIS
            if not oficina.get("pais"):
                pais=input("ingrese el pais")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', pais) is not None:
                    oficina["pais"] = pais
                else:
                    raise Exception ("sl pais no es valido ,por favor inicie todas las palabras con mayusculas")
            
             
            #REGION
            if not oficina.get("region"):
                region=input("ingrese la region")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', region) is not None:
                    oficina["region"] = region
                else:
                    raise Exception ("la region no es valida ,por favor inicie todas las palabras con mayusculas")
            
            
            # CODIGO POSTAL
            if not oficina.get("codigo_postal"):
                codigo_postal = input("Ingrese el codigo postal: ")
                if re.match(r'^[A-Z0-9\s-]+$', codigo_postal)is not None:
                    oficina["codigo_postal"] = codigo_postal
                else:
                    raise Exception(" El codigo postal no valido.")
                
            #TELEFONO
            if not oficina.get("telefono"):
                telefono = input("Ingrese el telefono: ")
                if re.match(r'^\+\d{1,3}\s\d{1,3}\s\d{4,10}$', telefono)is not None:
                    oficina["telefono"] = telefono
                else:
                    raise Exception("Telefono no valido,por favor rectificar formato : +pais(1-3 digitos) codigo_area(1-3 digitos) telefono(4-10 digitos).")

            if not oficina.get("linea_direccion1"):
                linea_direccion1 = input(f"Ingrese la linea de direccion 1: ")
                oficina["linea_direccion1"] = linea_direccion1

            if not oficina.get("linea_direccion2"):
                linea_direccion2 = input(f"Ingrese la linea de direccion 2: ")
                oficina["linea_direccion2"] = linea_direccion2
                break  
            
            
            
        except Exception as error:
            print(error)
            
            
            
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post(" ",headers=headers, data=json.dumps(oficina, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

def DeleteOficina(id):
    data = getOfi.getAllOfiId(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5005/oficinas/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Oficina eliminada correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Oficina no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
        

def menu():
  while True:
    os.system("clear")
    print(""" 

    A D M I N I S T R A R 
    D A T O S   D E   L A S 
    O F I C I N A S
    
    1. Guardar un nuevo dato de oficina
    2. Eliminar un nuevo dato de oficina 
    3. Actualizar un nuevo dato de oficina
    0. Salir
    
 """)
    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(guardarOficina(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
        
    elif(opcion == 2):
        idOficina = input("Ingrese el id del cliente que desea eliminar: ")
        print(tabulate(DeleteOficina(idOficina),headers="keys",tablefmt="github"))
    
    elif opcion==3:
            upOfi.menu()
            
    elif(opcion==0):
       break
   
    else:
       print("Elija una opcion correcta: ")




