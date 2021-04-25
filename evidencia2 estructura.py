venta = []
respuesta = 1
total=0
resp=1

import datetime
opcion = int(input("ingrese la opcion"))
if opcion == 1:
    idventa = input("ingrese la clave de venta")
    while resp == 1:
        """
        if venta:
            clave = max("venta") + 1
        else:
            clave = 1
            """
        Descripcion = input ("\nDescribe el producto: ")
        Cantidad = int(input("Cantidad de piezas: "))
        Precio = int(input("Precio: "))
        total = str(total+(Cantidad*Precio))
        date_object = datetime.date.today()
        registro = [Descripcion,Cantidad,Precio]
         
         
        resp = int(input("desea capturar otro registro 1-si 2-no"))
    venta[idventa] = [registro,total,date_object]
     
     
if opcion == 2:
    clave_buscar = int(input("ingrese la clave"))
    if clave_buscar in venta.keys():
        print(venta[clave_buscar])
    else:
        print("clave no registrada")
if opcion 
         