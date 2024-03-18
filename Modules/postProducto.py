import os 
from tabulate import tabulate 
import json 
import requests 
import Modules.getGamas as gG
import Modules.getProducto as gP


def postProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://172.16.103.33:5531"(id)")
        if(peticion.status == 204):
            data.append({"menssage": "producto eliminado correctamente"})
            return {
                "body":data, 
                "status": peticion.status_code,
            }
        else:
            return {
                "body": [{
                    "mensaje": "producto no enocntrado",
                    "id": id
                }],
                "status": 400,
            }



def postProducto():
    producto = {
            "codigo_producto": input("Ingrese el codigo del producto: "),
            "nombre": input("Ingrese el nombre del nombre: "),
            "gama":gG.getAllNombre()[int(input("Selecione la gama:\n"+"".join([f"\t{i}. {val}\n" for i, val in enumerate(gG.getAllNombre())])))],
            "dimensiones": input("Ingrese a gama del prodcuto: "),
            "proveedor": input("Ingrese el proveedor del producto: "),
            "descripcion": input("Ingrese la descripcion del producto: "),
            "cantidad_en_stock" : int(input("Ingrese la cantidad en stock: ")),
            "precio_venta": int(input("Ingrese el precio de ventas: ")),
            "precio_proveedor": int(input("Ingrese el precio del proveedor: "))
    }
    peticion = requests.post("http://172.16.103.33:5531", data=json.dumps(producto))
    res = peticion.json()
    res["Mensaje"] = "Producto Guardado"  
    return [res]

def menu():
    while True:
        os.system ("clear")
        print("""   
              
              A D M I N I S T R A R
              D A T O S   D E 
              P R O D U C T O S 
              

              1. Guardar un producto nuevo 
              2. Eliminar un producto
              0. Atras
              
           """)
        opcion = int(input("\nSeleccion una de las opciones: "))
        if(re.match(r'[0-9]+$', opcion)is not None):
            opcion = int(opcion)
        if(opcion>=0 and opcion<= 2):
            if(opcion == 1):
                print(tabulate(postProducto(), headers="keys", tablefmt="github"))
            elif(opcion == 2):
                idProducto = input("Ingrese rl id del producto que desea eliminar: ")
                print(tabulate(deleteProducto(idProducto)["body"], headers="keys", tablefmt="github")))        elif(opcion == 0):
            break

        input("Precione una tecla para continuar...")


    