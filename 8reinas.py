def calcQueens(size):
    board = [-1]*size
    return queens(board, 0, size)

def queens(board, current, size):
    if current == size:
        return board  # Devuelve el tablero cuando se encuentra una solución
    else:
        for i in sorted(range(size), key=lambda x: heuristic_safe_queens(board, current)):
            board[current] = i
            if noConflicts(board, current):
                solution = queens(board, current + 1, size)
                if solution:
                    return solution
        return None  # Retorna None si no se encuentra ninguna solución

def noConflicts(board, current):
    for i in range(current):
        if board[i] == board[current] or current - i == abs(board[current] - board[i]):
            return False
    return True

def heuristic_safe_queens(board, current):
    safe_queens = 0
    for i in range(current):
        if noConflicts(board, i):
            safe_queens += 1
    return safe_queens

def costo_conflictos(board):
    n = len(board)
    conflicts = 0
    for i in range(n):
        for j in range(i+1, n):
            # Verificar si hay conflicto entre la reina en la fila i y la reina en la fila j
            if board[i] == board[j] or abs(i - j) == abs(board[i] - board[j]):
                conflicts += 1
    return conflicts

# Ejemplo de uso:
# print(calcQueens(8))  # Imprimir la primer solución encontrada para el problema de las 8 reinas utilizando la heurística.

print(calcQueens(int(input("Escribe el numero de reinas"))))  # Calcular el número de soluciones para el problema de las 8 reinas utilizando la heurística.
