class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

root = Node(10)
root.left = Node(2)
root.right = Node(12)

def wypisz(p):

    if p!=None:
        print(p.val)
        wypisz(p.left)
        wypisz(p.right)

#wypisz(root)

#LKP
#LKP
#KLP
#KPL
#PLK
#PKL