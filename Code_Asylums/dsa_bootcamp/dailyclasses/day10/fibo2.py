def fibo(x):
    if x==1 or x==2:
        print(1)
        return 1
    else:
        y=fibo(x-1)+fibo(x-2)
        print(y)
        return y 

print("solution: ",fibo(100))