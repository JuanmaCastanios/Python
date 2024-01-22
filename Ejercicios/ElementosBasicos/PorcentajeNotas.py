# Escribe un programa PorcentajeNotas que lea por teclado cinco números enteros correspondientes al número de sobresalientes, 
# notables, aprobados, suspensos y no presentados de una asignatura, y muestre por pantalla el porcentaje de cada uno de ellos.
# Además, deberá mostrar el porcentaje total de presentados y de no presentados. De los presentados mostrará el porcentaje de aprobados y no aprobados. 

if __name__ == "__main__":
    sb = int(input("Introduce los sobresalientes: "))
    n = int(input("Introduce los notables: "))
    aprobados = int(input("Introduce los aprobados: "))
    suspensos = int(input("Introduce los suspensos: "))
    noPresentados = int(input("Introduce los no presentados: "))
    total = (sb + n + aprobados + suspensos + noPresentados)

    print("SB =",sb,"(",(sb/total)*100,"%)")
    print("N =",n,"(",(n/total)*100,"%)")
    print("A =",aprobados,"(",(aprobados/total)*100,"%)")
    print("S =",suspensos,"(",(suspensos/total)*100,"%)")
    print("NP =",noPresentados,"(",(noPresentados/total)*100,"%)")
    print("Total =",total,"(",(total/total)*100,"%)")
    print("Total presentados =",(sb + n + aprobados + suspensos),"(",((sb + n + aprobados + suspensos)/total)*100,"%)")
    print("Total aprobados =",(sb + n + aprobados),"(",((sb + n + aprobados)/(sb + n + aprobados + suspensos))*100,"%)")
    print("Total aprobados =",suspensos,"(",(suspensos/(sb + n + aprobados + suspensos))*100,"%)")
    