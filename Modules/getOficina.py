import Storage.oficina as of 

def getCodigoOfiCiudadName():
    CodigoOfCiudad = list()
    for val in of.oficina:
        codigoNames = dict({
            "codigo_oficina": val.get('codigo_oficina'),
            "ciudad": val.get('ciudad')
        })
        CodigoOfCiudad.append(codigoNames)
    return CodigoOfCiudad
    
    
def getCiudadTelefonoEspaña():
    ciudadTelefonoEspaña = []
    for val in of.oficina:
        if val.get('pais') == "España" :
            ciudadTelefonoEspaña.append(
                {
                    "ciudad": val.get("ciudad"),
                    "telefono": val.get("telefono")
                }
            )
    return ciudadTelefonoEspaña