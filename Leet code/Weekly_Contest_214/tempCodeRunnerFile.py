testcases=int(input())
for testcase in range(testcases):
    n,k = [int(i) for i in input().split(' ')]
    string=str(input())
    length=len(string)
    i=0 
    j=0
    alternator={True:['I', 'M'], False: ['M', 'I']}
    alt=True
    count=0
    solnArr=[]
    while i<length and j<length:
        if string[i]!=alternator[alt][0]:
            i+=1
            
        if string[j]!=alternator[alt][1]:
            j+=1

        if i>=length or j>=length:
            break

        if (alt and string[j]==':') or (not alt and string[i]==':'):
            count+=1
        
        if (alt and string[j]=="X") or (not alt and string[i]=='X'):
            print("go off")
            i=j=max(i,j)+1

        if string[i]==alternator[alt][0] and string[j]==alternator[alt][1]:
            print(string[i], string[j], i, j)
            alt=not alt
            value=k+1 - abs(j-i) - count
            if value>0 and alt:
                solnArr.append([value, j])
            elif value>0 and not alt:
                solnArr.append([value, i])
            count=0
    print(solnArr)
