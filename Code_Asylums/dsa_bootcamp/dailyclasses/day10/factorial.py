def factorial(x, fact={0:1, 1:1}):
    if x in fact:
        return fact[x]
    else:
        fact[x]=x*factorial(x-1)
        return fact[x]
print(factorial(500))