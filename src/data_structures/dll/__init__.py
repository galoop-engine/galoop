
class Node:
    def __init__(self, next=None, prev=None, value=None):
        self.next = next
        self.prev = prev
        self.value = value

    def get_next(self):
        return self.next

    # [x] set_next ( _node_?<Node/> )
    #     [description]
    #         adds a 'next' refrence to this node with the given _node_ value
    #
    #     [time-complexity]
    #         O(1)

    def set_next(self, _node):
        self.next = _node

    def get_prev(self):
        return self.prev

    # [x] set_prev  ( _node_?<Node/> -> != None)
    #     [description]
    #         adds a 'prev' refrence to this node with the given _node_ value
    #
    #     [time-complexity]
    #         O(1)

    def set_prev(self, _node):
        self.prev = _node

    # [] set_value (_value_?<any/>)
    #     [description]
    #         sets this nodes value to the given _value_
    #
    #     [time-complexity]
    #         O(1)


    def set_value(self, _value):
        self.value = _value

    # [x] get_value  (_)
    #     [description]
    #         returns the value of this node
    #
    #     [time-complexity]
    #        O(1)

    def get_value(self):
        return self.value

    def __str__(self):
        _ = "previous: {self.prev.value},\nnext: {self.next.value},\nvalue: {self.value}".format(self=self)
        return _

"""[DLL]

    [] add_to_head
        [description]
            adds to the head of the list

        [time-complexity]
            O(n)

    [] remove_from_head
        [description]
           removes the head node refrence from the list,
           updating the the last refrences next node to be the new head node

        [time-complexity]
            O(n)

    [] add_to_tail
        [description]
            adds to the tail of the list

        [time-complexity]
            O(n)

    [] remove_from_tail
        [description]
            removes the tail node refrence from the list,
            updating the last refrences previous node to be the new tail node

        [time-complexity]
            O(n)

    [] tell us its length
        [description]
            gives the current length of the nodelist

        [time-complexity]
            O(1)

"""
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
