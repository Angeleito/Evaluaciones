def main():
    print("UCAB, Elaborado por Araujo y Ornelas")
    
    # Solicitud de datos
    print("Introduzca un número entero positivo entre 1547 y 1699: ")
    X1 = int(input())
    
    # Procesamiento de datos
    if X1 >= 1547 and X1 <= 1699:
        N = (X1 // 100)
        r = (X1 % 100)
        Td = (r // 10)
        Cd = (r % 10)
        Pd = (N // 10)
        Sd = (N % 10)
        
        if ((Pd + Sd) % 2 != 0):  # Si la suma de los dos primeros dígitos es impar
            X2 = (Cd * 1000) + (Td * 100) + (Sd * 10) + Pd
        else:  # Si la suma de los dos primeros dígitos es par
            X2 = (Cd * 1000) + (Td * 100) + (Pd * 10) + Sd
        
        # Definiendo las variables para comparar y sumar
        p1 = N
        p2 = r
        N2 = (X2 // 100)
        r2 = (X2 % 100)
        p3 = r2
        p4 = N2
        
        # Determinar la suma excluyendo el mayor
        if (p1 > p2) and (p1 > p3) and (p1 > p4):
            Sum = p2 + p3 + p4
        elif (p2 > p1) and (p2 > p3) and (p2 > p4):
            Sum = p1 + p3 + p4
        elif (p3 > p1) and (p3 > p2) and (p3 > p4):
            Sum = p1 + p2 + p4
        elif (p4 > p1) and (p4 > p2) and (p4 > p3):
            Sum = p1 + p2 + p3
        
        # Suma total
        X3 = p1 + p2 + p3 + p4
        
        # Calcular el promedio de X1, X2 y X3
        prom = (X1 + X2 + X3) / 3
    else:
        print("El número no es correcto")
        print("El número introducido es: ",X1) 
    
    # Salida de datos
    print("El número introducido es: ",X1) 
    print("El número invertido es: ", X2)
    print("Los pares de numeros entre X1 y X2 son:","P1:",p1,"P2:",p2,"P3:",p4,"P4:",p3)
    print("La suma excluyendo el mayor valor es:", Sum)
    print("La suma total de los valores es:", X3)
    print("El promedio de X1, X2 y X3 es:", prom)
main()