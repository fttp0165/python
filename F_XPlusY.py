
def f_XplusY(X, Y):
    Z = []
    if (len(X) == len(Y)):
        for i in range(len(X)):
            Z.append(X[i]+Y[i])
        return Z


A = [1, 2, 3, 4]
B = [5, 6, 7, 8]
print(f_XplusY(A, B))
