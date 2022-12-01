
liczba = int(input())

liczba_len = len(str(liczba))

def dec_to_bin(liczba):

    result = 0
    i = 0

    while liczba > 0:
        
        result += (liczba % 2) * 10**i

        i+=1
        liczba//=2 

    return result



count = 0
for x in range(1,2**liczba_len):
    z = liczba
    mask = dec_to_bin(x)
    result = 0
    a = 0
    for i in range(liczba_len):
        if mask %10 == 1:
            result += (z%10)*(10**a)
            a+=1
        mask//=10
        z//=10

    if result %7==0:
        count+=1
    print(count)