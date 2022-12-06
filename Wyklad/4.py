from collections import deque

stack = deque()

stack.append(1)
stack.append(2)
stack.append(3)

print(stack)

print(stack.pop())
stack.pop()
stack.pop()

print(stack)

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(queue.popleft())