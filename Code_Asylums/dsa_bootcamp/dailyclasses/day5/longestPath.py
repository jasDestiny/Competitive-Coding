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


