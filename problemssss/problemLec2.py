class LL:
    def __init__(self, x):
        self.item = x
        self.next = None


class LLSeq:
    def __init__(self):
        self.head = None
        self.size = 0

    def create_ll(self, X):
        for a in reversed(X):
            self.ll_append(a)

    def ll_append(self, x):
        node = LL(x)
        node.next = self.head
        self.head = node
        self.size += 1

    def stuff(self):
        tail = self.head
        target = self.head
        while tail.next:
            tail = tail.next
        while target and target.item != 3:
            target = target.next
        tail.next = target
        return self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next


ll = LLSeq()
ll.create_ll([1, 2, 3, 4, 5, 6, 7])
print(list(ll))
ll_round = ll.stuff()


def pro(head):
    slow = fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        non_cycle = 0
        first = head
        while first:
            non_cycle += 1
            first = first.next
        return non_cycle

    cycle_len = 1
    fast = fast.next
    while fast != slow:
        fast = fast.next
        cycle_len += 1

    fount = head
    non_cycle = 0
    while fount != slow:
        fount = fount.next
        slow = slow.next
        non_cycle += 1

    return non_cycle + cycle_len


print(pro(ll_round))
