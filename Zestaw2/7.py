def ciag(n):

    return n*n + n + 1

liczba = int(input())

i = 1

while ciag(i) <= liczba:
    if liczba % ciag(i) == 0:
        print("si")
        exit()
    i+=1
print("no si")