n = int(input())

cnt = 0
sum = 0
a = 1

while sum <= n:
    cnt += 1
    sum += a
    a += 2
print(cnt - 1)