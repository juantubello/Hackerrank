def quick_sort(piv, arr):
 
    pivot_local = piv
    array_local = arr
    izquierda = []
    derecha = []
 
    # Separo el array obtenido por parametro en izquierda y derecha a partir de el pivot obtenido por parametro validando que los elementos menores
    # al pivot pertenecen a la parte izquierda y los mayores o iguales a pivot pertenecen a la parte derecha |  izquierda <- pivot -> derecha

    for i in array_local:
        if i < pivot_local:
            izquierda.append(i)
        else:
            derecha.append(i)

    # Si la longitud es menor o igual a 1 significa que ya esta ordenado y no tengo que imprimirlo en consola, caso contrario
    # obtengo el pivot de la nueva lista a ordenar y quito el mismo del array que se pasa por parametro, de esta forma
    # genero el corte a la recursividad, ya que solo se llama a la recursion cuando el array necesita ordenarse(array > 1)
    # este proceso lo hago primero para la parte izquierda y luego para la parte derecha
          
    if len(izquierda) > 1:

        #Obtengo pivot
        piv_der = izquierda[0]

        #Obtengo el array sin el pivot
        arr_der = izquierda[1:]

        #Ordeno la lista llamando a la recursividad
        izquierda = quick_sort(piv_der, arr_der)
        print(*izquierda)

    if len(derecha) > 1:

        #Obtengo pivot
        piv_izq = derecha[0]

        #Obtengo el array sin el pivot
        arr_izq = derecha[1:]

        #Ordeno la lista llamando a la recursividad
        derecha = quick_sort(piv_izq, arr_izq)
        print(*derecha)

    #Devuelvo el array ordenado    
    return izquierda + [pivot_local] + derecha

arr = [5, 8, 1, 3, 7, 9, 2]

pivot = arr[0]
array = arr[1:]

print(*quick_sort(pivot, array))