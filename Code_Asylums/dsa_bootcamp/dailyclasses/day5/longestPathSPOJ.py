n=int(input())
    connections={}
    for i in range(n-1):
        x,y=[int(x) for i in input().split()]
        if x not in connections:
            connections[x]=[y]
        else:
            connections[x].append(y)
            
longest=0
def longestPath(connections, source):
    global longest
    currentLength=1
    if not connections[source]:
        return 1
    lengths=[0]
    for i in connections[source]:
        lengths.append(currentLength+longestPath(connections,i))
    maxi=max(lengths)
    lengths.remove(maxi)
    secondMaxi=max(lengths)
    print(source, maxi+secondMaxi)
    if maxi+secondMaxi>longest:
        longest=maxi+secondMaxi
    return maxi

