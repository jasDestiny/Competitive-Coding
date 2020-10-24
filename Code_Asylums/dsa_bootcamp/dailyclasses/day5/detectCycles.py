def detectCycle(adjacencyMatrix, current, visited, parent=None):
    if visited[current]:
        return True
    visited[current]=True
    for i,j in enumerate(adjacencyMatrix[current]):
        if j and i!=parent:
            if detectCycle(adjacencyMatrix, i, visited, current):
                return True
    return False

adjacencyMatrix=[
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0]
]
n=3
print(detectCycle(adjacencyMatrix, 0, [False]*n))