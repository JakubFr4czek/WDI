from math import log10

"""
Kolokwium 1b
25 listopada 2021
Zadanie 2

Liczbę nazywamy iloczynowo-pierwszą jeżeli iloczyn jej cyfr w systemie o podstawie b jest liczbą
pierwszą. Na przykład:
13 jest liczbą iloczynowo-pierwszą w systemie dziesiętnym, bo 1 · 3 = 3.
16 jest liczbą iloczynowo-pierwszą w systemie trójkowym, bo 16 base 10 = 121 base 3, 1 · 2 · 1 = 2.

W liczbie naturalnej możemy dokonywać rotacji jej cyfr, np. 1428, 4281, 2814, 8142 albo 209, 092,
920.
Proszę napisać funkcję, która dla danej liczby naturalnej N, zwróci najmniejszą podstawę systemu (z
zakresu 2-16) w którym przynajmniej jedna z rotowanych liczb jest iloczynowo-pierwsza albo wartość
None, gdy taka podstawa nie istnieje.
"""

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def rotate(n):
    n_length = int(log10(n)) + 1               # 4281
    first_digit = n // (10 ** (n_length - 1))  # first_digit = 4
    n %= (10 ** (n_length - 1))                # 4281 -> 281
    n *= 10                                    # 281 -> 2810
    n += first_digit                           # 2810 -> 2814
    return n

def zad2_1(n):
    n_length = int(log10(n)) + 1
    for base in range(2, 17):
        for _ in range(n_length):
            n = rotate(n)
            n_copy = n
            product = 1
            while n_copy > 0:
                digit = n_copy % base
                n_copy //= base
                product *= digit
            if is_prime(product):
                return base
    return None

def zad2_2(n):
    n_length = int(log10(n)) + 1
    for base in range(2, 17):
        for _ in range(n_length):
            n = rotate(n)
            n_copy = n
            has_prime = False
            while n_copy > 0:
                digit = n_copy % base
                n_copy //= base
                if digit != 1:
                    if digit in (2, 3, 5, 7, 11, 13) and not has_prime:
                        has_prime = True
                    else:
                        break
            else:
                return base
    return None

print(zad2_2(16))