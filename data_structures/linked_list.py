#   ---------        ---------
#   |       |  .next |       |
#   |   1   |   ==>  |   2   |
#   |       |        |       |
#   ---------        ---------

# Linked List is a data structure made out of nodes, where each node points to next, and last points to null.


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next != None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def get(self, index):
        if index >= self.length():
            print("Error")
        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node
            current_index += 1

    def erase(self, index):
        if index >= self.length():
            print("Error")
        current_index = 0
        current_node = self.head
        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index += 1


my_list = Linked_list()
for i in range(100):
    my_list.append(i)
my_list.erase(2)
my_list.display()
