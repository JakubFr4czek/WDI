#stosu

#lifo (last in first out)

#init
#empty
#push
#pop (top)


class Node():

    def __init__(self,value):
        self.val = value
        self.next = None


class Stack():

    def __init__(self):
        self.head = None

    def empty(self):

        if self.head == None:
            return True
        return False
    
    def push(self, value):

        temp = Node(value)

        if self.head != None:
            temp.next = self.head

        self.head = temp


    def pop(self):

        if self.head != None:

            a = self.head.val

            self.head = self.head.next

            return a

        return None

s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.empty())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.empty())
