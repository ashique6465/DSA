class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
#create list
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
#print list
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    #append list
    def append(self,value):
        new_node = Node(value) 
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1
        return True
    #pop list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
#prepend
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
#pop first item
    def popFirst(self):
        if self.length == 0:
            return None
        
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:  
            self.tail = None
        return temp.value
    
    # get 
    def get(self,index):
        if index < 0 or index >= self.length:
            return Node

        temp = self.head
        for _ in range(index):
            temp = temp.next  
        return temp
    
    #set
    def set_value(self,index,value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    #insert
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node  = Node(value)
        temp = self.get(index-1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    #remove
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        if index ==0:
            return self.popFirst()
        if index == self.length - 1:
            return self.pop() 
        prev = self.get(index-1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
#reverse 
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


        

list1 = LinkedList(1)
list1.append(2)
list1.append(3)
list1.append(4)
# list1.set_value(1,4)
# list1.insert(1,1)
# list1.remove(2)
list1.reverse()
list1.printList()


# print(list1.get(2))
# list1.prepend(2)
#
# list1.printList()
# print(list1.pop())
# print(list1.pop())
# print(list1.pop())


        
# my_linked_list = LinkedList(4)
# print(my_linked_list)
# print("Head: ",my_linked_list.head.value)
# print("Tail:",my_linked_list.tail.value)
# print("Length: ",my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

                                                                                                                    