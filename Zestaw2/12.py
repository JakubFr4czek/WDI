n = int(input())

a = 0
for i in range(len(str(n)) - 1, 0, -1):
    b = (n//10**i)%10
    if b == len(str(n)):
        print("oł yeah")


    print(b)

if n%10 == len(str(n)):
    print("tataratatata")
print(n%10)

