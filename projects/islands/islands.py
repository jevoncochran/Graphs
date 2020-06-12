from util import Stack

islands = [[0, 1, 0, 1, 0],  # 4 islands
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

def get_neighbors(row, col, matrix):
    neighbors = []
    # north = matrix[row-1][col]
    # south = matrix[row+1][col]
    # west = matrix[row][col-1]
    # east = matrix[row][col+1]

    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((row-1, col))

    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.append((row+1, col))

    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((row, col-1))

    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((row, col+1))

    return neighbors

def dft(row, col, matrix, visited):
    stack = Stack()
    stack.push((row, col))
    while stack.size() > 0:
        row, col = stack.pop()
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(row, col, matrix):
                stack.push(neighbor)

def island_counter(matrix):
    count = 0
    visited = []

    for _ in range(len(matrix)):
        visited.append([False] * len(matrix[0]))

    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    dft(row, col, matrix, visited)
                    count+=1
                    
    return count

print(island_counter(islands))


# print(get_neighbors(1, 1, islands))
