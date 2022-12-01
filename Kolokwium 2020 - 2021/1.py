

def sprawdz(napis):

    N = len(napis)

    for rozmiar in range(1, int(N / 2) + 1):

        if N%rozmiar == 0:

            temp = napis[0:rozmiar]

            if napis.count(temp) == N//rozmiar:
                print("Pliko", temp)

    






T = ["ABCABCABC", "AAAA", "ABAABA"]

for i in range(len(T)):

    sprawdz(T[i])