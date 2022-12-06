#ciufa

#fifo (first in first out)

#init
#empty
#put
#get

class Node():

    def __init__(self,value):
        self.val = value
        self.next = None

class Queue():

    def __init__(self):
        self.head = None

    def empty(self):

        if self.head == None:
            return True
        return False
    
    def put(self, value):

        data = Node(value)

        if self.head != None:

            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = data
        else:
            self.head = data


    def get(self):

        if self.head != None:

            a = self.head.val

            self.head = self.head.next

            return a

        return None

q = Queue()

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())