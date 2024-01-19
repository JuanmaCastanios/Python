def funcion_principal():
    # Código principal o punto de entrada
    print("¡Hola desde la función principal!")

# Ejemplo de una clase en Python

class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print("Hola, soy", self.nombre)


# Bloque de código que se ejecuta cuando el archivo es ejecutado como script
if __name__ == "__main__":
    # Código que se ejecuta al ejecutar el archivo directamente

    # Llamada a la función principal
    funcion_principal()

    # Creación de una instancia de la clase y llamada al método
    objeto = MiClase(nombre = "Juan José")
    objeto.saludar()
