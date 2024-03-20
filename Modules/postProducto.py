import os 
from tabulate import tabulate 
import json 
import requests 
import Modules.getProducto as getPro
import re

def GuardarProducto():
        

    producto = dict()

    while True:
        try:
            
            #CODIGO
            if not producto.get("codigo_producto"):
             codigo = input("Ingrese el codigo del producto: ")
            if re.match(r'^[A-Z]{2}-\d{3}$', codigo) is not None:
                if getPro.getProductoCodigo(codigo):
                    raise Exception("El codigo ingresado ya existe.")
                else:
                    producto["codigo_producto"] = codigo
            else:
                raise Exception("El codigo no cumple con el estandar establecido ejm: XX-444 ")      
                


            #NOMBRE
            # validacion de cadena solo  letras primera Mayus
            if(not producto.get("nombre")):
                nombre = input("ingrese el nombre del producto")
                if(re.match(r'^[A-Z][a-z]*\s*)+$',nombre)is not None):
                    producto["nombre"] = nombre
                    break
                else:
                    raise Exception("el nombre del producto no cumple con el estandar establecido")
                

            #DIMENSIONES
            # VALIDAR NUMEROS
            if not producto.get("dimensiones"):
                dimensiones = input("ingrese las dimensiones del producto: ")
                if(re.match) (r'^\d+-\d+$', dimensiones) is not None:
                    producto[dimensiones] = dimensiones
                else:
                    raise Exception("Dimensiones no válidas, la forma correcta es ( numero-numero ).")
                    
            # PROVEEDOR
            #VALIDAR LETRAS,SOLO  PRIMERA EN MAYUSCULA
            if not producto.get("proveedor"):
                proveedor = input("ingrese el proveedor del producto: ")
                if(re.match) (r'^[A-Z][a-zA-Z0-9\s.]*$', proveedor) is not None:
                    producto[proveedor] = proveedor
                else:
                    raise Exception("Proveedor no valido, recuerde que la primera palabra debe iniciar con mayúsculas.")
                    
            #DESCRIPCION
            if not producto.get("descripcion"):
                descripcion= input("ingrese la descripcion del producto del producto: ")
                producto[descripcion] = descripcion
                    
            #CANTIDAD EN STOCK

            if not producto.get("cantidad_en_stock"):
                cantidad_en_stock= input("ingrese la cantidad en stock  del producto: ")
                if(re.match) (r'^[0-9]+$', cantidad_en_stock) is not None:
                    cantidad_en_stock = int (cantidad_en_stock)
                    producto[cantidad_en_stock] = cantidad_en_stock
                else:
                    raise Exception("Cantidad no valida, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO VENTA

            if not producto.get("precio_venta"):
                precio_venta= input("ingrese el precio de venta del producto: ")
                if(re.match) (r'^[0-9]+$', precio_venta) is not None:
                    precio_venta = int (precio_venta)
                    producto[precio_venta] = precio_venta
                else:
                    raise Exception("Precio de venta no valido, asegurese de ingresar solo dígitos numéricos.")
                    
            #PRECIO PROVEEDOR

            if not producto.get("precio_proveedor"):
                precio_proveedor= input("ingrese el precio proveedor del producto: ")
                if(re.match) (r'^[0-9]+$', precio_proveedor) is not None:
                    precio_proveedor = int (precio_proveedor)
                    producto[precio_proveedor] = precio_proveedor
                else:
                    raise Exception("Precio de proveedor no valido, asegurese de ingresar solo dígitos numéricos.")
            
        except Exception as error:
            print(error)                        
                


    peticion = requests.post("http://154.38.171.54:5008/productos",data=json.dumps(producto, indent=4).encode("UTF-8"))
    res =peticion.json()
    res["Mensaje"] = "producto guardado exitosamente"
    return [res]





def DeleteProducto(id):
    data = getPro.getProductoCodigooo(id)
    if len(data):
        peticion = requests.delete("http://154.38.171.54:5008/productos/{id}")
        if peticion.status_code == 204:
            data.append({"message":  "Producto eliminado correctamente"})
            return {
                "body": data,
                "status": peticion.status_code,
            }     
    else:
        return {
                "body":[{
                    "Mensaje": "Producto no encontrado.",
                    "id": id,
            }],
            "status": 400,
            }
        


# def deleteProducto(id):
#     data = gP.getProductCodigo(id)
#     if(len(data)):
#         peticion = requests.delete(f"http://154.38.171.54:5008/productos{id}") 
#         if(peticion.status == 204):
#             data.append({"menssage": "producto eliminado correctamente"})
#             return {
#                 "body":data, 
#                 "status": peticion.status_code,
#             }
#         else:
#             return {
#                 "body": [{
#                     "mensaje": "producto no enocntrado",
#                     "id": id
#                 }],
# #                 "status": 400,
#             }


    # if(__name__ == "main"):
    #     with open("storage/producto.json", "r") as f:
    #         fichero = f.read()
    #         data = json.loads(fichero)
    #         for i, val in enumerate(data):
    #             data[i]["id"] = (i+1)
    #         data=json.dumps(data, indent=4).encode("utf-8")
    #         with open("storage/producto.json", "wb+") as f1:
    #             f1.write(data)
    #             f1.close()

    # peticion = requests.post("http://172.16.103.33:5531"), data=json.dumps(producto, indent =4).encode("UTF-8"))
    # res = peticion.json()
    # res["Mensaje"] = "Producto Guardado"  
    # return [res]

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
                print(tabulate(GuardarProducto(), headers="keys", tablefmt="github"))
                input("Precione una tecla para continuar...")

            elif(opcion == 2):
                idProducto = input("Ingrese rl id del producto que desea eliminar: ")
                print(tabulate(DeleteProducto(idProducto)["body"], headers="keys", tablefmt="github"))
        
            elif(opcion == 0):
                break
        


    