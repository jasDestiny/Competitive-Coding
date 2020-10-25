def slowestKey(releaseTimes, keysPressed):
    if not releaseTimes:
        return None
    Sum=releaseTimes[0]
    for i in range(1, len(releaseTimes)):
        releaseTimes[i]=releaseTimes[i]-Sum
        Sum+=releaseTimes[i]
    print(releaseTimes)
    solution=[]
    maxi=max(releaseTimes)
    for i in range(len(releaseTimes)):
        if releaseTimes[i]==maxi:
            solution.append(keysPressed[i])
    return max(solution)

print(slowestKey([23,34,43,59,62,80,83,92,97], "qgkzzihfc"))
        