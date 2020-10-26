def noOfSteps(source, target, transformations):
    transformations+=[source, target]
    hashMap={i:[] for i in transformations}
    createMap(hashMap, transformations)
    steps=0
    found=False
    visited={i:False for i in transformations}
    visited[source]=True
    parents=[source]
    while parents:
        children=[]
        steps+=1
        for i in parents:
            for j in hashMap[i]:
                if not visited[j]:
                    children.append(j)
                if j==target:
                    found=True
                    break
            if found:
                break
        if found:
            break
        else:
            parents=children.copy()
            children=[]
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

noOfSteps("mat", "bob", ["cat", "bat","cab","cob","dog"])
