from math import sqrt


def sitko(ile_KURWA):

    TABLICA_KURWA = [True for chuj in range(ile_KURWA)]

    TABLICA_KURWA[0] = TABLICA_KURWA[1] = False
    for i in range(2, int(sqrt(ile_KURWA) + 1)):
        if TABLICA_KURWA[i]:

            for j in range(i * i, ile_KURWA, i):
                TABLICA_KURWA[j] = False
    return TABLICA_KURWA

KURWICA_JASNA = int(input())

S = sitko(KURWICA_JASNA)

for i in range(2, len(S)):

    if S[i]:
        print(i)
        
    
