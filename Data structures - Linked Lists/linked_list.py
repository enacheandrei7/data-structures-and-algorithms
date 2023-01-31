"""
Implementation of linked lists in python
"""

class Node:
    """Creates the nodes of the Linked List"""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    """Creates the Linked List"""
    def __init__(self):
        self.head = None


    def insert_at_begining(self, data):
        """Insert node at the beginning the Linked List"""
        node = Node(data, self.head)
        self.head = node


    def insert_at_end(self, data):
        """Inserts node at the end of the Linked List"""
        if self.head is None:
            self.head = Node(data, None)
            return

        new_node = Node(data, None)

        itr = self.head
        while itr.next_node:
            itr = itr.next_node

        itr.next_node = new_node


    def remove_at_index(self, index):
        """Removes the element from index position"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next_node
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next_node = itr.next_node.next_node
                break
            itr = itr.next_node
            count += 1


    def insert_at(self, index, data):
        """Adds the element to index position"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next_node)
                itr.next_node = node
                break
            itr = itr.next_node
            count += 1


    def create_linked_list_from_list(self, data_list):
        """Creates Linked List from list of elements"""
        self.head = None
        for elem in data_list:
            self.insert_at_end(elem)


    def show_list(self):
        """Shows the Linked List"""
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        li_str = ''

        while itr:
            li_str += str(itr.data) + ' --> '
            itr = itr.next_node

        print(li_str)


    def get_length(self):
        """Gets the length of the Linked List"""
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next_node
        return count


li = LinkedList()
# li.insert_at_begining(5)
# li.insert_at_begining(89)
# li.insert_at_begining(11)
# li.insert_at_begining(22)
# li.insert_at_end(100)
li.create_linked_list_from_list(['Bibi', 'Marcu', 'Lilly', 'Tudor'])
li.show_list()
print('Length: ', li.get_length())
li.remove_at_index(2)
li.show_list()
li.insert_at(1, 'Fruru')
li.show_list()
