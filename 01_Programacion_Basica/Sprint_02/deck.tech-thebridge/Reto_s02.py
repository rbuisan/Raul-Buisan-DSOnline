"""
Lista limpia sprint 1:

Alba Requena | alba.requena@bridge.example | Data Science
Sergio Molina | sergio.molina@bridge.example | IA Engineering
Carla Vidal | carla.vidal@bridge.example | Ciberseguridad
Iván Tejero | ivan.tejero@bridge.example | Data Science
Marta Sanchís | marta.sanchis@bridge.example | IA Engineering
Adrián Gascó | adrian.gasco@bridge.example | Ciberseguridad
Noa Ferrán | noa.ferran@bridge.example | Data Science
Óscar Ibáñez | oscar.ibanez@bridge.example | IA Engineering
Elena Cortés | elena.cortes@bridge.example | Data Science

Lista nueva sprint 2:

Vera Montull ; vera.montull@bridge.example ; Data Science
Rubén Alcaraz ;  Ruben.Alcaraz@Bridge.example  ; IA Engineering
VERA MONTULL ;   VERA.MONTULL@bridge.example ; Data Science
Alba Requena ;  ALBA.REQUENA@BRIDGE.EXAMPLE ; Data Science
Nadia Solé ; nadia.sole@bridge.example ; Ciberseguridad
Vera Montull Ríos ; vera.montull@bridge.example ; Data Science
Tomás Iriarte ; tomas.iriarte@bridge.example ; IA Engineering

Diccionario cohortes ( programa → código de cohorte )
"Data Science" → "DS-MAR26"
"IA Engineering" → "IAE-MAR26"


Reglas:

Las reglas del registro
- La identidad es el correo, normalizado: sin espacios y en minúsculas. 
VERA.MONTULL@… y elena.vidal@… son la misma persona, aunque el nombre esté escrito distinto.
- Alguien que ya está en la cohorte no entra otra vez: el método de alta devuelve False y lo anota como rechazo con motivo "duplicado".
- Quien es de otro programa tampoco entra en esa cohorte: motivo "otro_programa". 
Con el reparto bien hecho no debería pasar nunca: es el cinturón de la clase, y se comprueba llamándola a mano.
- Quien viene de un programa sin cohorte abierta no es un rechazo: no hay dónde meterlo. 
Va a la lista sin_cohorte, y su programa aparece en el conjunto programas_sin_cohorte.
- Una línea en blanco no es nadie: se salta al parsear, no crea una persona vacía.
- Cada rechazo se anota en la propia cohorte, como {"email": …, "motivo": …}. Un rechazo sin motivo no le sirve a nadie.


"""

# Bridge SA · Operations — el registro de cohortes
#
# Ya tienes cargado:
#   ALTAS_PREVIAS  lista de dicts {"nombre", "email", "programa"} (viene del S1)
#   HOJA_NUEVAS    el texto de la hoja de esta semana: "nombre ; correo ; programa"
#   COHORTES       dict {programa: codigo} con las cohortes abiertas
#   ORIGEN_ALTAS   de donde salen las altas previas (para el artefacto, no lo cambies)
#
# Deja preparado esto, con estos nombres exactos:
#   normalizar_email(texto)    -> str, sin espacios y en minusculas
#   parsear_hoja(texto)        -> list de dicts {"nombre", "email", "programa"}
#   class Cohorte(codigo, programa) -> self.codigo, self.programa,
#                                 self.miembros (dict correo -> persona),
#                                 self.rechazos (list de {"email", "motivo"}),
#                                 alta(persona) -> True / False,
#                                 emails() -> set, total() -> int, y __str__
#   registro                   -> dict {codigo: Cohorte}, uno por cohorte abierta
#   inscribir(registro, altas) -> (registradas, sin_cohorte)
#   sin_cohorte, programas_sin_cohorte, artefacto

ALTAS_PREVIAS = [
    {"nombre": "Alba Requena", "email": "alba.requena@bridge.example", "programa": "Data Science"}, 
    {"nombre": "Sergio Molina", "email": "sergio.molina@bridge.example", "programa": "IA Engineering"}, 
    {"nombre": "Carla Vidal", "email": "carla.vidal@bridge.example", "programa": "Ciberseguridad"}, 
    {"nombre": "Iván Tejero", "email": "ivan.tejero@bridge.example", "programa": "Data Science"}, 
    {"nombre": "Marta Sanchís", "email": "marta.sanchis@bridge.example", "programa": "IA Engineering"}, 
    {"nombre": "Adrián Gascó", "email": "adrian.gasco@bridge.example", "programa": "Ciberseguridad"}, 
    {"nombre": "Noa Ferrán", "email": "noa.ferran@bridge.example", "programa": "Data Science"}, 
    {"nombre": "Óscar Ibáñez", "email": "oscar.ibanez@bridge.example", "programa": "IA Engineering"}, 
    {"nombre": "Elena Cortés", "email": "elena.cortes@bridge.example", "programa": "Data Science"}]

HOJA_NUEVAS = """Vera Montull ; vera.montull@bridge.example ; Data Science
Rubén Alcaraz ;  Ruben.Alcaraz@Bridge.example  ; IA Engineering
VERA MONTULL ;   VERA.MONTULL@bridge.example ; Data Science
Alba Requena ;  ALBA.REQUENA@BRIDGE.EXAMPLE ; Data Science
Nadia Solé ; nadia.sole@bridge.example ; Ciberseguridad
Vera Montull Ríos ; vera.montull@bridge.example ; Data Science
Tomás Iriarte ; tomas.iriarte@bridge.example ; IA Engineering
"""

COHORTES = {'Data Science': 'DS-MAR26', 'IA Engineering': 'IAE-MAR26'}
ORIGEN_ALTAS = "reto ds-reto-s01 · entrega del propio alumno (intento 1)"




# print("============")
# print(ALTAS_PREVIAS)
# print("============")
# print(f"HOJA_NUEVAS {type(HOJA_NUEVAS)}")
# print(HOJA_NUEVAS)
# print("============")
# print(type(COHORTES))
# print(COHORTES)
# print("============")
# print(type(ORIGEN_ALTAS))
# print(ORIGEN_ALTAS)
# print("============")

def normalizar_email(texto):
    normalizado = "".join(texto.split()).lower()
    return normalizado


def parsear_hoja(texto):
    # una linea = "nombre ; correo ; programa"
    # una linea en blanco no es nadie: no crea ninguna fila
    filas = []
    for linea in texto.split("\n"):
        if linea.strip():  # ignorar líneas en blanco
            nombre, email, programa = linea.split(" ; ")
            
            nombre = " ".join(nombre.split()).title()
            email = "".join(email.split()).lower()
            programa = " ".join(programa.split()).title()
            programa.replace("Ia Engineering", "IA Engineering")
            filas.append({"nombre": nombre, "email": email, "programa": programa})
    return filas


class Cohorte:
    def __init__(self, codigo, programa):
        self.codigo = codigo
        self.programa = programa

    def alta(self, persona):
        # motivos de rechazo: "duplicado" y "otro_programa"
        if persona["programa"] != self.programa:
            self.rechazos.append({"email": persona["email"], "motivo": "otro_programa"})
            return False
        return False


def inscribir(registro, altas):
    registradas = []
    fuera = []
    # cada alta va a la cohorte de SU programa; si no hay ninguna abierta
    # para ese programa, no es un rechazo: es que no hay donde meterla
    return registradas, fuera


registro = {}
todas = list(ALTAS_PREVIAS) + parsear_hoja(HOJA_NUEVAS)
indice = 1


for item in todas:
    print(f"{indice} - {item['nombre']} - {item['email']} - {item['programa']}")
    indice += 1

registradas, sin_cohorte = inscribir(registro, todas)
programas_sin_cohorte = set()

artefacto = {
    "artefacto": "registro_cohortes",
    "fuente": "",            # <- de donde sale esto
    "origen": ORIGEN_ALTAS,  # <- la procedencia no te la inventas: se arrastra
    "cohortes": {},          # <- {codigo: {"programa", "miembros", "total"}}
    "rechazos": [],          # <- los de todas las cohortes, juntos
    "sin_cohorte": sin_cohorte,
}

print("Miembros:", sum(c.total() for c in registro.values()),
      "· Sin cohorte:", len(sin_cohorte))
