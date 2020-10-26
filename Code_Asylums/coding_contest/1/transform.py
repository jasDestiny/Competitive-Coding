def noOfSteps(source, target, transformations):
    transformations+=[source, target]
    hashMap={i:[] for i in transformations}
    createMap(hashMap, transformations)
    steps=-1
    found=False
    visited={i:False for i in transformations}
    parents=[source]
    while parents:
        children=[]
        steps+=1
        for i in parents:
            visited[i]=True
            for j in hashMap[i]:
                children.append(j)
    
    if found:
        print("Found in ",steps,"steps")
    else:
        print("unable to find")


def createMap(hashMap, transformations):
    for i in transformations:
        for j in transformations:
            if diff(i,j)==1:
                hashMap[i].append(j)
                
def diff(a, b):
    diff=0
    for i,j in enumerate(a):
        if j!=b[i]:
            diff+=1
    return diff

print(noOfSteps("mat", "bob", ["cat", "bat","cab","cob","dog"]))
