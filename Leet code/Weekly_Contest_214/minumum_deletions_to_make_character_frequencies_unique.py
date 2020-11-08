def minDeletions(s) -> int:
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1

    l=[]
    for i in freq.items():
        l.append(i[1])

    l.sort()
    print(l)
    turns=0
    n=len(l)
    for i in range(0, n):
        for j in range(0, n-1):
            if l[j]==l[j+1] and l[j]!=0:
                turns+=1
                l[j]=l[j]-1
    return turns
print(minDeletions("bbcebab"))