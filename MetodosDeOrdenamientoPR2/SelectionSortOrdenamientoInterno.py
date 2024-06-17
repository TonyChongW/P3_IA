def selection_sort(arr):
    # Recorremos la lista desde el principio hasta el pen�ltimo elemento.
    for i in range(len(arr) - 1):
        # Suponemos que el elemento actual es el m�nimo.
        min_index = i
        
        # Comparamos el elemento actual con los elementos restantes en la lista.
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # Si encontramos un elemento m�s peque�o, actualizamos min_index.
                min_index = j
        
        # Intercambiamos el elemento actual con el elemento m�nimo encontrado.
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Lista original:", arr)
    selection_sort(arr)
    print("Lista ordenada:", arr)
