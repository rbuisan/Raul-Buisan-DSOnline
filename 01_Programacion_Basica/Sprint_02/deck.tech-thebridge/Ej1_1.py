compra = ["pan", "leche", "huevos", "cafe"]

# TODO: imprime el primer elemento, el ultimo y el slice [1:3]
# TODO: anade "fruta" al final con append() y ordena la lista con sort()
# TODO: imprime la lista ordenada, cuantos elementos tiene y la posicion de "leche"
print(compra[0])
print(compra[-1])
compra.append("fruta")
compra.sort()
print(f"Lista: {compra} tamaño {len(compra)} posicion de leche: {compra.index('leche')}")