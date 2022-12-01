from math import sqrt

def czy_prime(liczba):

    if liczba < 2: return False

    if liczba % 2 == 0 or liczba % 3 == 0: return False

    n = 5

    while n <= sqrt(n):

        if liczba % n == 0: return False

        n += 2

        if liczba % n == 0: return False

        n+=4

    return True

T = [17, 8, 8, 4,5, 17, 17]


for i in range(len(T)):
    T[i] = czy_prime(T[i])

print(T)

a = 1
b = 1

S = [] #fibuś

while a < len(T):
    
    a, b = b, a+b
    S.append(a)
print(S)
posInFibus = 0

white2115potrzymajmitonachwile = 0

for i in range(len(T)):

    if posInFibus < len(S) and i == S[posInFibus]:
        print(i, S[posInFibus], T[i])
        posInFibus+=1

        if T[i] == True:
            print("WYPIERDALAAAAAJ!")
            exit()

    else:
        if T[i] == True:
            white2115potrzymajmitonachwile+=1

    
if white2115potrzymajmitonachwile > 0:
    print("KURWRWADFSSSSAS sTRTATATKKKK")


