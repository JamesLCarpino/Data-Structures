"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        # check if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # the new node becomes the head of our list
            new_node.next = self.head
            # set the current head's prev to the new node
            self.head.prev = new_node
            # set the new node's next to the current head
            # reassign self.head to point the new node
            self.head = new_node
            # needs to add one to the length for it because we are creating one new
            self.length = self.length + 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        if self.head is None:
            return None

        elif self.length == 1:
            current_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return current_head.value
        else:
            current_head = self.head
            self.head = current_head.value
            self.delete(current_head)
            self.length -= 1
            return current_head.value

        # if self.tail is None and self.head is None:
        #     return None
        # else:
        #     self.head.next = self.head
        #     self.delet

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        # check if the DLL is empty
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            # the new node becomes the tail of our list moving other one to the prev position
            new_node.prev = self.tail
            # set the current tail's prev to the new node
            self.tail.next = new_node
            # set the new node's next to the current tail
            # reassign self.head to point the new node
            self.tail = new_node
            # needs to add one to the length for it because we are creating one new
            self.length = self.length + 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        if self.tail is None:
            return None

        elif self.length == 1:
            current_tail = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return current_tail.value
        else:
            current_tail = self.tail
            self.tail = current_tail.value
            self.delete(current_tail)
            self.length -= 1
            return current_tail.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        # need to take node and reasign it to the head
        # takes in
        move_node = ListNode(node, None, None)
        self.head = move_node.insert_before(0)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        # need to take node and reasign it to the tail
        # move_node = ListNode(node)
        # if move_node == None or (move_node).next == None:
        #     return None

        # # initialize first and last pointers
        # first = move_node
        # last = move_node

        # while last.next != None:
        #     last = last.next

        # move_node = first.next
        # first.next = None

        # last.next = first
        # return move_node
        move_node = ListNode(node, None, None)
        self.head = move_node.insert_before(-1)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):
        # decriment the length
        self.length -= 1

        # if empty
        if not self.head and not self.tail:
            # error todo
            return
        # if head and tail
        if self.head == self.tail:
            # this means only one item in list
            # we dont need to look or mess with node, just get rid of pointers to head and tail
            self.head = None
            self.tail = None
        # if head
        elif self.head == node:
            self.head = self.head.next
            # delete method
            node.delete()
            # this gets rid of the node

        # if tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()

        # otherwise
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        pass
        if self.head is None:
            return None

        max_so_far = self.head.getValue()
        current = self.head.getNext()

        while current is not None:
            if current.getValue() > max_so_far:
                max_so_far = current.getValue()
            current = current.getNext()
        return max_so_far
