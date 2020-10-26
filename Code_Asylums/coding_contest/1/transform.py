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
                    visited[j]=True
                if j==target:
                    found=True
                    return steps
        parents=children.copy()
        children=[]
    return -1

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

print(noOfSteps("mad", "bob", ["mat", "cat", "bat","cab","cob","dog"]))
