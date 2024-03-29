import json
import requests
import Modules.getPedido as getPed
from tabulate import tabulate
import os
import time


def updatePedidoFechas(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido que desea actualizar la fecha del pedido?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_pedido"] = input("ingrese la nueva fecha del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
        

def updatePedidoFechaEsperadas(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido en el que desea actualizar la fecha esperada del pedido?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_esperada"] = input("Ingrese la nueva fecha esperada del pedido")
                    
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoFechaEntregadas(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido que desea actualizar la fecha de entrega?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["fecha_entrega"] = input("ingrese la nueva fecha de entrega del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")



def updatePedidoEstado(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido que desea actualizar el estado del pedido?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["estado"] = input("ingrese el nuevo estado del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoComentario(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido que desea actualizar el comentario?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["comentario"] = input("ingrese el nuevo comentario del pedido: ")
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")


def updatePedidoCodigoCliente(codigo):
    while True:
        if(codigo != None):
            pedido= getPed.getPedidoCodigos((codigo))
            if (pedido):
                print(tabulate(pedido, headers="keys", tablefmt="github"))
                opc=int(input("""
                    ¿Este es el pedido que desea actualizar el codigo de cliente?
                            1. Si
                            2. No
                """))
                if(opc):
                    headers = {'Content-type': 'application/json', 'charset': 'UTF-8'}
                    pedido[0]["codigo_cliente"] = int(input("ingrese el nuevo codigo del cliente del pedido: "))
                    peticion = requests.put(f'http://154.38.171.54:5007/pedidos/{pedido[0].get("id")}', headers= headers, data= json.dumps(pedido[0]))
                    data = peticion.json()
                    return [data]

                else:
                    codigo = None
            else:
                print(f"el pedido {codigo} no existe")
                codigo = None      
        else:
            codigo = input("ingrese el codigo del pedido")
            
def menu():
  while True:
    os.system("clear")
    print("""
          
          E D I T A R
          I N F O R M A C I O N 
          D E    L O S  
          P E D I D O S 
          
                                 1. Fecha del pedido
                                 2. Fecha esperada
                                 3. Fecha de entrega
                                 4. Estado del pedido
                                 5. Comentario del pedido
                                 6. Codigo del cliente
                                 0. Salir


""")
    
    opcion= int(input("\nSeleccione el dato que quiera editar: "))
    codigopedido = input(("Ingrese el codigo del pedido al que deseas actualizar los datos: "))
    if (opcion == 1):
        print(tabulate(updatePedidoFechas(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==2):
        print(tabulate(updatePedidoFechaEsperadas(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==3):
        print(tabulate(updatePedidoFechaEntregadas(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==4):
        print(tabulate(updatePedidoEstado(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==5):
        print(tabulate(updatePedidoComentario(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==6):
        print(tabulate(updatePedidoCodigoCliente(codigopedido), headers="keys", tablefmt="github"))
    elif (opcion ==0):
        break 