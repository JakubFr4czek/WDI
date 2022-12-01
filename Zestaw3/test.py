T = [0, 2]


def ciag(n):
    if(n < len(T)): return T[n]
    else: T.append((1/2)*(T[n - 1] + (1/T[n - 1])))





for i in range(1,10):

    ciag(i)
    print(T[i])