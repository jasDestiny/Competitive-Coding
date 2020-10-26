def noOfSteps(source, target, transformations):
    hashMap={source:[], target:[]}
    for i in transformations:
        hashMap[i]=[]
    print(hashMap)
    transformations.append(source, target)

print(noOfSteps("mat", "bob", ["cat", "bat","cab","cob","dog"]))