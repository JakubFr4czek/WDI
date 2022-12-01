
n = int(input()) #n - cyfrowe


for i in range(10**(n-1), 10**(n)):

    liczba = i
    suma = 0

    while liczba > 0:
        
        suma += (liczba%10)**n
        liczba//=10
    #print(liczba, " ", suma)

    if suma == i:
        print(i)

