T = [(1, 1), (2, 3), (4, 1), (4, 5)]

S = [0 for _ in range(len(T))]
G = [0 for _ in range(len(T))]
#ile pol szachuje i czy szachuje innych skoczkow:


N = 10
maks = 0
for i in range(len(T)):

    y,x = T[i]

    szachowanePola = 0

    if x + 1 < N and y - 2 >= 0:
        szachowanePola += 1

        for j in range(len(T)):
            if T[j] == (x + 1, y - 2): 
                szachowanePola -= 1 
                S[j]=1 
            
    if x + 2 < N and y - 1 >= 0:
        szachowanePola += 1
        for j in range(len(T)):
            if T[j] == (x + 2, y - 1): 
                szachowanePola -= 1 
                S[j]=1 

    if x - 1 >= 0 and y - 2 >= 0:
        szachowanePola += 1
        for j in range(len(T)):
            if T[j] == (x - 1, y - 2): 
                szachowanePola -= 1 
                S[j]=1 

    if x - 2 >= 0 and y - 1 >= 0:
        szachowanePola += 1
        for j in range(len(T)):
            if T[j] == (x - 2, y - 1): 
                szachowanePola -= 1 
                S[j]=1 

    if x - 2 >= 0 and y + 1 < N:
        szachowanePola += 1
        for j in range(len(T)):
            if T[j] == (x - 2, y + 1): 
                szachowanePola -= 1 
                S[j]=1 
    if x - 1 >= 0 and y + 2 < N:
        szachowanePola += 1

        for j in range(len(T)):
            if T[j] == (x - 1, y + 2): 
                szachowanePola -= 1 
                S[j]=1 
    if x +2 < N and y + 1 < N:
        szachowanePola += 1
        
        for j in range(len(T)):
            print(T[j], (x+2, y+1))
            if T[j] == (x + 2, y + 1): 
                
                szachowanePola -= 1 
                S[j]=1 
    print(S)
    if S[i] == 0:
        szachowanePola+=1
    if szachowanePola > maks:
        maks = szachowanePola

print(maks)