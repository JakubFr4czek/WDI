import random


#T = [random.randrange(1, 99, 2) for i in range(N)]
#print(T)
T = [1,2,3,4,5,4,3]
N= len(T)
r = T[1] - T[0]
count = 2

maxiPlus = 0
maxiMinus = 0

for i in range(1, N - 1):
    print(T[i + 1] - T[i])
    if T[i + 1] - T[i] == r:
        count += 1
    else:
        if r > 0 and count > maxiPlus:
            maxiPlus = count
        elif r < 0 and count > maxiMinus:
            maxiMinus = count
        count = 2
        r = T[i + 1] - T[i]
if r > 0 and count > maxiPlus:
    maxiPlus = count
elif r < 0 and count > maxiMinus:
    maxiMinus = count

print(maxiPlus,maxiMinus)
            


    
