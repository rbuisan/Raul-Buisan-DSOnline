"""Repaso del Sprint 1 con el bucle while. 
1) crea la variable fuerza con valor inicial 5 e imprime un mensaje de arranque; 
2) monta un while que se ejecute mientras fuerza < 10; 
3) dentro del bucle, imprime la fuerza actual y auméntala de uno en uno (tiene que pasar por 5, 6, 7, 8 y 9); 
4) ya fuera del bucle, imprime que el jugador ha subido de nivel."""

fuerza = 5
print("Arrancando el juego...") 
while fuerza < 10:
    print(f"Fuerza actual: {fuerza}")
    fuerza += 1
print("El jugador ha subido de nivel.")

