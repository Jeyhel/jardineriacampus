# import os 
from tabulate import tabulate
import Modules.getClients as cliente 
import Modules.getOficina as oficina 
import Modules.getEmpleado as empleado  
import Modules.getPedido as pedidos
import Modules.getPago as pago 
import sys

 


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


#menu()   
#print(dir())
#print(sys.modules)

#for nombre, objeto in sys.modules.items():
    #if nombre.startswith("modules"):
        #modulo = getattr(objeto, "__name__", None)
        #if ((modulo != "modules")):
            #file = modulo.split(".")[-1]  # Cambio "get" por "."
            #print(file)
            
if(__name__ == "__main__"):
    while True:
      print("""
    __  ___                    ____       _            _             __
   /  |/  /__  ____  __  __   / __ \_____(_)___  _____(_)___  ____ _/ /
  / /|_/ / _ \/ __ \/ / / /  / /_/ / ___/ / __ \/ ___/ / __ \/ __ `/ / 
 / /  / /  __/ / / / /_/ /  / ____/ /  / / / / / /__/ / /_/ / /_/ / /  
/_/  /_/\___/_/ /_/\__,_/  /_/   /_/  /_/_/ /_/\___/_/ .___/\__,_/_/   
                                                    /_/                
            1.Clients
            2.Oficina
            3.Empleado
            4.Pedidos
            5.Pago
            6.Salir
""")
      # print("Presiona [ctrl + C] Para salir del programa ")
       
#     try:
#     opcion = int(input("seleccione una de las opciones: "))
#         except KeyboardInterrupt:
#             os.system("clear")
#             print("Has salido exitosamente!")
#             break
#     else:
#         if (opcion == 1):
#             print(tabulate(getAllStocksPriceGama))
      
      
      opcion = int(input("\nSeleccione una de las opciones: "))
      if(opcion == 1):
        cliente.menu
      elif(opcion == 2):    
        oficina.menu()     
      elif(opcion == 3):  
        empleado.menu()
      elif(opcion == 4): 
        pedidos.menu()
      elif(opcion == 5): 
        pago.menu()
      elif(opcion == 6): 
        break
