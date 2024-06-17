def radix_sort(arr):
    # Encontramos el n�mero m�ximo para determinar la cantidad de d�gitos.
    max_num = max(arr)
    exp = 1

    # Mientras haya d�gitos a procesar.
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Contamos la frecuencia de cada d�gito en el arreglo.
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Calculamos las posiciones finales de los d�gitos.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Colocamos los elementos en el arreglo de salida siguiendo el orden de los d�gitos.
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copiamos el arreglo de salida de nuevo al arreglo original.
    for i in range(n):
        arr[i] = output[i]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", arr)
    radix_sort(arr)
    print("Lista ordenada:", arr)

