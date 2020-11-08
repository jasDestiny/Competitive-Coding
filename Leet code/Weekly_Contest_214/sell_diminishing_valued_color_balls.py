class Solution:
    def maxProfit(self, inventory, orders) -> int:
        inventory.sort(reverse=True)
        soln=0
        leng=len(inventory)
        while orders>0:
            orders-=1
            soln+=inventory[0]
            print(inventory[0], inventory)
            inventory[0]-=1
            if inventory[0]<inventory[1]:
                self.siftDown(inventory, 0, leng-1)
        return soln
    
    def siftDown(self, inventory, index, endIndex):
        c1=index*2 +1
        while c1<=endIndex:
            c2= -1 if c1+1>endIndex else c1+1
            indexToSwap=c1 if inventory[c1]> inventory[c2] else c2

            if inventory[indexToSwap]>inventory[index]:
                inventory[index], inventory[indexToSwap]=inventory[indexToSwap], inventory[index]
                index=indexToSwap
                c1=index*2 +1
            else:
                break



s=Solution()
print(s.maxProfit([3, 5], 6))
        
            
        
        
            
            