from tabulate import tabulate
import Modules.getClients as cliente 
import Modules.getOficina as oficina 
import Modules.getEmpleado as empleado  
import Modules.getPedido as pedidos

#print(tabulate(empleado.getAllNombreApellidoEmailJefe(), tablefmt= "grid"))


    
#print(tabulate(empleado.getAllNombreApellidoPuesto(), tablefmt= "grid"))

#print(tabulate(pedidos.getAllPedidosEntregadosAtrasadosDeTiempo(), tablefmt= "grid"))

#print(tabulate(pedidos.getAllPedidosClienteFechaEsperadaFechaDeEntrega(), tablefmt= "grid"))

print(tabulate(pedidos.getAllPedidosRechazados(), tablefmt= "grid")) 
