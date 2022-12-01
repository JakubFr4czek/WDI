n = int(input())

a = 0
for i in range(len(str(n)) - 1, 0, -1):
    b = (n//10**i)%10

    if b <= a:
        print("nieeee :(")
        exit()
    a = b


    print(b)
if a >= n%10:
    print("helnoł")
print(n%10)

