count_max = 0
solution = 2
for i in range(2, 10000 + 1):

    count = 0
    
    
    a = i
    while a != 1:
        a = (a%2)*(3*a + 1) + (1 - a%2)*a/2
        count+=1

    if count > count_max:
        count_max = count
        solution = i
    
print(solution)
    