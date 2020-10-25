def withinBounds(x, y, xLen, yLen):
    if x<0 or y<0 or x>=xLen or y>=yLen:
        return False
    return True

def minimumEffortPath(heights):
    x,y=0,0
    X=[1,1,-1,-1]
    Y=[1,-1,1,-1]
    xLen=len(heights[-1])
    yLen=len(heights)



heights=[[1,2,2],[3,8,2],[5,3,5]]
print(minimumEffortPath(heights))
    