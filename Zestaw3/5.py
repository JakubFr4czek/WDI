def search_min(S):

    mini = S[0]
    pos = 0

    for i in range(1,len(S)):

        if S[i]>mini:
            mini = S[i]
            pos = i

    return (mini, pos)

T = []

a = int(input())
it = 0
T.append(a)

while a != 0:

    a = int(input())
    T.append(a)


for i in range(9):

    mini, pos = search_min(T)
    T[pos] = -1

mini, pos = search_min(T)
print(mini)





    
