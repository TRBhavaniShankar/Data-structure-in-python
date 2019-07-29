'''
Design a stack ADT using a single queue as an instance variable, and only constant additional local
memory within the method bodies. What is the running time of the push(), pop(), and top() methods
for your design? Implement your modified stack ADT in Python, including tester code to test all its
methods.

Ans :
1. create a simple Queue ADT
2. use the queue as an instance variable in the stack ADT
3. while pushing the data into stack we follow the below,
    enqueue the data in the queue,
    if the queue already contain an element
        dequeue the element keep it in a temp variable and enqueue the element back to the same queue
        thus by doing this we will have the stack structure(i.e., LIFO)

    run time for this will we O(n) because we need to denqueue all the elements and enqueue back to the same queue

4. pop operation as normal addition of the new node to the queue, thus the running time for pop is O(1)
5. running time for top function : as the queue is already in the stack structure we can just return the first element from the
    queue, thus the running time is O(1)
'''

#Queue ADT
class Queue:

    def __init__(self):
        self.items = []
        self.size = 0

	#queue length
    def _len(self):
        return self.size
	
	#check if queue is empty
    def is_empty(self):
        return self.size == 0
	
	#enqueue the queue
    def enqueue(self, data):
        self.items.append(data)
        self.size += 1
	
	#dequeue from the queue
    def dequeue(self):
        self.size -= 1
        return self.items.pop(0)

#Implement your modified stack ADT in Python
class StackQ:
	
	#use Queue as an instance variable
    def __init__(self):
        self.q = Queue()
	
	#ize of the stack
    def _size(self):
        return self.q._len()
	
	#check if stack is empty
    def is_empty(self):
        return self.q.is_empty()
	
	#push value into stack
    def push(self,element):
        self.q.enqueue(element)
        for _ in range(self.q.size - 1):
            deq = self.q.dequeue()
            self.q.enqueue(deq)
	
	#pop the last element entered from stack
    def pop(self):
        if self.is_empty():
            return "No elements in the stack to pop"
        return self.q.dequeue()

	#return the last element entered the stack
    def top(self):
        if self.is_empty():
            return "No elements in the stack"
        return self.q.items[0]

# including tester code to test all its methods.
stk = StackQ()
stk.push(5)
stk.push(2)
stk.push(0)
stk.push(1)

print("is stack empty : ",stk.is_empty())
print("Length of the stack : ", stk._size())

print(stk.pop())
print(stk.top())
print(stk.pop())
print(stk.pop())
print(stk.top())
print(stk.pop())
print(stk.pop())
print(stk.top())

print("is stack empty : ",stk.is_empty())
