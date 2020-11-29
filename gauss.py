a = [
    [4, 8, 3],
    [5, 7, 1],
    [9, 3, 3],
]

b = [29, 22, 24]
n = len(a)
x = [1]*n

# Elimination
for k in range(n-1):
    for i in range(k + 1, n):
        pivot = a[i][k] / a[k][k]
        for j in range(k, n):
            a[i][j] = a[i][j] - a[k][j]*pivot
        b[i] = b[i] - b[k]*pivot
print(a)
print(b)


# back-substitution
for i in range(n-1,-1,-1):
    aux = b[i]
    for j in range(n):
        aux = aux - a[i][j]*x[j]
    x[i] = (a[i][i] + aux) / a[i][i]
print(x)