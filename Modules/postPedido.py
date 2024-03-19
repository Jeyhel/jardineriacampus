import json 
import requests 
import os 
from tabulate import tabulate
import Modules.getPedido as getPed
import re
def guardarPedido():
    
    pedido = dict ()
    while True:
        try:
            
            
            #CODIGO PEDIDO
            if not pedido.get("codigo_pedido"):
                codigo = input ("ingrese el codigo del producto: ")
                if re.match(r'^[A-Z]{2}-\d{3}$', codigo)is not None:
                    if getPed.getAllCodigoPedido(codigo):
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
                codigo_cliente=input("ingrese el codigo del cliente")
                if re.match(r'^[0-9]+$',codigo)is not None:
                    codigo_cliente = int(codigo_cliente)
                    AAA =getPed.getAllcodigoCliente(codigo)
                    if AAA:
                        pedido["codigo_producto"] = codigo
                        break
                    else:
                        raise Exception ("el codigo del cliente no esta registrado") 
                else:
                    raise Exception ("el codigo del cliente no esta registrado")                  
            
        except Exception as error:
            print(error)
            
    peticion = requests.post("http://154.38.171.54:5007/pedidos", data=json.dumps(pedido, indent=4).encode("UTF-8"))
    res = peticion.json()
    res["Mensaje"] = "Pedido Guardado exitosamente"
    return [res]



def DeletePedido(id):
    data = getPed.getPedidoCodigoasd(id)
    if len(data):
        peticion = requests.delete("http://154.38.171.54:5007/pedidos/{id}")
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
        


    peticion = requests.post("http://154.38.171.54:5007/pedidos", data = json.dumps(pedido, indent =4).encode("UTF-8"))
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
        print(tabulate(guardarPedido(), headers="keys", tablefmt="github"))
        input("Presione Enter para continuar... ")

    elif(opcion==0):
       break
    else:
       print("Elija una opcion correcta: ")


