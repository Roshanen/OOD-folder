class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while (cur.next != None):
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if (self.head == None):
            self.head = Node(item)
        else:
            cur = self.head
            while (cur.next != None):
                cur = cur.next
            cur.next = Node(item)

    def addHead(self, item):
        if (self.head == None):
            self.head = Node(item)
        else:
            p = Node(item)
            p.next = self.head
            self.head = p

    def search(self, item):
        if (self.head == None):
            return "Not Found"
        else:
            cur = self.head
            while (cur != None):
                if (cur.value == item):
                    return "Found"
                cur = cur.next
            return "Not Found"

    def index(self, item):
        if (self.head == None):
            return -1
        else:
            cur = self.head
            index = 0
            while (cur != None):
                if (cur.value == item):
                    return index
                cur = cur.next
                index += 1
            return -1

    def size(self):
        if (self.head == None):
            return 0
        else:
            cur = self.head
            index = 1
            while (cur.next != None):
                index += 1
                cur = cur.next
            return index

    def pop(self, pos):
        if (self.head == None):
            return "Out of Range"
        else:
            cur = self.head
            prev = None
            index = 0
            while (cur != None):
                if (index == pos):
                    if (prev != None):
                        prev.next = cur.next
                    else:
                        self.head = self.head.next
                    return "Success"
                index += 1
                prev = cur
                cur = cur.next
            return "Out of Range"

L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)
