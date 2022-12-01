N = 11
T = [0,1,2,3,4,5,6,7,8,9,7]

pierwszy = 0
sumaEl = 0
sumaId = 0

maks = 0
dlCiagu = 1

for i in range(N - 1):

    if T[i] < T[i + 1]:
        dlCiagu += 1
        sumaEl += T[i]
        sumaId += i

        if sumaEl == sumaId:
            if dlCiagu > maks:
                    maks = dlCiagu
    else:

        sumaEl += T[i]
        sumaId += i

        if sumaEl == sumaId:
            if dlCiagu > maks:
                    maks = dlCiagu

        for j in range(pierwszy, i):
            dlCiagu -=1
            sumaEl -= T[j]
            sumaId -= j

            if sumaEl == sumaId:
                if dlCiagu > maks:
                    maks = dlCiagu

        sumaEl = 0
        sumaId = 0
        dlCiagu = 1
        pierwszy = i + 1

if T[N - 2] < T[N - 1]:
    sumaEl += T[N - 2]
    sumaId += N - 2

    if sumaEl == sumaId:
        if dlCiagu > maks:
                    maks = dlCiagu

print(maks)