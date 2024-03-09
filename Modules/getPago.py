import Storage.pago as pag

def getFechaPago():
    clientesPago= set()
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPago.add(val.get("codigo_cliente"))

    return clientesPago


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


         
def getAllFormaDePago():
    Paypal = set ()
    for val in pag.pago:
        FormaPago = val.get("forma_pago")
        if FormaPago not in Paypal:
            Paypal.add (FormaPago)
    return Paypal 

