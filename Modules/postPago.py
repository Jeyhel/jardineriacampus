import json
import requests
import os
from tabulate import tabulate
import Modules.getClients as getCli
import Modules.getPago as getPag
import re

def GuardarPago():
    
    pago = dict
    while True:
        try:
            
            #CODIGO CLIENTE
            
            if not pago.get("codigo_cliente"):
                codigo_cliente = input("ingrese el codigo del cliente")
                if re.match(r'^[0-9]+$', codigo_cliente) is not None:
                    codigo_cliente =int(codigo_cliente)
                    adios= getPag.getOneClienteCodigo(codigo_cliente)
                    if adios:
                        pago["codigo_cliente"] = codigo_cliente
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido,por favor ingresar solo sigitos numericos")

            
            # FORMA PAGO
            if not pago.get("forma_pago"):
                forma_pago = input("ingrese la forma de pago")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', forma_pago) is not None:
                    holi =getPag.getAllformapago(forma_pago)
                    if holi:
                        pago["forma_pago"] = forma_pago
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido,por favor ingresar solo sigitos numericos")
            
           
            # ID TRANSACCION
            
            if not pago.get("id_transaccion"):
                id_transaccion = input("Ingrear el ID de transaccion: ")
                if re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id_transaccion) is not None:
                    Nose = getPag.getAllIDTransac(id_transaccion)
                    if Nose:
                        raise Exception("El ID de transaccion ya existe.")
                    else:
                        pago["id_transaccion"] = id_transaccion
                else:
                    raise Exception("ID no valido, porfavor rectificar")
                
            # FECHA PAGO

            if not pago.get("fecha_pago"):
                fecha_pago = input("Ingrese la fecha del pedido: ")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pago)is not None:
                    pago["fecha_pago"] = fecha_pago
                else:
                    raise Exception("Fecha ingresada no valida,por favor utilice el formato (Año/mes-/dia)")


            # PAGO
            
            if not pago.get("total"):
                total = input("Ingrese el total del pago: ")
                if re.match(r'^[0-9]+$', total) is not None:
                    total = int(total)
                    pago["total"] = total
                    break
                else:
                    raise Exception("Total por favor ingresar solo digitos numericos.")

        except Exception as error:
            print(error)


    peticion = requests.get("http://154.38.171.54:5006/pagos",data=json.dumps(GuardarPago, indent=4).encode("UTF-8"))
    res = peticion.json.json()
    res["mensaje"] = "Pago guardado exitosamnete"
    return[res]



def DeletePago(id):
    data = getPag.GETpagocodigo(id)
    if len(data):
        peticion = requests.delete("http://154.38.171.54:5006/pagos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pago eliminado exitosamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Pago no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }




    # peticion = requests.post("http://154.38.171.54:5006/pagos", data = json.dumps(pago, indent =4).encode("UTF-8"))
    # res=peticion.json()
    # res["mensaje"] = "Producto Guardado"
    # return [res]

def menu():
    while True:
        os.system("clear")
        print(""" 

        A D M I N I S T R A R 
        D A T O S   D E    L O S
        P A G O S
        
        1. Guardar un nuevo registro de pago
        0. Salir 
""")
opcion= int(input("\nSeleccione una de las opciones: "))
if(opcion == 1):
    print(tabulate(GuardarPago(), headers="keys", tablefmt="github"))
    input("Presione Enter para continuar... ")

elif(opcion==0):
    breakpoint 
else:
    print("Elija una opcion correcta: ")

           