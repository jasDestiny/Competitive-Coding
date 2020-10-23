def detectCycle(adjacencyMatrix, source):
    parents=[source]
    visited={}
    while parents:
        children=[]
        for i in parents:
            if i in visited:
                return "CYCLE DETECTED"
            visited[i]=True
            for i,j in enumerate(adjacencyMatrix[i]):
                if j==1:
                    children.append(i)
        parents=children.copy()
    return "NO CYCLES"
                    

adjacencyMatrix=[
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0]
]
print(detectCycle(adjacencyMatrix, 1))