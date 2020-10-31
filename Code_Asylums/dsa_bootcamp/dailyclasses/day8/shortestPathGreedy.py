def shortestPath(map, source, target):
    greedy=[float("inf") for i in range(len(map))]
    greedy[source]=0
    parent=[source]
    current=parent
    while parent:
        for i in parent:
            for j,k in enumerate(map[i]):
                if k!=float("-inf"):
                    