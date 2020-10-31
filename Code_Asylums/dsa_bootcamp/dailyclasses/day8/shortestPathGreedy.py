def shortestPath(map, source, target):
    greedy=[float("inf") for i in range(len(map))]
    visited=[False for i in range(len(map))]
    greedy[source]=0
    visited[source]=True
    parent=[source]
    current=parent
    while parent:
        children=[]
        for i in parent:
            for j,k in enumerate(map[i]):
                if k!=float("-inf"):
