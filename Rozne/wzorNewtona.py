#Wzór newtona an+1 = (s/an + an)/2
#a1 = 1

eps = 1e-10

s = float(input())

a = 1
b = (s/a + a)/2

while abs(a-b) >= eps:
    a = b
    b = (s/a + a)/2
print(b)