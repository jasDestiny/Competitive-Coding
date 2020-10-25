def withinBounds(x, y, xLen, yLen):
    if x<0 or y<0 or x>=xLen or y>=yLen:
        return False
    return True

def minimumEffortPath(heights):
    x,y=0,0
    xLen=len(heights[-1])
    yLen=len(heights)
    solution=[]
    checkPointX=0
    checkPointY=0
    pathTaken=None
    minDiff=float("inf")
    a=float("-inf")
    for i in heights:
        i.append(float("inf"))
    heights.append([float("inf")]*len(heights[-1]))
    count=0
    while x!=len(heights[-1]) and y!=len(heights) and count<5:
        print(x,y,a)
        right=abs(heights[y+1][x]-heights[y][x])
        down=abs(heights[y][x+1]-heights[y][x])
        if min(right, down)>minDiff:
            a=minDiff
            if pathTaken=="right":
                x=checkPointX+1
            else:
                y=checkPointY+1
        else:
            if right>down:
                x+=1
                if minDiff>right:
                    checkPointX=x
                    checkPointY=y
                    minDiff=right
                    pathTaken="right"
                a=max(a, right)
            else:
                y+=1
                if minDiff>down:
                    checkPointX=x
                    checkPointY=y
                    minDiff=down
                    pathTaken="down"
                a=max(a, down)
        count+=1
    return a

heights=[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(minimumEffortPath(heights))
    