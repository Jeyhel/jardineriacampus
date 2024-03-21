import json 
import requests 
import os 
from tabulate import tabulate
import Modules.getPedido as getPed
import Modules.getClients as getCli
import re

def guardarPedido():
    pedido = dict()
    while True:
        try:
            
            
            #CODIGO PEDIDO
            if not pedido.get("codigo_pedido"):
                codigo = input ("ingrese el codigo del producto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo)is not None:
                    if getPed.getCodigoPedido(codigo):
                        raise Exception ("el codigo ingresado ya existe")
                    
                    else: pedido["codigo_producto"] = codigo
                    
            else:
                raise Exception("el codigo no cumple con el estandar establecido")
            
            
            #FECHA PEDIDO
            if not pedido.get("fechas_pedido"):
                fecha_pedido = input("ingrese la fecha del pedidoo")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_pedido)is not None:
                    pedido["fecha_pedidio"] = fecha_pedido
                    
            #FECHA ESPERADA
            if not pedido.get("fechas_esperada"):
                fecha_esperada = input("ingrese la fecha esperada del producto")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_esperada)is not None:
                    pedido["fecha_esperada"] = fecha_esperada
                    
                    
            #FECHA ENTREGA
            if not pedido.get("fechas_entrega"):
                fecha_entrega = input("ingrese la fecha esperada del producto")
                if re.match(r'^\d{4}-\d{2}-\d{2}$',fecha_entrega)is not None:
                    pedido["fecha_entrega"] = fecha_entrega
                    
                    
            #ESTADO
            if not pedido.get("estado"):
                estado=input("ingrese el estado del producto")
                if re.match(r'^[A-Z][a-z]*$',estado) is not None:
                   pedido["estado"] = estado
                   
                   
            #COMENTARIO
            if not pedido.get("comentario"):
                comentario =input("ingrese el cometario del producto")
                if comentario.strip() == "":
                    pedido["comentario"] = comentario
                    
                    
            #CODIGO CLIENTE
            if not pedido.get("codigo_cliente"):
                codigo = input("Ingrese el codigo del cliente: ")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo = int(codigo)
                    tkt = getCli.getOneClienteCodigo(codigo)
                    if tkt:
                        pedido["codigo_cliente"] = codigo
                        break
                    else:
                        raise Exception("El codigo del cliente no esta registrado.")
                else:
                    raise Exception("El codigo del cliente no esta registrado.")                 
            
        except Exception as error:
            print(error)

    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
    peticion = requests.post("http://154.38.171.54:5007/pedidos",headers=headers, data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"
    return [res]



def DeletePedido(id):
    data = getPed. getcodigoPedido(id)
    if len(data):
        peticion = requests.delete(f"http://154.38.171.54:5007/pedidos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Pedido eliminado exitosamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Pedido no encontrado.",
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
    P E D I D O S
    
    1. Guardar un nuevo pedido
    2. Borrar un nuevo pedido
    3. Actualizar un nuevo pedido
    0. Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(guardarPedido(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")
    
    elif(opcion == 2):
        idPedido= input("Ingrese el id del empleado que desea eliminar: ")
        print(tabulate(DeletePedido(idPedido), headers="keys", tablefmt="github"))

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")


