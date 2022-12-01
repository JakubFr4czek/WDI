N= int(input())

T = [0 + i for i in range(N + 1)]

def na4(liczba):
    
    S = [0 for _ in range(64)]
    it = 0
    while liczba > 0:
        S[it]=liczba%4
        liczba//=4
        S.sort()

    return S
    
def rowne(a,b):

    i = 0
    j = 0

    while i < len(a) and j < len(b):
        
       # print(a[i], " ", b[i])

        if a[i] == b[j]:
            if i < len(a): i+=1
            if j < len(b): j+=1
        elif a[i] < b[j]:
            temp = a[i]
            while i < len(a) and a[i]==temp: i+=1
        elif a[i] > b[j]:
            temp = b[j]
            while j < len(b) and b[j]==temp: j+=1

        elif a[i] != b[j]:
            return False

    return True


for i in range(1, N + 1):
    print(na4(T[i - 1]))
    print(rowne(na4(T[i-1]), na4(T[i])))
        
