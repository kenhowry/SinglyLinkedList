class SLLIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if not self.current is None:
            return_value = self.current.value
            self.current = self.current.next
            return return_value
        else:
            raise StopIteration("No more values.")
    
    def __iter__(self):
        return self
        
class Node:
    def __init__(self, v, n):
        self.value = v
        self.next = n
    
    def __eq__(self, other):
        return self.value == other.value

    def __str__(self):
        return str(self.value)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __iter__(self):
        return SLLIterator(self.head)
    
    #returns the number of nodes in the list
    def get_size(self):
        return self.size

    #returns bool depending on whether the list has no nodes, or contains nodes
    def is_empty(self):
        return self.head is None

    #returns a str, representing the values of all items in the list
    def __str__(self):
        #if the list is empty
        if self.head is None:
            return '[]'
        
        result = '['

        #create a reference to the head and advance it instead of head
        #advancing head removes nodes

        temp_node = self.head

        while temp_node.next is not None:
            result += str(temp_node) + " "
            temp_node = temp_node.next
        
        return result + str(temp_node) + ']'
    
    #inserts a new node with the parameter as the new first element
    def add_first(self, value):    
        #step 1: create a node with value and the head as next ref
        new_node = Node(value, self.head)

        #step 2: make head point to new node
        self.head = new_node

        #step 3:incremenet size
        self.size += 1

    #appends a new node with the parameters as the last element
    def add_last(self, value):
        #step 1: create a node with value and None as ref
        new_node = Node(value, None)

        #step 2: make the old end point to the new end
            #special case: the list is initially empty

        if self.head is None:
            self.head = new_node

        else:
            temp_node = self.head

            while temp_node.next is not None:
                temp_node = temp_node.next
            
            temp_node.next = new_node

        #step 3: increment size
        self.size += 1
        
    #remove the first node, return its associated value
    def remove_first(self):
        if self.head is None:
            raise ValueError("List is empty.")
        
        #step 1: store the head value
        return_value = self.head.value

        #step 2: advance the head reference
        self.head = self.head.next

        #step 3: decrement size
        self.size -=1

        return return_value
    
    #remove the last node, return its associated value
    def remove_last(self):
        #if the list is empty, calling the method should raise an error
        if self.head is None:
            raise ValueError("List is empty.")          

        return_value = None

        #if the list has only one element, return the value of that element and set the head to null
        if self.head.next is None:
                return_value = self.head.value
                self.head = None
        else: 
            temp_node = self.head
            while temp_node.next.next is not None:
                temp_node = temp_node.next          

            return_value = temp_node.next.value
            temp_node.next = None

        self.size -= 1   

        return return_value
    
    #return the value stored at the given index position
    def get(self, index):
        #IndexError
        if index >= self.size:
            raise IndexError("Index is out of range.")
        
        #step 1: create variable to track the index
        idx_value = 0

        #step 2: create a second variable to traverse the list 
        temp_node = self.head

        #step 3: traverse list until the given index and return value
        while True:
            if idx_value == index:
                return temp_node.value
            temp_node = temp_node.next
            idx_value += 1
    
    #removes the node at index [i] from the list, returning its associated value
    def remove_at_index(self, index: int):
        #ValueError
        if self.head is None:
            raise ValueError("List is empty.")  
        
        #IndexError
        if index >= self.size:
            raise IndexError("Index is out of range.")
        
        #decrement size
        self.size -= 1
       
        #step 1: create variables to track the index and traverse list
        idx_value = 0
        current_node = self.head

        #step 2: traverse list until the given index and deletes node
        while idx_value <= index:
            node_before = current_node
            current_node = current_node.next
            idx_value += 1
            if index == 0:
                deleted_value = self.head.value
                self.head = self.head.next
                return deleted_value
            elif idx_value == index:
                deleted_value = current_node.value
                node_before.next = current_node.next
                return deleted_value
    
    #finds the minimum value in the list and returns the value
    def find_minimum(self):
        #list is empty; raising a ValueError
        if self.head is None:
            raise ValueError("List is empty.")
        
        #creating variable
        min_value = None

        #if the list has only one element, return the value of that element
        if self.head.next is None:
            min_value = self.head.value

        else:
        #step 1: store the head value as starting value
            temp_node = self.head
            min_value = self.head.value

        #step 2: transverse the list comparing the values and changing the value of the variable accordingly
            while temp_node is not None:
                if min_value > temp_node.value:
                    min_value = temp_node.value
                
                #increment
                temp_node = temp_node.next

        #step 3: return the minimum value
        print(min_value)

    def rotate(self, n):
        """
        takes int n as a parameter 
        the new head of the list should point 
        to the index n element of the original list
        if n is an invalid value; raise IndexError
        """

#main code block
a_list = SinglyLinkedList()

a_list.add_first(1)
a_list.add_last(2)
a_list.add_first(3)
a_list.add_last(4)
print(a_list)

print(a_list.remove_at_index(0))
print(a_list)

for value in a_list:
    print(value)
