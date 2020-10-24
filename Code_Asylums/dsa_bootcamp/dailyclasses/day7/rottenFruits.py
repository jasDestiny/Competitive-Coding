def withinBounds(x, y, X, Y):
    if x<X and y<Y and x>-1 and y>-1:
        return True
    return False

def rottenOrange(m, dimX, dimY):
    steps=1
    allRotten=False
    allIncontact=True
    x=[1,1,-1,-1]
    y=[-1,1,-1,1]
    while :
        for i in range(0, dimY, 1):
            for j in range(0, dimX, 1):
                if m[j][i]==-1:
                    
                    for k in range(4):

    return steps

matrix=[
    [1,0,1],
    [-1,-1,0],
    [0,0,1]
]
dimX,dimY=3,3
print(rottenOrange(matrix), dimX, dimY)