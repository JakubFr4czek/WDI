from tkinter import X


numer_biezacego_roku = int(input())


def find(x,y): 

    

    for i  in range(x, y+1):

        a = i
        b = y

        while a <= numer_biezacego_roku:

            if a == numer_biezacego_roku:
                print("x: ",x,"y: ", y)
                return True

            b = a + b
            a = b - a

        
    return False



y = 1

while find(1,y) == False:
    y+=1