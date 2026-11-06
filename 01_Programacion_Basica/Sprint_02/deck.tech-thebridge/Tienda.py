
"""
Nombre de la clase: Tienda.
Atributos comunes: tipo, que vale "Electrodomésticos", y abierta, que vale True.
Atributos propios de cada tienda, que el constructor recibe en este orden: nombre (nombre, string), dirección (direccion, string), 
número de empleados (num_empleados, int) y ventas de los últimos 3 meses (ventas_3_meses, lista de 3 números).
Método para calcular las ventas de todos los meses, que devuelva un número con todas las ventas: total_ventas().
Método que calcula la media de ventas de los últimos meses, por empleado: ventas_por_empleado().
Método que devuelve en un string el nombre de la tienda, junto con su dirección: nombre_direccion().
Método que obtiene las ventas del último mes: ventas_ultimo_mes().
Método para dar una proyección de las ventas en caso de haber invertido X dinero en marketing en esa tienda, 
siendo X el parámetro de entrada: proyeccion_marketing(x). 
Si X es menor de 1000, cada venta de los últimos 3 meses se multiplica por 1.2; si X es mayor o igual de 1000, se multiplica por 1.5. Este método reescribe el atributo de ventas de los últimos 3 meses y devuelve la lista de ventas con el aumento aplicado.
Se pide:

Implementar la clase Tienda.
Crear tres tiendas con datos inventados: tienda1, tienda2 y tienda3.
Comprobar en al menos una de ellas todo lo implementado en la clase (sus atributos, media de ventas, ventas por empleado...).
Calcular la suma total de las ventas del último mes de todas las tiendas, con un bucle for, y guardarla en total_ultimo_mes.
Imprimir por pantalla los nombres de las tiendas cuya dirección contenga el string "Avenida".
Seguro que ya has hecho este apartado... Documenta la clase.

"""
class Tienda:
    """Clase tienda:
        Atributos comunes: tipo, que vale "Electrodomésticos", y abierta, que vale True.
Atributos propios de cada tienda, que el constructor recibe en este orden: nombre (nombre, string), dirección (direccion, string), 
número de empleados (num_empleados, int) y ventas de los últimos 3 meses (ventas_3_meses, lista de 3 números).
Método para calcular las ventas de todos los meses, que devuelva un número con todas las ventas: total_ventas().
    """
    tipo = "Electrodomésticos"
    abierta = True
    def __init__(self, nombre, direccion, num_empleados, ventas_3_meses):
        self.nombre = nombre
        self.direccion = direccion
        self.num_empleados = num_empleados
        self.ventas_3_meses = ventas_3_meses
    def total_ventas(self):
        return sum(self.ventas_3_meses)
    def ventas_por_empleado(self):
        return self.total_ventas() / self.num_empleados
    def nombre_direccion(self):
        return f"{self.nombre} - {self.direccion}"
    def ventas_ultimo_mes(self):
        return self.ventas_3_meses[-1]
    def proyeccion_marketing(self, x):
        if x < 1000:
            self.ventas_3_meses = [venta * 1.2 for venta in self.ventas_3_meses]
        else:
            self.ventas_3_meses = [venta * 1.5 for venta in self.ventas_3_meses]
        return self.ventas_3_meses


tienda1 = Tienda("Tienda 1", "Calle Falsa 123", 5, [1000, 2000, 3000])
tienda2 = Tienda("Tienda 2", "Avenida Siempre Viva 456", 10, [1500, 2500, 3500])
tienda3 = Tienda("Tienda 3", "Calle Real 789", 8, [2000, 3000, 4000])
total_ultimo_mes = 0
for tienda in [tienda1, tienda2, tienda3]:
    total_ultimo_mes += tienda.ventas_ultimo_mes()
    if "Avenida" in tienda.direccion:
        print(tienda.nombre)
print(f"Suma total de las ventas del último mes: {total_ultimo_mes}")

