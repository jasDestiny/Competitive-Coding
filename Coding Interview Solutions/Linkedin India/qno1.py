def bitwiseEquations(a, b):
    solution=[]
    for i in range(0, len(a), 1):
        notFound=True
        for j in range(0, a[i], 1):
            if j^(a[i]-j)==b[i]:
                print(j, a[i]-j)
                notFound=False
                solution.append((2*j)+(3*(a[i]-j)))
                break
        if notFound:
            solution.append(0)
    return solution
print(bitwiseEquations([29, 36, 57],[25, 18, 3]))

