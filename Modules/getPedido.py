from tabulate import tabulate
from datetime import datetime, timedelta
import requests

def getAllPedido():
    peticion = requests.get(" http://154.38.171.54:5007/pedidos")
    data = peticion.json
    return data 



#punto 9
def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado":
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days < 0:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado

    
    

#date_1 = '2006-01-17'
#date_2 = '2006-01-17'
#date_1= "/".join(date_1.split("-")[::-1])
#date_1= "/".join(date_1.split("-")[::-1])
#print(lista)

#date_1 = '2024-03-07'
#date_2 = '2024-03-09'

#start = datetime.strptime(date_1, "%d/%m/%Y")
#start = datetime.strptime(date_2, "%d/%m/%Y")

#diff =  end.date ()- start.date 
#print (diff.days)

#import Storage.pedido as pe
from datetime import datetime 

#punto 10
def getAllPedidosClienteFechaEsperadaFechaDeEntrega():
    pedidosEntregado = []
    for val in getAllPedido():
        if val.get("estado") == "Entregado" and val.get("fecha_entrega") is None:
            val["fecha_entrega"] = val.get("fecha_esperada")
        if val.get("estado") == "Entregado": 
            date_1 = "/".join(val.get("fecha_entrega").split("-")[::-1])
            date_2 = "/".join(val.get("fecha_esperada").split("-")[::-1])
            start = datetime.strptime(date_1, "%d/%m/%Y")
            end = datetime.strptime(date_2, "%d/%m/%Y")
            diff = end.date() - start.date()
            if diff.days == 2:
                pedidosEntregado.append({
                    "codigo_de_pedido": val.get("codigo_pedido"),
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_esperada": val.get("fecha_esperada"),
                    "fecha_de_entrega": val.get("fecha_entrega"),
                })
    return pedidosEntregado
            
            
            
            
            
#import Storage.pedido as pe
from datetime import datetime 

#punto 11
def getAllPedidosRechazados():
    pedidosRechazados = []
    for val in getAllPedido():
        fechaRechazo = val.get("fecha_esperada")
        if val.get("estado") == "Rechazado" and fechaRechazo.startswith("2009"): 
           pedidosRechazados.append(val)
    return pedidosRechazados


#punto 7 
def getEstadoPedidos():
    estadosPedidos = set()
    for val in getAllPedido():
       estado_pedido = val.get('estado')
       estadosPedidos.add(estado_pedido)
    return estadosPedidos


#punto 12
def getAllPedidosDeEnero():
    PedidosDeEnero = list()
    for val in getAllPedido():
        if (val.get("estado") == "Entregado" and val.get("fecha_entrega") != None):
            FechaEntregada = "/".join(val.get("fecha_entrega").split("-")[::-1])
            start = datetime.strptime(FechaEntregada, "%d/%m/%Y")
            if val.get("estado") == "Entregado" and start.month == 1:
                PedidosDeEnero.append(val)
    return PedidosDeEnero

def menu():
     while True: 
         print("""   
             
             REPORTES 
             DE LOS 
             PEDIDOS 
          
          1. Pedidos entragados atrazados 
          2. 2 dias antes de la fecha esperada
          3. Estados por los que puede pasar el pedido
          4. Estado del pedido
          5. Pedidos del mes de enero 
          6. Salir
""")
         opcion = int(input("\nSeleccione una de las opciones: "))
         if(opcion ==1):
            print(tabulate(getAllPedidosEntregadosAtrasadosDeTiempo(), headers="keys", tablefmt="github"))
         elif(opcion == 2):
            print(tabulate(getAllPedidosClienteFechaEsperadaFechaDeEntrega(), headers="keys", tablefmt="github"))
         elif(opcion == 3):
            print(tabulate(getAllPedidosRechazados(), headers="keys", tablefmt="github"))
         elif(opcion == 4):
            print(tabulate(getEstadoPedidos(), headers="keys", tablefmt="github"))
         elif(opcion == 5):
            print(tabulate(getAllPedidosDeEnero(), headers="keys", tablefmt="github"))
         elif(opcion == 6):
            break
         else:
             print("elija una opcion valida") 



         