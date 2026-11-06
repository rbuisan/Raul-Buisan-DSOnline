
# 1 --------------------
invitados = ["Pepe", "Juan", "Ana"]

for invitado in invitados:
    print(invitado)

invitados.sort()
primero = invitados[0]

baja = invitados.pop()
nuevo = "Gandhi"
indice = int(len(invitados) / 2)
invitados.insert(indice, nuevo)
print(invitados)

# 2 --------------------
tupla_1 = (5,)
print(f"tupla_1: {type(tupla_1)}")

tupla_2 = ("a", "b", "c")

tupla_3 = tupla_1 + tupla_2
print(f"tupla_3: {tupla_3}")

tupla_4 = tupla_3[:2]
print(f"tupla_4 (dos primeros valores): {tupla_4}")


# 6 --------------------
def junta_palabras(*args):
    return " ".join(args)

junto = junta_palabras("Hola", "me", "llamo", "Alberto")
print(junto)


# 7 --------------------

# Implementa aquí la clase Perro
class Perro:
    """Clase que representa a un perro con sus características y comportamientos básicos.

    Atributos de clase:
        num_patas (int): Número de patas del perro (4).
        num_orejas (int): Número de orejas del perro (2).
        num_ojos (int): Número de ojos del perro (2).

    Atributos de instancia:
        raza (str): La raza del perro.
        pelo (str): El color del pelo del perro. Por defecto, 'Marrón'.
        duenio (str, optional): El nombre del dueño. Por defecto, None.
        velocidad (int): La velocidad actual del perro. Inicialmente 0.
    """
    num_patas = 4
    num_orejas = 2
    num_ojos = 2

    def __init__(self, raza, pelo = "Marrón", duenio = None):
        self.raza = raza
        self.pelo = pelo
        self.duenio = duenio
        self.velocidad = 0
    def andar(self, aumento_velocidad):
        self.velocidad += aumento_velocidad
    def parar(self):
        self.velocidad = 0
    def ladrar(self, entrada):
        return f"GUAU!{entrada}"
    def doc(self):
        print(f"Raza {self.raza} Pelo {self.pelo} Duenio {self.duenio} Velocidad {self.velocidad}")
mi_perro = Perro("RAza")
mi_perro.andar(5)
print(mi_perro.velocidad)
mi_perro.parar()
print(mi_perro.velocidad)
ladrido = mi_perro.ladrar("tengo hambre")
print(ladrido)

mi_perro.doc()
