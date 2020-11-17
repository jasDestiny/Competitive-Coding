def fibo(x, dict={1: 1, 2: 1}):
    if x in dict:
        print(dict[x])
        return dict[x]
    else:
        dict[x]=fibo(x-1)+fibo(x-2)
        print(dict[x])
        return dict[x]

print("solution: ",fibo(10))