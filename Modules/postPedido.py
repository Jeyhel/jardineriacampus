import json 
import requests 
import os 
from tabulate import tabulate

def postPedido():
    pedido = {
        "codigoPedido": int(input("Ingrese el codigo del pedido: ")),
        "fecha_pedido": input("Ingrese la fecha del pedido: "),
        "fecha_esperada": input("Ingrese la fecha esperada del pedido: "),
        "fecha_entrega": input("Ingrese la fecha de entrega del pedido: "),
        "estado": input("Ingrese el estado del pedido: "),
        "comentario": input("Ingrese los comentarios acerca del pedido: "),
        "codigo_cliente": int(input("Ingrese el codigo del cliente: "))
    }
    peticion = requests.post("http://172.16.103.33:5530", data = json.dumps(pedido, indent =4).encode("UTF-8"))
    res=peticion.json()
    res["mensaje"] = "Producto Guardado"
    return [res] 

def menu():
  while True:
    os.system("clear")
    print(""" 

    A D M I N I S T R A R 
    D A T O S   D E   L O S 
    P E D I D O S
    
    1.Guardar un nuevos pedido
    0.Salir
""")

    opcion= int(input("\nSeleccione una de las opciones: "))
    if(opcion == 1):
        print(tabulate(postPedido(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")


