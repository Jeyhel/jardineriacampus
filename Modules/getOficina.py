import Storage.oficina as of 

def getAllCodigoCiudad():
    getAllCodigoCiudad = []
    for val in of.oficina:
        codigoCiudad.append({
            
            "codigo": val.get ("codigo_oficina"),
            "codigo": val.get ("oficina")
        })
        return codigoCiudad 
    def getAllCiudadTelefeno(pais):
        getAllCiudadTelefeno = []
        for val in of.oficina:
            if(val.get("pais") == pais):
                ciudadTelefono.append ({
                
                "ciudad": val.get ("ciudad"), 
                "telefono": val.get ("telefono"), 
                "oficina": val.get ("codigo_oficina"), 
                "pais": val.get ("pais"), 
            })
            return ciudadTelefeno