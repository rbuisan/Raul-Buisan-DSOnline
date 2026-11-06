
"""
Escribe factura(*precios, **opciones): acepta un número variable de precios con
*args y opciones con **kwargs. Suma el total,
aplica un 21% de IVA si llega iva=True, y devuelve el texto "TOTAL MONEDA" 
con el total redondeado a 2 decimales y la moneda de opciones ("EUR" si no se indica). 
Pruébala con factura(10, 20, 5), factura(10, 20, 5, iva=True) y factura(100, 50, iva=True, moneda="USD").
"""

def factura(*precios, **opciones):

    # TODO: suma los precios que llegan en la tupla 'precios'
    print(sum(precios))
    # TODO: si opciones trae iva, multiplica el total por 1.21
    hayIva = opciones.get("iva", False)
    if hayIva:
        total = sum(precios) * 1.21
    else:
        total = sum(precios)
        
    # TODO: coge la moneda de opciones ("EUR" si no viene)
    moneda = opciones.get("moneda", "EUR")
    # TODO: devuelve el texto "TOTAL MONEDA", con el total redondeado a 2 decimales
    return f"{total:.2f} {moneda}"

factura(10, 20, 5)
factura(10, 20, 5, iva=True)
factura(100, 50, iva=True, moneda="USD")
