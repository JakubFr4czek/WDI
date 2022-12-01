from math import sqrt

eps = 10e-7

a = sqrt(0.5)

result = a
result_before = 1

while abs(result - result_before) > eps:
    result_before = result

    a = sqrt(0.5 + (0.5*a))
    result *=a

# b = 2/pi
print(2/result)