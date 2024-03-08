import Storage.pago as pag

def getFechaPago():
    clientesPago= set()
    for val in pag.pago:
        fechaPagos = val.get("fecha_pago")
        if fechaPagos.startswith("2008"):
            clientesPago.add(val.get("codigo_cliente"))

    return clientesPago