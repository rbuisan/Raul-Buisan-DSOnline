def conversor_km_millas(distancia):
    return round(0.62 * distancia, 1)

def minmax(numeros):
    return min(numeros), max(numeros)

numeros = [22, 34, 15, 26, 18]
print(conversor_km_millas(113))
print(minmax(numeros))


class Coche:
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0
    def acelerar(self, incremento):
        self.velocidad += incremento

    def frenar(self, dec):
        self.velocidad -= dec
        self.velocidad = max(0, self.velocidad)


a = Coche("Seat")
b = Coche("Tesla")
a.acelerar(50); b.acelerar(120); b.frenar(200)
print(f"Marca {a.marca} velocidad {a.velocidad}")
print(f"Marca {b.marca} velocidad {b.velocidad}")



# -------------

"""
El mismo gestor de biblioteca del repositorio, pero con dos clases que colaboran:

Libro(titulo, autor), con un método datos() que devuelva "titulo - autor";
Biblioteca(), que arranque con self.libros = [] y tenga agregar(libro), eliminar(titulo), buscar(titulo) (devuelve el libro o None) y mostrar().
Crea una biblioteca, agrega dos libros (por ejemplo "1984" de Orwell y "Un mundo feliz" de Huxley), busca uno por su título, muéstralos todos y elimina uno.
"""

class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def datos(self):
        return f"{self.titulo} - {self.autor}"

class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar(self, libro):
        self.libros.append(libro)

    def eliminar(self, titulo):
        self.libros = [libro for libro in self.libros if libro.titulo != titulo]

    def buscar(self, titulo):
        for libro in self.libros:
            if libro.titulo == titulo:
                return libro
        return None
    
    def mostrar(self):
        for libro in self.libros:
            print(libro.datos())

biblioteca = Biblioteca()
libro1 = Libro("1984", "Orwell")
libro2 = Libro("Un mundo feliz", "Huxley")
biblioteca.agregar(libro1)
biblioteca.agregar(libro2)
encontrado = biblioteca.buscar("1984")
if encontrado:
    print("Encontrado " + encontrado.datos())

print("Todos los libros:")
biblioteca.mostrar()



## -----------------------

texto = "el perro y el gato y el perro juegan en el jardin"
palabras = texto.split()
print(palabras)
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

ranking = sorted(
      conteo.items(), key=lambda x: x[1], reverse=True
  )
palabra_mas_repetida, max_frecuencia = ranking[0]
print(f"{palabra_mas_repetida}   {max_frecuencia}")