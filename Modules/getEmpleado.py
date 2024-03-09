import  Storage.empleado as em

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



import  Storage.empleado as em

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
    print("""  ____                        __                   __        __                                   __               __          
   / __ \___  ____  ____  _____/ /____  _____   ____/ /__     / /___  _____   ___  ____ ___  ____  / /__  ____ _____/ /___  _____
  / /_/ / _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/  / __  / _ \   / / __ \/ ___/  / _ \/ __ `__ \/ __ \/ / _ \/ __ `/ __  / __ \/ ___/
 / _, _/  __/ /_/ / /_/ / /  / /_/  __(__  )  / /_/ /  __/  / / /_/ (__  )  /  __/ / / / / / /_/ / /  __/ /_/ / /_/ / /_/ (__  ) 
/_/ |_|\___/ .___/\____/_/   \__/\___/____/   \__,_/\___/  /_/\____/____/   \___/_/ /_/ /_/ .___/_/\___/\__,_/\__,_/\____/____/  
          /_/                                                                            /_/                                      
    """)


