def NWD(a,b):

    while b > 0:
        a,b = b, a%b

    return a


T = [1,2,3,4,5,6,2,8,73,134430,2344333,12,13,14,454,16,17,18,19,20]

N = len(T)
cnt = 0
for i in range(N):

    if i + 1 < N and NWD(T[i], T[i + 1]) == 1:
        if i + 2 < N and NWD(T[i + 1], T[i + 2]) == 1:
            cnt+=1
        elif i + 3 < N and NWD(T[i + 1], T[i + 3])== 1:
            cnt+=1
    elif i + 2 < 2 and NWD(T[i], T[i + 2]) == 1:
        if i + 3 < N and NWD(T[i + 2], T[i + 3])== 1:
            cnt+=1
        elif i + 4 < N and NWD(T[i + 2], T[i + 4])== 1:
            cnt+=1
print(cnt)