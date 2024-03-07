import Storage.pedido as pe
from datetime import datetime 


def getAllPedidosEntregadosAtrasadosDeTiempo():
    pedidosEntregado = []
    for val in pe.pedido:
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
