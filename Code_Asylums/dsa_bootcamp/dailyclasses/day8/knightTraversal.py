def withinBoard(x,y):
    if x<8 and y<8 and x>-1 and x>-1:
        return True
    else:
        return False

def knightTraversal(kx, ky, dx, dy):
    x=[2,2,-2,-2,1,-1,1,-1]
    y=[1,-1,1,-1,2,-2,-2,2]
    steps=1
    if kx==dx and ky==dy:
        return steps
    stepArray=[]
    while x:
        nextX=[]
        nextY=[]
        steps+=1
        found=False
        for i in range(len(x)): 
            if withinBoard(kx+x[i], ky+y[i]):
                if kx+x[i]==dx and ky+y[i]==dy:
                    found=True
                    break
                nextX.append(kx+x[i])
                nextY.append(ky+y[i])
        x=nextX.copy()
        y=nextY.copy()
        if found==True:
            return steps

print(knightTraversal(0,0,1,1))
    
