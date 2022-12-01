suma = int(input())

a = 1
b = 1

ciag = []

while a < suma:

    if len(ciag) > 1:
        ciag.append(ciag[-1] + a)
    else:
        ciag.append(a)

    b = a + b
    a = b - a
for el in ciag:
    if el == suma:
        print("istnieje")

for i in range(len(ciag)):

    for j in range(i):

        if(ciag[i] - ciag[j]) == suma:
            print("istnieje")


#print(ciag)