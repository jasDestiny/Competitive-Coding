n=int(input())
    connections={}
    for i in range(n-1):
        x,y=[int(x) for i in input().split()]
        if x not in connections:
            connections[x]=[y]
        else:
            connections[x].append(y)
