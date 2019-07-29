'''
Suppose that two stacks of positive integers are needed for a project. Each stack is to contain
integers that are less than or equal to 500. One stack is to contain even integers; the other stack is to
contain odd integers. Also, the total number of values in the combined stacks at any given time will
not exceed 200.

Design a way to implement both stacks in one 1-D array.

Ans:
1. Create the even array from the beginning and the odd array from the end of the same array.
2. Initially let,
       even array has [0:0] of one main array
       Odd array has [max size of the array : max size of the array]
3. Before putting the value into the even array increment the array top by one i.e., [0:1]
   Before putting the value into the odd array decrement the array top by one i.e., [max size -1 : max size]
'''


# Write a Python class definition(s) for the double stack representation designed previously.
# Include the following operations:
# ◦ isEmpty (for each stack)
# ◦ size (for each stack)
# ◦ push (insert an integer onto the correct stack depending on whether it is even or odd)
# ◦ pop (for each stack)
# ◦ top (for each stack)
# Ans:
class Stack:

    max = 200
    array = []
    evenTop = 0
    oddTop = max
    evenStack = array[0:evenTop]
    oddStack = array[oddTop:max]

    # returns size of even array stack
    def evenSize(self):
        return self.evenTop

    # returns size of odd array
    def oddSize(self):
        return self.max - self.oddTop -1

    # check if the array stack is empty or not
    def isEmptyEven(self):
        if len(self.evenStack) == 0:
            return True
        return False

    # check if the array stack is empty or not
    def isEmptyodd(self):
        if len(self.oddStack) == 0:
            return True
        return False

    # push only even value to the array stack
    def evenPush(self, n):
        if n > 500:
            print("cannot insert value which is more than 500!")

        else:
            if n % 2 == 0:
                if self.evenTop == self.oddTop:
                    print("evenStack is full")

                else:
                    self.evenTop += 1
                    self.evenStack.append(n)

            else:
                print("cannot push odd number to even stack")

    # push only odd value to the array stack
    def oddPush(self, n):
        if n > 500:
            print("cannot insert value which is more than 500!")

        else:
            if n % 2 == 1:
                if self.evenTop == self.oddTop:
                    print("oddStack is full")

                else:
                    self.oddTop -= 1
                    self.oddStack.append(n)

            else:
                print("cannot push even number to odd stack")

    # pop even value from the array stack
    def evenPop(self):
        if self.isEmptyEven() == True:
            return "no elements to pop from evenStack. evenStack is empty"

        else:
            evenval = self.evenStack[len(self.evenStack) - 1]
            self.evenStack.remove(self.evenStack[len(self.evenStack) - 1])
            self.evenTop -= 1
            return evenval

    # pop odd value from the array stack
    def oddPop(self):
        if self.isEmptyodd() == True:
            return "no elements to pop from oddStack. oddStack is empty"

        else:
            oddval = self.oddStack[len(self.oddStack) - 1]
            self.oddStack.remove(self.oddStack[len(self.oddStack) - 1])
            self.oddTop += 1
            return oddval

    # returns the value of the top of the array stack
    def top_evenStack(self):
        if self.isEmptyEven():
            return "evenStack is empty"
        return self.evenStack[len(self.evenStack) - 1]

    # returns the value of the top of the array stack
    def top_oddStack(self):
        if self.isEmptyodd():
            return "oddStack is empty"
        return self.oddStack[len(self.oddStack) - 1]


# Fully test all the stack operations in a Python main program.
stk = Stack()
print("----------------------------------------------------")
print("when pushing odd data in to even stack : ")
stk.evenPush(13)
print("----------------------------------------------------")
print("when pushing even data in to odd stack : ")
stk.oddPush(12)
print("----------------------------------------------------")
stk.evenPush(222)
stk.evenPush(210)
stk.evenPush(350)
stk.evenPush(352)
stk.evenPush(354)
stk.evenPush(366)
stk.evenPush(550)
print("----------------------------------------------------")
for i in range(210):
    if i % 2 == 0:
        stk.evenPush(i)
    else:
        stk.oddPush(i)
print("----------------------------------------------------")
print(stk.oddStack)
print(stk.evenStack)
print("top even : ", stk.top_evenStack())
print("top odd : ", stk.top_oddStack())
print("-------------1----------------")
print("pop odd : ", stk.oddPop())
print("pop even : ", stk.evenPop())
print(stk.oddStack)
print(stk.evenStack)
print("top even : ", stk.top_evenStack())
print("top odd : ", stk.top_oddStack())
print("-------------2----------------")
print(stk.oddStack)
print(stk.evenStack)
print("top odd : ", stk.top_oddStack())
print("top even : ", stk.top_evenStack())
print(stk.isEmptyEven())
print(stk.isEmptyodd())
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print("-------------3----------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop odd : ", stk.oddPop())
print("pop even : ", stk.evenPop())

print("--------------4---------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop odd : ", stk.oddPop())
print("pop even : ", stk.evenPop())

print("-------------5----------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop even : ", stk.evenPop())
print("pop odd : ", stk.oddPop())
print("--------------6---------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop even : ", stk.evenPop())
print("pop odd : ", stk.oddPop())

print("-------------7----------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop even : ", stk.evenPop())
print("pop odd : ", stk.oddPop())

print("------------8-----------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop even : ", stk.evenPop())
print("pop odd : ", stk.oddPop())
print("top odd : ", stk.top_oddStack())
print("top even : ", stk.top_evenStack())
print("-------------9----------------")
print("even size : ", stk.evenSize())
print("odd size : ", stk.oddSize())
print(stk.oddStack)
print(stk.evenStack)
print("pop even : ", stk.evenPop())
print("pop odd : ", stk.oddPop())
print("top odd : ", stk.top_oddStack())
print("top even : ", stk.top_evenStack())
print("--------------------------------------")
for i in range(201):
    if i == 0:
        continue
    else:
        if i % 2 == 1:
            print(stk.oddPop())
        else:
            print(stk.evenPop())
