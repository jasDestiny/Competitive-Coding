def findShortestPath(graph, source, target):
    table, visited=[float("inf") for i in graph], [False for i in graph]
    current, currentDist=source, 0
    table[current], visited[current]=0, True
    for i in range(len(graph)):
        for i in range(0, len(graph[current]), 1):
            if graph[current][i]!=float("inf") and not visited[i]:
                table[i]=min(table[i], map[current][i]+currentDist)
        minVal, mini=float("inf"), None
        for i in range(len(table)):
            if table[i]<minVal and not visited[i]:
                visited[i]=True
                minVal=table[i]
                mini=i
        if mini==target:
            break
        current=min
        currentDist=minVal
    return table[current]

n=float("inf")
graph=[[0, 3, n, 7, 8],[3, 0, 1, 4, n],[n, 1, 0, 2, n],[7, 4, 2, 0, 4],[8, n, n, 3, 0]]
print(findShortestPath(graph, 0, 1))

