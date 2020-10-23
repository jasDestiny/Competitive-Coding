class graph:
    def __init__(self, x={}, v=0):
        self.value=x
        self.vertices=v
    
    def ratTraverse(self, posX, posY, grid, visited, destX=3, destY=3):
        print(posX, posY)
        if posX>=len(grid[-1]) or posY>=len(grid):
            return False

        if visited[posY][posX]==1:
            return False

        visited[posY][posX]=1
        if destX==posX and destY==posY:
            return True
        
        if grid[posY][posX]==0:
            return False

        r=self.ratTraverse(posX+1, posY, grid, visited, destX, destY)
        d=self.ratTraverse(posX, posY+1, grid, visited, destX, destY)
        l=self.ratTraverse(posX-1, posY, grid, visited, destX, destY)
        u=self.ratTraverse(posX, posY-1, grid, visited, destX, destY)

        return r or d or l or u
        
            

g=graph()
grid=[
[1,0,1,0],
[1,1,0,0],
[1,0,1,0],
[1,1,1,1]
]
visited=[
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]

print(g.ratTraverse(0, 0, grid, visited, 3, 3))

