def soln():
    arr=[1, 2]
    return arr[-1] if arr[-1]>arr[-2] else arr[-2]
print(soln())