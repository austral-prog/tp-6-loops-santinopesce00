# Replace the "ANSWER HERE" for your answer

def flatten(matrix):
    """
    Dada una lista de listas (matriz), retorna una unica lista
    con todos los elementos en orden.

    Ejemplo: flatten([[1, 2], [3, 4], [5, 6]]) -> [1, 2, 3, 4, 5, 6]
    """
    answer = []
    for lista in matrix:
        for elemento in lista:
            answer.append(elemento)
    return answer


def row_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la fila correspondiente.

    Ejemplo: row_sums([[1, 2, 3], [4, 5, 6]]) -> [6, 15]
    """
    answer = []
    for lista in matrix:
        suma = 0
        for elemento in lista:
            suma += elemento
        answer.append(suma)
    return answer


def col_sums(matrix):
    """
    Dada una matriz (lista de listas de numeros), retorna una lista
    donde cada elemento es la suma de la columna correspondiente.
    Se asume que todas las filas tienen la misma longitud.

    Ejemplo: col_sums([[1, 2, 3], [4, 5, 6]]) -> [5, 7, 9]
    """
    if len(matrix) == 0:
        return []
    num_cols = len(matrix[0])
    answer = []
    for col in range(num_cols):
        total = 0
        for fila in matrix:
            total += fila[col]
        answer.append(total)
    return answer
