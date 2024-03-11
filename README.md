#reportes de empleados
opcion = int(input("\nSeleccione una de las opciones: "))

elif(opcion == 3):
      print(tabulate(getEmpleadosPuesto(), headers="keys", tablefmt="github"))
else:
     print("elija una opcion valida")
     

#reporte de oficina
opcion = int(input("\nSeleccione una de las opciones: "))
if(opcion ==1):
    print(tabulate(getOfiCiudadName(), headers="keys", tablefmt="github"))
elif(opcion == 2):
      print(tabulate(getCiudadTelefonoEspannnnnnnnnna(), headers="keys", tablefmt="github"))
else:
     print("elija una opcion valida") 

#reporte pedido
opcion = int(input("\nSeleccione una de las opciones: "))
if(opcion ==1):
    print(tabulate(getAllPedidosEntregadosAtrasados(), headers="keys", tablefmt="github"))
elif(opcion == 2):
      print(tabulate(getAllPedidosRechazados(), headers="keys", tablefmt="github"))
elif(opcion == 3):
      print(tabulate(getEstadoPedidos(), headers="keys", tablefmt="github"))
elif(opcion == 4):
      print(tabulate(getAllPedidosDeEnero(), headers="keys", tablefmt="github"))
else:
     print("elija una opcion valida") 


#reporte pago
opcion = int(input("\nSeleccione una de las opciones: "))
if(opcion ==1):
    print(getFechaPago(), ))
elif(opcion == 2):
      print(getAllPagoFecha(), ))
elif(opcion == 3):
      print(getAllFormaDePago(), ))
else:
     print("elija una opcion valida") 
      

