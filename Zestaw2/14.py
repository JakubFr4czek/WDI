from math import log10

def dec_to_bin(n):

    result = 0

    a = 0

    while n > 0:
        if n%2 == 0:
            count+=1
        result += (n%2)*10**a
        a+=1
        n//=2

    
    return result


x = int(input())
y = int(input())

liczba_len = int(len(str(x))) + int(len(str(y)))

for i in range(2**(liczba_len - 1), 2**(liczba_len)):

    print(dec_to_bin(i))

    #eval(x,y,dec_to_bin(i))