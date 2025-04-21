class LinkedListNode:
    def __init__(self, x):  # O(1)
        self.item = x       # property
        self.next = None    # the after property pointer, type -> class

    def later_node(self, i):    # using get_at/ set_at  O(i)
        if i == 0:
            return self
        assert self.next    # ensures we don’t go out of bound
        return self.next.later_node(i - 1)  # recursive


class LinkedListSeq:
    def __init__(self):     # O(1)
        self.head = None    # type -> class(LinkedListNode), it save all the nodes of LinkedList
        self.size = 0

    def __len__(self):      # O(1)
        return self.size

    def __iter__(self):     # O(n) iter_seq
        node = self.head
        while node:
            yield node.item
            node = node.next

    def build(self, X):     # O(n)
        for a in reversed(X):   # (Begin) 3(head) | 2(head) -> 3 | 1(head) -> 2 -> 3 (End)
            self.insert_first(a)

    def insert_first(self, x):  # O(1)
        new_node = LinkedListNode(x)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def get_at(self, i):        # O(i)
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):     # O(i)
        node = self.head.later_node(i)
        node.item = x
        return node.item

    def delete_first(self):     # O(1)
        x = self.head.item
        self.head = self.head.next
        self.size -= 1
        return x

    def insert_at(self, i, x):     # O(i)
        if i == 0:
            self.insert_first(x)
            return
        new_node = LinkedListNode(x)
        node = self.head.later_node(i-1)    # find origin LL, index i-1
        new_node.next = node.next           # put origin LL.next (index i ) to next_node.next,
                                            # now is new_node + ori LL (index i and after)
        node.next = new_node                # combine
        self.size += 1

    def delete_at(self, i):         # O(i)
        if i == 0:
            self.delete_first()
        node = self.head.later_node(i-1)
        x = node.next.item                  # node is type(head) -> class
        node.next = node.next.next
        self.size -= 1
        return x

    def insert_last(self, x):       # O(n)
        self.insert_at(len(self), x)

    def delete_last(self):          # O(n)
        return self.delete_at(len(self) - 1)


LL = LinkedListSeq()
LL.build([1, 2, 3])
print(list(LL))
print(LL.get_at(1))
print(LL.set_at(1, 69), list(LL))
