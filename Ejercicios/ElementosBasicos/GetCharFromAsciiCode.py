# Escribe un programa llamado GetCharFromAsciiCode que devuelva el carácter asociado al valor ASCII en decimal introducido por teclado.

if __name__ == "__main__":
    ascii = input("Introduce un valor ASCII: ")
    print(chr(int(ascii)))