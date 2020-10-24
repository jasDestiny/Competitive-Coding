def detectCycle(adjacencyMatrix, source):
    parents=[source]
    visited={}
    while parents:
        children=[]
        for i in parents:
            print(i)
            if i in visited:
                return "CYCLE DETECTED"
            visited[i]=True
            for k,j in enumerate(adjacencyMatrix[i]):
                if j==1 and k!=i:
                    children.append(k)
        parents=children.copy()
    return "NO CYCLES"
                    

adjacencyMatrix=[
    [0, 1, 1],
    [1, 0, 1],
    [0, 1, 0]
]
print(detectCycle(adjacencyMatrix, 0))