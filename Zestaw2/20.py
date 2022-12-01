from math import sqrt

def change_base(l, b):

    T = []

    while l > 0:

        T.append(l%b)
        l//=b

    return T

a = int(input())
b = int(input())

for x in range(2  , 16 + 1):

    l1 = change_base(a, x)
    l2 = change_base(b, x)

    print(l1, " ", l2)


    for q in range(len(l1)):

        for w in range(len(l2)):

            if l1[q] == l2[w]:
                print("ten nie: ", x)
