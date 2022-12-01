def compare_binary(T, S): # 1 dla t > s, 2 dla t < s, 3 dla t = s 
    N = len(T)

    i = 0

    while i < N:

        if T[i] < S[i]: return 1
        elif T[i] > S[i]: return 2

        i+=1
        
    return 3

 




TAB =  [
    [1,0,0,0,1,1,1,0],
    [1,0,1,0,1,1,1,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,0],
    [1,0,0,0,1,1,1,1],
    [1,1,0,1,1,0,1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,1,0,1,1,1,1]
]

min = TAB[0]
maks = TAB[0]

for i in range(len(TAB)):

    if compare_binary(min, TAB[i]) == 1:
        min = TAB[i]
    if compare_binary(maks, TAB[i]) == 2:
        maks = TAB[i]


print(maks)
print(min)
