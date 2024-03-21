import json
import requests
import os
from tabulate import tabulate
#import Modules.getClients as getCli
import re
import Modules.getPago as getPag
import Modules.UpdatePago as upPa
import Modules.UpdateProducto as upPro

def GuardarPago():
    pago = dict ()
    while True:
        try:
            
            #CODIGO CLIENTE
            
            if not pago.get("codigo_cliente"):
                codigo_cliente = input("ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$', codigo_cliente) is not None:
                    codigo_cliente =int(codigo_cliente)
                    love= getPag.getcodigoPago(codigo_cliente)
                    if love:
                        pago["codigo_cliente"] = codigo_cliente
                    else:
                        raise Exception("Codigo cliente no encontrado.")
                else:
                    raise Exception("Codigo no valido,por favor ingresar solo digitos numericos. ")

            
            
          # FORMA PAGO
            if not pago.get("forma_pago"):
                forma_pago = input("Ingrese el metodo de pago: ")
                if re.match(r'^[A-Z][a-zA-Z0-9-\s]*$', forma_pago) is not None:
                    pago["forma_pago"] = forma_pago
                else:
                    raise Exception("Formas de pago validas:PayPal / Transferencia / Cheque ")
            
           
            # ID TRANSACCION
            
            if not pago.get("id_transaccion"):
                id_transaccion = input("Ingrear el ID de transaccion: ")
                if re.match(r'^[a-zA-Z]{2}-[a-zA-Z]{3}-\d{6}$', id_transaccion) is not None:
                    cluck = getPag.getAllITransaId(id_transaccion)
                    if cluck:
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

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5006/pagos",headers=headers, data=json.dumps(pago, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]


def DeletePago(id):
    data = getPag.getcodigoPago(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5006/pagos/{id}")
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


def menu():
    while True:
        os.system("clear")
        print(""" 

        A D M I N I S T R A R 
        D A T O S   D E    L O S
        P A G O S
        
        1. Guardar un nuevo registro de pago
        2. Borrar un nuevo registro de pago
        3. Actualizar un nuevo registro de pago
        0. Salir 
        
""")
        opcion= int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            print(tabulate(GuardarPago(), headers="keys", tablefmt="github"))
            input("Presione Enter para continuar... ")
            
        elif(opcion == 2):
            idPago= input("Ingrese el id del empleado que desea eliminar: ")
            print(tabulate(DeletePago(idPago), headers="keys", tablefmt="github"))
        
         
        elif opcion==3:
            upPa.menu()
                    
        elif(opcion==0):
            break

        else:
            print("Elija una opcion correcta: ")

           