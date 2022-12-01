from random import randint

for N in range(20,41):

    T = [ randint(1,365) for i in range(N)]

    prob = 0

    for i in range(N):

        for j in range(N):

            if i != j and T[i] == T[j]:
                prob += 1

    print("Piks mówi: ", prob, N, prob/N)