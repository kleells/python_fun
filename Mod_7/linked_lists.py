# Create a class for the nodes called Node. Each node will contain two
# fields: the data and the reference link. For now, set the reference
# to None at the start. This will set the reference to an empty value
# unless otherwise specified.

    # Use the init method to initialize the attributes of the class.
    # We want data and reference fields to be created for each node.

    # Don't forget to use the self keyword to bind the attributes
    # with the given arguments. This allows us to access the
    # attributes and methods of the class in Python.

class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

# Create a node with a value of 5 (leave the reference as is).
# Print the node's data to check that it works.

node1 = Node(5)
print(node1.data)
print(node1.reference)

node2 = Node(11)
node1.reference = node2
print(node1.reference)
# OUTPUT: <__main__.Node object at 0x10fa7bee0>


# Create a class for the linked list called LinkedList. This class
# stores the head of the list. Initially we want to create an empty
# linked list by setting head equal to None.

# Use the init method to initialize the attributes of the class.
# We want a head field to be created in the linked list.

# Don't forget to use the self keyword to bind the attributes with
# the given arguments.

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # traverse a linked list (define a method that will go through
    # and print the data of each node)

        # Define a method called print_linked_list() and write a
        # conditional statement that checks if the linked list
        # is empty. If it is, print a message saying, 'The linked
        # list is empty'

    def print_linked_list(self):
        if self.head == None:
            print("The linked list is empty")
        
        # If the linked list is not empty, print each node's data and
        # use the reference to access each node.

            # Set a variable called c_node (representing the current
            # node) equal to self.head. This is not necessary, but
            # will help. For example, c_node.data will be the current
            # node's data. This is easier to read and type than
            # self.head.data.

            # Use a while loop since we know the end condition. When
            # the reference is equal to 'None', stop the function.
            # In other words, we want to print the node's data and set
            # the current node equal to the reference link to go to
            # the next node until the reference link is 'None'.

            # In the while loop, print the current node's data. Also,
            # set c_node equal to c_node.reference. We do this so the
            # reference of the node becomes the new current node.
            # This allows us to access each node in the linked list.

        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference

    # Define a method to add a node to the beginning of a linked list.

        # Set a variable called n_node that will store the data from
        # each new node created using the Node class (shown in green).
        
        # Set the reference to the next node as the current head.
        # In other words, set the reference as pointing to the
        # current first node (shown in blue).

        # Set the current head as the new node. In other words,
        # set self.head equal to the n_node to make the new
        # node the head/first node (shown in red).

    def add_to_start(self, data):
        n_node = Node(data)
        n_node.reference = self.head
        self.head = n_node

linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()
