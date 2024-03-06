import  Storage.cliente as cli

def getAllClientsName():
    clienteName = list()
    for val in cli.cliente:
        codigoName = dict({
              "codigo_cliente": val.get('codigo_cliente'),
              "codigo_cliente": val.get('nombre_cliente')
            
        })
        clienteName.append(codigoName)  
    return clienteName 

def getOneClienteCodigo(codigo):
    for val in cli.cliente:
        if(val.get('codigo_cliente') == codigo):
            return {
                "codigo_cliente": val.get('codigo_cliente'), 
                "nombre_cliente": val.get('nombre_cliente')
         } 
            
def getAllClientCreditCiudad(limiteCredit, ciudad):
    ClientCredit.append(val)
    return ClientCredit 
  
def getAllClientPaisRegionCiudad(pais,region=None, ciudad=None): 
    clientZone = list()
    for val in cli.cliente:
        if(val.get('pais') == pais):
            
            if((region != None or val.get('region') == region)):
                clientZone.append(val) 
            elif((region != None and val.get('region') == region)): 
                clientZone.append(val)     
    return clientZone
  
            
     
        
        

