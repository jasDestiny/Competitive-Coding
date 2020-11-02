
def shortestPath(map, source, target):
    greedy, visited=[float("inf") for i in range(len(map))], [False for i in range(len(map))]
    greedy[source],visited[source] =0, True
    parent=[source]
    current=parent
    for i in range(len(map)):
        nextChildDist=float("-inf")
        nextChild=None
        for j,k in enumerate(map[current]):
            greedy[j]=min(greedy[j], greedy[current]+k)
            if nextChildDist>greedy[j]:
                nextChildDist=greedy[j]
                nextChild=j
        current=nextChild
    return greedy[target]
        