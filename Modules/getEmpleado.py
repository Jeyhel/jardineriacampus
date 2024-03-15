from tabulate import tabulate 

#punto 3 
def getNombreApellidoJefe():
    NombreApellidoJefe = []
    for val in em.empleado:
        if val.get('codigo_jefe') == 7 :
            NombreApellidoJefe.append(
                {
                    "nombre": val.get("nombre"),
                    "apellidos": f'{val.get("apellido1")} {val.get("apellido2")}',
                    "email": val.get("email")
                }
            )
    return NombreApellidoJefe


#punto 4
def getAllNombreApellidoEmailJefe():
    nombreApellidoEmail = []
    for val in em.empleado:
         if val.get('codigo_jefe') == None:
             nombreApellidoEmail.append(
                {
                    "nombre":val.get("nombre"),
                    "apellidos":(f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "email": val.get("email"),
                    "nombre_puesto": val.get("jefe")
                      }  )  
    return   nombreApellidoEmail


#punto 5
def getAllNombreApellidoPuesto():
    nombreApellidoPuesto = []   
    for val in em.empleado:
        if(val.get('puesto') != "Representante Ventas"): 
             nombreApellidoPuesto.append(
                 {
                    "nombre":val.get("nombre"),
                    "apellidos":(f"{val.get('apellido1')} {val.get('apellido2')}"),
                    "nombre_puesto":val.get("puesto")
                     
                 } )
    return nombreApellidoPuesto 

def menu():
     while True: 
         print("""  

             REPORTES 
             DE LOS 
             EMPLEADOS 
             
          1.Obtener nombre y apellido del Jefe
          2.Obtener nombre, apellido y email del Jefe
          3.Obtener nombre, apellido y puesto 
          4.Salir                       
""")
         opcion = int(input("\nSeleccione una de las opciones: "))
         if(opcion == 1):
            print(tabulate(getNombreApellidoJefe(), headers="keys", tablefmt="github"))
         elif(opcion == 2):
            print(tabulate(getAllNombreApellidoEmailJefe(), headers="keys", tablefmt="github"))
         elif(opcion == 3):
            print(tabulate(getAllNombreApellidoPuesto(), headers="keys", tablefmt="github"))
         elif(opcion == 4):
            break
         else:
            print("elija una opcion valida")
