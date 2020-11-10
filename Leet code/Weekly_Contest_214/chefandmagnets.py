testcases=int(input())
for testcase in range(testcases):
    n,k = [int(i) for i in input().split(' ')]
    string=str(input())
    length=len(string)
    count, i=0, 0
    stack=[]
    magneticPower=0
    attracted=set()
    count=0
    count1=0
    while i<length:
        if string[i]=='M':
            magneticPower+=(k+1)
            stack.append(i)
        elif string[i]=='I':
            if magneticPower>0:
                count1+=1
                attracted.add(i)
                stack.pop()
                if stack:
                    magneticPower=abs(stack[-1]-i)-count
                else:
                    magneticPower=0
        elif string[i]==':':
            magneticPower-=1
            count+=1
        elif string[i]=='X':
            magneticPower=0
        i+=1
    
    i=len(string)-1
    while i>-1:
        if string[i]=='M':
            magneticPower+=(k+1)
            stack.append(i)
        elif string[i]=='I':
            if magneticPower>0 and i not in attracted:
                count1+=1
                attracted.add(i)
                stack.pop()
                if stack:
                    magneticPower=abs(stack[-1]-i)-count
                else:
                    magneticPower=0
        elif string[i]==':':
            magneticPower-=1
            count+=1
        elif string[i]=='X':
            magneticPower=0
        i-=1


    print(count1)