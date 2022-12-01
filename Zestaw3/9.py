from random import randint

N = int(input())

T = [randint(1,100) for i in range(N)]
count = 1
maks = -1
for i in range(N - 1):

    if T[i] < T[i + 1]:
        count += 1
    else:
        count = 1

    if count > maks:
        maks = count
print(maks)