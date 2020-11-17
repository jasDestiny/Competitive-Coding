def fibo(x, dict={1: 1, 2: 1}):
    if x in dict:
        return dict[x]
    else:
        dict[x]=fibo(x-1)+fibo(x-2)
        return dict[x]

print("solution: ",fibo(100))