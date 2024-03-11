import Storage.pago as pag

#punto 8
def getFechaPago():
    clientesPago= set()
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPago.add(val.get("codigo_cliente"))

    return clientesPago


#punto 13
def getAllPagoFecha():
    pagoFecha = []
    for val in pag.pago:
        if("2008") in val.get("fecha_pago") and val.get("forma_pago") == ("PayPal"):
            pagoFecha.append({
                    "codigo_de_cliente": val.get("codigo_cliente"),
                    "fecha_pago": val.get("fecha_pago"),
                    "forma_pago": val.get("forma_pago"),
                    "total": val.get("total")
                })
    pagoFecha = sorted(pagoFecha, key=lambda x: x ["total"], reverse=True)

    return pagoFecha


         
#punto 14
def getAllFormaDePago():
    Paypal = set ()
    for val in pag.pago:
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal 



def menu():
     while True: 
         print("""   
     ___                        __                   __                              
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     ____  ____ _____ _____ 
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / __ \/ __ `/ __ `/ __ \
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / /_/ / /_/ / /_/ / /_/ /
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  / .___/\__,_/\__, /\____/ 
          /_/                                             /_/          /____/       
          
          1. Obtener fecha y pago 2008
          2. Obtener pago y fecha 2008 mediante Paypal
          3. Obtener forma de pago en la tabla pago
          4. Salir
""")
         opcion = int(input("\nSeleccione una de las opciones: "))
         if(opcion ==1):
            print(getFechaPago(), )
         elif(opcion == 2):
            print(getAllPagoFecha(), )
         elif(opcion == 3):
            print(getAllFormaDePago(), )
         elif(opcion == 4):
            break
         else:
            print("elija una opcion valida") 
