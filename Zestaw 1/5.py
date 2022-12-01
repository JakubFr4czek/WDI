pierwiastek = int(input())

a = 1 #pierwszy wyraz zawsze rowny 1
b = (pierwiastek / a + a)/2

eps = 1e-10

while abs(a - b) > eps:
    a = b
    b = (pierwiastek / a + a)/2

print(b)