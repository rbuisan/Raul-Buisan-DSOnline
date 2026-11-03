ALTAS_TEXTO = """  Alba   Requena ;  ALBA.REQUENA@bridge.example ; Data Science

sergio molina ; sergio.molina@bridge.example ; IA Engineering
Nuria Bel ; nuria.bel.bridge.example ; Data Science
CARLA VIDAL ; carla.vidal @Bridge.Example ; Ciberseguridad
  Iván  Tejero ; ivan.tejero@BRIDGE.example ;  Data  Science 

Marta Sanchís ; MARTA.SANCHIS@BRIDGE.EXAMPLE ; IA Engineering
SERGIO   MOLINA ;  Sergio.Molina@bridge.example  ; IA Engineering
Adrián Gascó ; adrian.gasco@bridge.example ; Ciberseguridad
  Noa Ferrán;noa.ferran@bridge.example;Data Science
Óscar Ibáñez ; oscar.ibanez@bridge.example ; IA Engineering 
elena  cortés ; ELENA.CORTES@bridge.example ; Data Science"""


# Bridge SA · Operations — altas de la cohorte de marzo
#
# ALTAS_TEXTO ya esta cargado con el listado, tal cual.
# Cada linea util tiene la forma:  Nombre ; correo ; programa
#
# Deja preparadas estas tres cosas:
#   altas_limpias -> lista de listas [nombre, email, programa]
#   descartes     -> lista de listas [linea_original, motivo]
#   artefacto     -> el paquete que se lleva el Sprint 2
#
# Recuerda: linea en blanco se salta (no es descarte); correo sin @ o que
# no acabe en @bridge.example es descarte "email_invalido"; correo ya
# visto es descarte "duplicado". Y primero se limpia, despues se decide.
#
# Trucos: " ".join(t.split()) deja un solo espacio entre palabras;
#         "".join(t.split()) los quita todos;  t.title() pone la inicial
#         de cada palabra en mayuscula.

altas_limpias = []
descartes = []
vistos = []

def clean_entry(items):
    if (len(items) == 3):
        print("items:", items)
        nombre = " ".join(items[0].split()).title()
        email = "".join(items[1].split()).lower()
        programa = " ".join(items[2].split()).title()


        if (not "@" in email or not email.endswith("@bridge.example")):
            descartes.append([items, "email_invalido"])
        elif email in vistos:
            descartes.append([items, "duplicado"])
        else:

            if programa == ("Ia Engineering"): # Caso especial de formato de IA
                programa = "IA Engineering"

            altas_limpias.append([nombre, email, programa])
            vistos.append(email)        

for linea in ALTAS_TEXTO.split("\n"):
    elementos = linea.split(";")
    clean_entry(elementos)


artefacto = {
    "artefacto": "altas_limpias",
    "fuente": "",          # <- de donde salen estos datos
    "columnas": ["nombre", "email", "programa"],
    "altas": altas_limpias,
    "descartes": descartes,
}

print("Altas validas:", len(altas_limpias))
for alta in altas_limpias:
    print(alta)
print("===========")
print("Descartes:", len(descartes))
for descarte in descartes:
    print(descarte)
