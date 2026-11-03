stock = {"portatil": 12, "monitor": 5, "teclado": 30}

# TODO: recorre stock con .items() e imprime "producto: N uds" en cada vuelta
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad} uds")

# TODO: suma 3 al stock de "monitor" y anade la clave nueva "raton" con valor 18
stock["monitor"] += 3
stock["raton"] = 18
# TODO: imprime el stock actualizado
print("Stock actualizado:")
for producto, cantidad in stock.items():
    print(f"{producto}: {cantidad} uds")

categorias = ["info", "audio", "info", "video", "audio"]
# TODO: imprime las categorias unicas convirtiendo la lista en un set
print(f"Categorías únicas: {set(categorias)}")