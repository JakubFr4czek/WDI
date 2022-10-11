
n = int(input())


b = 1
end = 0
while end == 0:

    for a in range(1,b+1):

        c = a
        d = b
        #if a == 1 and b == 2021:
            #print("a: ", a)
            #print("b: ", b)

        while c < n:

            d = c+d
            c = d-c

        if(c == n):
            print("a:",a)
            print("b:",b)
            end = 1

    b += 1

