def czy_wielokrotnosc_kwadratu_liczby_naturalnej(liczba):

    a = 2

    while a**2 <= liczba:
        #print(liczba%(a**2))
        if liczba%(a**2): return True
        a+=1
    return False


T = [[1,2,3,4,5],
     [1,2,16,16,16],
     [1,2,16,16,16],
     [1,2,16,16,16],
     [1,2,16,16,16]]

N = len(T)

for i in range(N): #wybieram wiersz do usuniecia

    for j in range(N): #wybieram jedna kolumne do usuniecia

        for k in range(N): #wybieram druga kolumne do usuniecia

            el = int(0)
            z = int(0)
            #print("-------------------")
            for q in range(N):
                for w in range(N):
                    
                    

                    if q != i and w != j and w !=k and j != k:
                        el+=1

                        if(czy_wielokrotnosc_kwadratu_liczby_naturalnej(T[q][w])): 
                            #print(T[q][w])
                            z+=1

                        
                        if i == 0 and j == 0 and k ==1: 
                            print(el, " ", w)

            
            if el == z and el != 0: 
                print("SIUUUUU!")