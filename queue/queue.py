"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue? you need to implement the head and tail of the linked list when using an array you don't.
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # 1
        # self.storage = []
        # 2
        self.storage = LinkedList()

    def __len__(self):
        # 1
        # return len(self.storage)
        # 2
        return self.size

    def enqueue(self, value):
        # 1
        # self.storage.insert(0, value)
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):

        # 1
        # if len(self.storage) == 0:
        #     return None
        # else:
        #     return self.storage.pop()
        if self.storage.tail:
            self.size -= 1
            return self.storage.remove_head()
