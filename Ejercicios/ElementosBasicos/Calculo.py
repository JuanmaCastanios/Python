# Escribe un programa Calculo que acepte por teclado dos números y una operación aritmética y muestre el resultado por pantalla.
# Las posibles operaciones a realizar serán la suma, resta, multiplicación, división y resto sobre números reales.

# Metodos de operaciones
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def producto(a, b):
    return a * b

def division(a, b):
    if(b != 0):
        return a / b
    else:
        return "ERROR.No se puede dividir por 0"

def resto(a, b):
    return a % b

# Diccionario de operaciones
operaciones = {
    '+':suma,
    '-':resta,
    '*':producto,
    '/':division,
    '%':resto
}

# main
if __name__ == "__main__":
    num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))
    operador = input("Introduce la operación aritmética (+, -, *, /, %): ")
    
    # Verifica si el operador ingresado está en el diccionario de operaciones
    resultado = operaciones.get(operador, lambda x, y:"Operación no válida")(num1,num2)
    print(resultado)