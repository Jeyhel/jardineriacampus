from tabulate import tabulate
import os
import Modules.getClients as cliente 
import Modules.getOficina as oficina 
import Modules.getEmpleado as empleado  
import Modules.getPedido as pedidos
import Modules.getPago as pago 
#import Modules.getGamas as gama

#import sys



 


#punto 1
#print(tabulate(oficina.getCodigoOfiCiudadName(), tablefmt="grid"))

#punto 2
#print(tabulate(oficina.getCiudadTelefonoEspaña(), tablefmt="grid"))

#punto 3
#print(tabulate(empleado.getNombreApellidoJefe(), tablefmt="grid"))

#punto 4
#print(tabulate(empleado.getAllNombreApellidoEmailJefe(), tablefmt="grid"))

#punto 5
#print(tabulate(empleado.getAllNombreApellidoPuesto(), tablefmt= "grid"))

#punto 6
#print(tabulate(cliente.getNombreClientesEspañoles(), tablefmt="grid"))

#punto 7
#print(tabulate(pedidos.getEstadoPedidos(), tablefmt="grid"))

#punto 8
#print((pago.getFechaPago()))

#punto 9
# #print(tabulate(pedidos.getAllPedidosEntregadosAtrasadosDeTiempo(), tablefmt= "grid"))

#punto 10
# print(tabulate(pedidos.getAllPedidosClienteFechaEsperadaFechaDeEntrega(), tablefmt= "grid"))

#punto 11
# print(tabulate(pedidos.getAllPedidosRechazados(), tablefmt= "grid")) 

#punto 12
#print(tabulate(pedidos.getAllPedidosDeEnero(), tablefmt= "grid"))

#punto 13
#print(pago.getAllPagoFecha())

#punto 14 
#print(pago.getAllFormaDePago())

#punto 16 
#print(tabulate(cliente.getAllClienteCiudadDeMadrid(), tablefmt= "grid"))

#menu()   
#print(dir()) 
#print(sys.modules)

#for nombre, objeto in sys.modules.items():
    #if nombre.startswith("modules"):
        #modulo = getattr(objeto, "__name__", None)
        #if ((modulo != "modules")):
#             #file = modulo.split(".")[-1]  # Cambio "get" por "."
#             #print(file)

import Modules.getClients as RepClients
import Modules.postClients as CRUDClients

import Modules.getEmpleado as RepEmpleado
import Modules.postEmpleado as CRUDEmplado

import Modules.getOficina as RepOficina
import Modules.postOficina as CRUDOficina

import Modules.getPago as RepPago
import Modules.postPago as CRUDPago

import Modules.getPedido as RepPedido
import Modules.getPedido as CRUDPedido

import Modules.getProducto as Repproducto
import Modules.postProducto as CRUDproducto


def menuClientes():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   A L 
              M E N U    D E 
              C L I E N T S
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            RepClients.menu()
        if(opcion == 2):
            CRUDClients.menu()
        elif(opcion == 0):
            break



def menuEmpleado():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   A L 
              M E N U    D E 
              E M P L E A D O  
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            RepEmpleado.menu()
        if(opcion == 2):
            CRUDEmplado.menu()
        elif(opcion == 0):
            break


def menuOficina():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   AL 
              M E N U    D E 
              O F I C I N A 
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            RepOficina.menu()
        if(opcion == 2):
            CRUDOficina.menu()
        elif(opcion == 0):
            break



def menuPago():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   AL 
              M E N U    D E 
              P A G O 
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            RepPago.menu()
        if(opcion == 2):
            CRUDPago.menu()
        elif(opcion == 0):
            break



def menuPedido():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   AL 
              M E N U    D E 
              P E D I D O 
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
             RepPedido.menu()
        if(opcion == 2):
            CRUDPedido.menu()
        elif(opcion == 0):
            break



def menuProducto():
    while True: 
        os.system ("clear")
        print(""" 
              
              B I E N V E N I D O   A L 
              M E N U   D E 
              P R O D U C T O S
              
                                   
               1. Reportes de los productos
               2. Guardar, actualicar y eliminar productos
               0. Regresar al menu principal 
               
             """)
        opcion = int(input("\nSeleccione una de las opciones: "))
        if(opcion == 1):
            Repproducto.menu()
        if(opcion == 2):
            CRUDproducto.menu()
        elif(opcion == 0):
            break

if(__name__ == "__main__"):
        while True:
            os.system("clear")
            print("""
             

                M E N U 
                P R I N I C I P A L 
                
                1.Clients 
                2.Oficina
                3.Empleado
                4.Pedidos
                5.Pago
                6.Productos
                7.Salir
""")
            opcion = int(input("\nSeleccione una de las opciones: "))
            if(opcion == 1):
                menuClientes()
            elif(opcion == 2):    
                menuOficina()     
            elif(opcion == 3):  
                menuEmpleado()
            elif(opcion == 4): 
                menuPedido()
            elif(opcion == 5): 
                menuPago()
            elif(opcion == 6): 
                menuProducto()
            elif(opcion == 7):
                break


      # print("Presiona [ctrl + C] Para salir del programa ")
       
    # try:
    #     opcion = int(input("seleccione una de las opciones: "))
    # except KeyboardInterrupt:
    #         os.system("clear")
    #         print("Has salido exitosamente!")
    #         break
    # else:
    #     if (opcion == 1):
    #         print(tabulate(getAllStocksPriceGama))
      
