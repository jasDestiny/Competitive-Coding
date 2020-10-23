def detectCycle(adjacencyMatrix, source):
    parents=[source]
    visited={}
    while parents:
        children=[]
        for i in parents:
            if i in visited:
                return "CYCLE DETECTED"
            visited[i]=True
            for j in adjacencyMatrix[i]:
                if adjacencyMatrix[j]==1:
                    children.append(j)
        parents=children.copy()
    return "NO CYCLES"
                    

adjacencyMatrix=[
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
print(detectCycle(adjacencyMatrix, 1))