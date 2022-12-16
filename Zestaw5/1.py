#kalkulator na ulamkach zwyklych

def nwd(a, b):

    while b > 0:

        a,b = b, a%b

    return a

def shortenTheFraction():

    l = int(input("Podaj Licznik: "))
    m = int(input("Podaj Mianownik: "))

    n = nwd(l, m)

    print(l//n, m//n)

def menu():

    print("Wybierz 1, aby dodac ulamki: ")
    print("Wybierz 2, aby odjac ulamki: ")
    print("Wybierz 3, aby pomnozyc ulamki: ")
    print("Wybierz 4, aby podzielic ulakmi: ")
    print("Wybierz 5, aby podniesc ulamek do potegi: ")
    print("Wybierz 6, aby skrocic ulamek: ")

    choice = int(input())

    match choice:
        case 1:
            add(True)
        case 2:
            add(False)
        case 3:
            multiply(True)
        case 4:
            multiply(False)
        case 5:
            raiseToThePower()
        case 6:
            shortenTheFraction()












menu()