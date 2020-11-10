
def printPossible(rows, grid, permissibleTime):
    parent=[[0,0]]
    time=0
    visited=[[True for i in range(len(grid[0]))] for j in range(len(grid))]
    target=[len(grid[0])-1, len(grid)-1]
    visited[0][0]=False
    x=[1,0,-1,0]
    y=[0,1,0,-1]
    while parent:
        time+=1
        children=[]
        found=False
        for i in parent:
            for j in range(4):
                pointX=i[0]+x[j]
                pointY=i[0]+y[j]
                if pointX<len(grid[0]) and pointY<len(grid) and pointX>-1 and pointY>-1:
                    if visited[pointY][pointX] and grid[pointX][pointY]=='.':
                        visited[pointY][pointX]=False
                        children.append([pointY, pointX])
                if pointX==target[0] and pointY==target[1]:
                    found=True
                    break
        if found:
            break
        parent=children.copy()
        children=[]
    return True if time<=permissibleTime and found else False

rows=2
grid=[['.','#'],['#','.']]
permissibleTime=2
print(printPossible(rows, grid, permissibleTime))