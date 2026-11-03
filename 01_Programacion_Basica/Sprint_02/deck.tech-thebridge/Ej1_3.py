"""
Es tu primer día en la biblioteca del barrio. Empieza creando tú las dos colecciones:
libros: la lista con los 8 títulos: "El mal de Corcira", "Un mundo feliz", "Lolita", "Crimen y castigo", "El senor de los anillos", "Cien anos de soledad", "Harry Potter" y "Seda".
biblioteca: la lista de tuplas (título, unidades) con esos mismos títulos y, en el mismo orden, 4, 2, 5, 2, 6, 5, 9, 2 unidades.
Y con ellas responde, imprimiendo cada respuesta en su línea: 
1) cuántos títulos diferentes hay (usa un set); 
2) cuántas letras tiene la palabra "Seda"; 
3) cuántas unidades hay de "Seda" (busca su tupla en biblioteca); 
4) añade ("Data Science", 3) a biblioteca e imprime el total de unidades."""

libros = ["El mal de Corcira", "Un mundo feliz", "Lolita", "Crimen y castigo", 
          "El senor de los anillos", "Cien anos de soledad", "Harry Potter", "Seda"]

biblioteca = [("El mal de Corcira", 4), ("Un mundo feliz", 2), ("Lolita", 5), 
              ("Crimen y castigo", 2), ("El senor de los anillos", 6), 
              ("Cien anos de soledad", 5), ("Harry Potter", 9), ("Seda", 2)]

# 1) cuántos títulos diferentes hay (usa un set)
print(f"Títulos diferentes: {len(set(libros))}")

# 2) cuántas letras tiene la palabra "Seda"
print(f"Letras en 'Seda': {len("Seda")}")

# 3) cuántas unidades hay de "Seda" (busca su tupla en biblioteca)
for titulo, unidades in biblioteca:
    if titulo == "Seda":
        print(f"Unidades de 'Seda': {unidades}")
        break

# 4) añade ("Data Science", 3) a biblioteca e imprime el total de unidades
biblioteca.append(("Data Science", 3))
print(f"Total de unidades: {sum(unidades for titulo, unidades in biblioteca)}")
                      