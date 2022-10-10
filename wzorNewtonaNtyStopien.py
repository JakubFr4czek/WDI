s = float(input()) #liczba z ktorej chce pierwiastek
n = int(input()) #stopien danego pierwiastka

eps = 1e-10

a = 1
b = (s/(a**(n-1)) + (n-1)*a)/n

while abs(a-b) >= eps:
    a = b
    b = (s/(a**(n-1)) + (n-1)*a)/n
print(a)