def datos():
    print("Verificador de integridad")
    print("Autor: Juan José Blanco Díaz")

#Sacar pro pantalla la cabecera de la aplicación
datos()
#Solicitar al usuario el mensaje y mostrar el hash
print("El valor del hash es:",hash(input("Introduce una cadena:")))