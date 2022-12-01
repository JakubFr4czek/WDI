n = int(input())


for i in range(len(str(n)) - 1, 0, -1):
    a = (n//10**i)%10

    if n%10 == a:
        print("piks smutny")
        exit()
print("hepi")
