suma = int(input())

ciag = [int(1)]

a = 1
b = 1

i = 0 #iterator po tablicy ciag

while a < suma:

    b = a + b
    a = b - a

    ciag.append(ciag[i] + a)
    i+=1


for i in range(len(ciag)):

    if ciag[i] == suma:
        print("TAK")

    for j in range(i):
        
        if ciag[i] - ciag[j] == suma:
            print("TAK")
            
print(ciag)