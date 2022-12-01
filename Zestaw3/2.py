import math

a = int(input())
b = int(input())

counter = [0 for i in range(10)] #do zliczania liczb od 0 do 9

a_length = int(math.log10(a) + 1)
b_length = int(math.log10(b) + 1)

if a_length != b_length:
    print("nie prawda!!! AAAAAAAAAAAAA")
    exit()

for i in range(a_length):

    counter[a%10] += 1
    a//=10

    counter[b%10] -= 1
    b//=10

for i in range(10):

    if counter[i] != 0:
        print(":((((((")
        exit()
print("TAK OWSZEM KURWAAAAA TAAK, MATKO TAK SA TE SAME AAAAAA!!!!!")

    