class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)

    def __str__(self):
        s = ""
        current = self
        while current != None:
            s += f"{current.value} -> "
            current = current.next
        return s

    def reverse(self):

        cur = self
        new = cur.next
        cur.next = None
        while new != None:
            prev = cur
            cur = new
            new = cur.next
            cur.next = prev

        return cur


root = Node(3)
cur = root
cur.add(4)
cur = cur.next
cur.add(5)
cur = cur.next
cur.add(6)
cur = cur.next

cur = root
while cur:
    print(cur.value)
    cur = cur.next
print(root)
print("-----")
cur = root.reverse()
print(cur)
# print(root.reverse())
while cur:
    print(cur.value)
    cur = cur.next
