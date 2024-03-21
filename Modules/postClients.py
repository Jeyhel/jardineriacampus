import json
import requests
import os
from tabulate import tabulate 
import re 
import Modules.getClients as getcli 
import Modules.UpdateClients as upCli
def guardarCliente():

    cliente = dict()
    while True:
        try:
            
            
            #Codigo del cliente
            if not cliente.get("codigo_cliente"):
                codigo = input("ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo) is not None:
                    codigo = int(codigo)
                    if getcli.getClienteCodigos(codigo):
                        raise Exception("el codigo del cliente ya existe")
                    else:
                        cliente["codigo_cliente"] = codigo
                else:
                    raise Exception ("El codigo ingresado no es valido, ingrese solo digitos numericos, por favor. ")
                    
            
             
            #Nomre del cliente
            if not cliente.get("nombre_cliente"):
               nombre_cliente = input(f"Ingrese el nombre del cliente: ")
               if re.match(r'^[A-Z][a-zA-Z0-9\s]*$', nombre_cliente) is not None:
                    cliente["nombre_cliente"] = nombre_cliente
               else:
                    raise Exception("Por favor ingrese de nuevo el nombre, recuerde que la palabra debe iniciar con mayúscula.")
            
            
            #Nombre del contacto
            if not cliente.get("nombre_contacto"):
                nombre_contacto= input("ingrese el nombre del contacto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',nombre_contacto) is not None:
                    cliente["nombre_contacto"]= nombre_contacto
                else:
                    raise Exception("el nombre no es valido,por favor inicie todas las palabras con mayuscula")
             
            
            #Apellido del contacto
            if not cliente.get("apelllido_contacto"):
                apelllido_contacto = input("ingrese el apellido  del contacto: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',apelllido_contacto) is not None:
                    cliente["apelllido_contacto"]= apelllido_contacto
                else:
                    raise Exception("el apellido ingresado no es valido,por favor inicie todas las palabras con mayuscula")
            
               
            
            # Telefono del contacto  
            if not cliente.get("telefono"):
                telefono= input("ingrese el numero de telefono: ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$',telefono) is not None:
                    if getcli.getAllTelefono(telefono):
                         raise Exception("el telefono ingresado ya existe")
                    else:
                        cliente["telefono"] = telefono
                else:
                    raise Exception ("Telefono no valido, ejm: 845210369 o 5 5487-8745 ")
                
            
            #Fax
            if not cliente.get("fax"):
                fax = input("ingrese el fax : ")
                if re.match(r'^\d{1,3} ?\d{4}-?\d{4}$',fax) is not None:
                    cliente["fax"]= fax
                else:
                    raise Exception("el fax ingresado no es valido")
                
            
            #Linea de direccion 1 
            if not cliente.get("linea_direccion1"):
                linea_direccion1 = input("ingrese  la linea_direccion1 : ")
                cliente["linea_direccion1"]= linea_direccion1
              
              
            
            #Linea de direccion 2
            if not cliente.get("linea_direccion2"):
                linea_direccion2 = input("ingrese  la linea_direccion2 : ")
                cliente["linea_direccion2"]= linea_direccion2
                
            
            
            #Ciudad
            if not cliente.get("ciudad"):
                ciudad = input("ingrese la ciudad: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',ciudad) is not None:
                    cliente["ciudad"]= ciudad
                else:
                    raise Exception("la ciudad ingresada no es valida")
                
           
            #Region
            if not cliente.get("region"):
                region= input("ingrese la region: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',region) is not None:
                    cliente["region"]= region
                else:
                    raise Exception("la region ingresada no es valida")
                
            
            #Pais
            if not cliente.get("pais"):
                pais= input("ingrese  el pais: ")
                if re.match(r'^[A-Z][a-zA-Z0-9\s]*$',pais) is not None:
                    cliente["pais"]= pais
                else:
                    raise Exception("el pais ingresado no es valido")
                
            
            #Codigo postal
            if not cliente.get("codigo_postal"):
                codigo_postal = input("Ingrese el Codigo postal: ")
                if re.match(r'^\d{4,5}$', codigo_postal) is not None:
                    cliente["codigo_postal"] = codigo_postal
                else:
                    raise Exception("Codigo postal no valido, asegurese de ingresar 4 o 5 dígitos numéricos")
            
            
            
            #Codigo empleado de ventas
            if not cliente.get("codigo_empleado_rep_ventas"):
                codigo_empleado_rep_ventas = input(f"Escriba el codigo del representante de ventas: ")
                if re.match(r'^[0-9]+$', codigo_empleado_rep_ventas) is not None:
                    codigo_empleado_rep_ventas = int(codigo_empleado_rep_ventas)
                    cliente["codigo_empleado_rep_ventas"] = codigo_empleado_rep_ventas
                else:
                    raise Exception("Codigo ingresado no valido,por favor ingresar solo dígitos numéricos")
            
            
            
             #Limite credito  
            if not cliente.get("limite_credito"):
                limite_credito = input(f"Escriba el limite de credito: ")
                if re.match(r'^[0-9]+$', limite_credito) is not None:
                    limite_credito = float(limite_credito)
                    cliente["limite_credito"] = limite_credito
                    break
                else:
                    raise Exception("Limite de credito  no valido, por favor ingresar solo dígitos numéricos")
                                   
        except Exception as error:
            print(error)



# def postClients():
#     cliente = {
#         "codigo_cliente": int(input("Ingrese el codigo del cliente: ")),
#         "nombre_cliente": input("Ingrese el nombre del cliente: "),
#         "nombre_contacto": input("Ingrese el nombre de contacto: "),
#         "apellido_contacto": input("Ingrese el apellido de contacto: "),
#         "telefono": input("Ingrese el telefono del cliente: "),
#         "fax": input("Ingrese el fax cliente: "),
#         "linea_direccion1": input("Ingrese la linea de direccion 1: "),
#         "linea_direccion2": input("Ingrese la linea de direccion 2: "),
#         "ciudad": input("Ingrese la ciudad del cliente: "),
#         "region": input("Ingrese la region del cliente: "),
#         "pais": input("Ingrese el pais del cliente: "),
#         "codigo_postal": input("Ingrese el codigo postal del cliente: "),
#         "codigo_empleado_rep_ventas": int(input("Ingrese el codigo del representante de ventas del cliente: ")),
#         "limite_credito": int(input("Ingrese el limite de credito del cliente: "))
#         }
    
    
    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5001/cliente",headers=headers, data=json.dumps(cliente, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]

    #peticion = requests.post(" http://154.38.171.54:5001/cliente", data = json.dumps(cliente, indent =4).encode("UTF-8"))
    #res=peticion.json()
    #res["mensaje"] = "Producto Guardado"
    #return[res]

def DeleteClientes(id):
    data = getcli.getClientsId(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5001/cliente/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Cliente eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Cliente no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }


def menu():
  while True:
    os.system("clear")
    print(""" 
    
    A D M I N I S T R A R 
    D A T O S   D E   L O S 
    C L I E N T E S

    1. Guardar un nuevo cliente 
    2. Eliminar un nuevo cliente 
    3. Actualizar un nuevo cliente
    0. Salir 
    
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
       print(tabulate(guardarCliente(),headers="keys",tablefmt="github"))
       input("Presione Enter para continuar... ")

    elif(opcion==2):
        idCliente = input("Ingrese el id del cliente que desea eliminar: ")
        print(tabulate(DeleteClientes(idCliente),headers="keys",tablefmt="github"))
    
    elif opcion==3:
            upCli.menu()
        

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")


     