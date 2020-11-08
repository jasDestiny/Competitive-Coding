class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n==0:
            return 0
        n+=1
        arr=[0, 1]
        maximum=max(arr)
        for i in range(2, n, 1):
            if i%2==0:
                arr.append(arr[i//2])
            else:
                arr.append(arr[i//2]+arr[(i//2)+1])
            if maximum<arr[-1]:
                maximum=arr[-1]
        return maximum
        