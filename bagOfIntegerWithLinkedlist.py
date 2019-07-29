'''
A bag is a container that holds a finite collection of like items in no particular order. Repeated /
duplicate items are allowed. Various operations can be performed on a bag.
You are to implement a bag of integers using a singly-linked list and a class definition IntBag.
Ans:
'''

class IntBag:
	
	# construct a bag
    class node:

        __slots__ = '_item', '_next'

        def __init__(self,item,next):
            self._item = item
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
	
	# determine the size of a bag. i.e. the current number of items in a bag
    def __len__(self):
        return self._size
	
	# determine whether or not a bag is empty
    def is_empty(self):
        return self._size == 0
	
	# add an item to a bag
    def add(self, element):
        oldNode = self._head
        self._head = self.node(element,oldNode)
        self._size += 1

	# determine whether or not a specified item is contained in a bag
    def search(self, searchElement):

        current = self._head

        while current != None:
            if current._item == searchElement:
                return "item found"

            current = current._next

        return "item not found"
	
	# determine the number of occurrences of a specified item in a bag
    def numberOfOccurrencesItem(self, searchElement):

        current = self._head
        count = 0

        while current != None:
            if current._item == searchElement:
                count += 1

            current = current._next

        return count
	
	# remove a specified item (i.e. one occurrence) from a bag
    def removeSpecifiedItem(self,rmveElement):

        if self.is_empty():
            return "list is empty"

        else:
            temp = self._head
            if temp._item == rmveElement:
                self._head = temp._next
                self._size -= 1

            else:
                previous = self._head
                curr = self._head._next

                while curr != None:
                    if curr._item == rmveElement:
                        previous._next = curr._next
                        self._size -= 1
                        break

                    previous = curr
                    curr = curr._next

	# remove all occurrences of a specified item from a bag
    def removeAllOccurrences(self,rmveElement):

        if self.is_empty():
            return "list is empty"

        else:
            temp = self._head
            while temp._next != None:
                if temp._item == rmveElement:
                    self._head = temp._next
                    temp = self._head
                    self._size -= 1
                else:
                    break

            previous = self._head
            curr = self._head._next

            while curr != None:
                if curr._item == rmveElement:
                    previous._next = curr._next
                    self._size -= 1
                else:
                    previous = curr
                curr = curr._next

	# print the contents of a bag
    def printAllItems(self):

        if self.is_empty():
            print("bag is empty")
        else:
            current = self._head
            while current != None:
                print(current._item)
                current = current._next

# Write a test program which simulates the use of a bag, making sure that you test all the operations
# and any special cases associated with the operations.
bag = IntBag()
bag.add(12)
bag.add(12)
bag.add(12)
bag.add(12)
bag.add(12)
bag.add(54)
bag.add(3)
bag.add(99)
bag.add(5)
bag.add(12)
bag.add(12)
bag.add(12)
print(bag._head)
print("print all")
bag.printAllItems()
print("length: ",bag.__len__())
print("___________________________________")
print("Remove specified item - 12 :")
bag.removeSpecifiedItem(12)
bag.printAllItems()
print("length: ",bag.__len__())
print("___________________________________")
print("Remove specified item - 12 :")
bag.removeSpecifiedItem(12)
bag.printAllItems()
print("length: ",bag.__len__())
print("___________________________________")
print("Number of occurences for 12 : ",bag.numberOfOccurrencesItem(12))
print("search for 12 : ",bag.search(12))
print("___________________________________")
print("Remove all occurence of specified item - 12 :")
bag.removeAllOccurrences(12)
bag.printAllItems()
print("length: ",bag.__len__())
print("___________________________________")
print("Number of occurences for 12 : ",bag.numberOfOccurrencesItem(12))
print("search for 12 : ",bag.search(12))
print("___________________________________")
print("Is bag empty: ",bag.is_empty())
print("length: ",bag.__len__())
print("___________________________________")
bag.removeSpecifiedItem(5)
bag.removeSpecifiedItem(99)
bag.removeSpecifiedItem(3)
bag.removeSpecifiedItem(54)
print("Is bag empty: ",bag.is_empty())
print("length: ",bag.__len__())
print("print all : ")
bag.printAllItems()
print("___________________________________")
