def isArithmetic(arr):
    if len(arr)<2:
        return False
    for i in range(1, len(arr),1):
        arr.sort()
        if arr[i]-arr[i-1]!=arr[1]-arr[0]:
            return False
    return True

def checkArithmeticSubarrays(nums, l, r):
    """
    :type nums: List[int]
    :type l: List[int]
    :type r: List[int]
    :rtype: List[bool]
    """
    solution=[]
    for i in range(len(l)):
        solution.append(isArithmetic(nums[l[i]:r[i]+1]))
    return solution
            
print(checkArithmeticSubarrays([4,6,5,9,3,7],[0,0,2],[2,3,5]))