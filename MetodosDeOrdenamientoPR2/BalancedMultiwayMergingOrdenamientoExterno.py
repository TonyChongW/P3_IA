import heapq

def balanced_multiway_merge(sequences):
    # Creamos una lista de mont�culos (heaps) para realizar la fusi�n multidireccional equilibrada.
    min_heap = []
    result = []

    # Inicializamos el mont�culo con el primer elemento de cada secuencia.
    for seq in sequences:
        if seq:
            element = seq.pop(0)
            min_heap.append((element, seq))

    # Convertimos la lista de mont�culos en un mont�culo.
    heapq.heapify(min_heap)

    # Fusionamos las secuencias hasta que el mont�culo est� vac�o.
    while min_heap:
        smallest, seq = heapq.heappop(min_heap)
        result.append(smallest)

        if seq:
            element = seq.pop(0)
            heapq.heappush(min_heap, (element, seq))

    return result

# Ejemplo de uso:
if __name__ == "__main__":
    sequences = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Secuencias originales:", sequences)
    merged_sequence = balanced_multiway_merge(sequences)
    print("Secuencia fusionada:", merged_sequence)

