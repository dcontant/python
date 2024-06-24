class Node:
    def __init__(self, val = None, nextNode = None):
        self.val  = val
        self.nextNode = nextNode

class LinkedList:
    
    def __init__(self, head: Node = None) -> None:
        self.head = head

    def get(self, index: int) -> int:
        i = 0
        cur = self.head
        while cur:
            if i < index:
                cur = cur.nextNode
                i += 1
            else:
                return cur.val
        return -1
        
    def insertHead(self, val: int) -> None:
        newHead = Node(val = val, nextNode = self.head)
        self.head = newHead
        
    def insertTail(self, val: int) -> None:
        previous = cur = self.head
        if cur == None: 
            self.head = Node(val)
            return
        while cur:
            previous = cur
            cur = cur.nextNode
        previous.nextNode = Node(val = val, nextNode = None)

    def NodesFromList(self, values: list[int]) -> None:
        if not self.head:
            self.head = Node(values[0]) 
        cur = self.head
        while cur.nextNode:
            cur = cur.nextNode
        for val in values[1:]:
            newNode = Node(val)
            cur.nextNode = newNode
            cur = newNode

    def remove(self, index):
        if index < 0:
            print("Index out of range")
            return False
        if index == 0:
            if self.head:
                self.head = self.head.nextNode
                return True
            else:
                print("List is empty")
                return False
        current = self.head
        prev = None
        count = 0
        while current and count != index:
            prev = current
            current = current.nextNode
            count += 1
        if current is None:
            print("Index out of range")
            return False
        prev.nextNode = current.nextNode
        return True

    def getValues(self) -> list[int]:
        values = []
        cur = self.head
        while cur:
            values.append(cur.val)
            cur = cur.nextNode
        return values
    
    def reverseList(self):
        prev = None
        current = self.head
        while current:
            next_node = current.nextNode
            current.nextNode = prev
            prev = current
            current = next_node
        self.head = prev
        

#########################################################
print()       
#[empty LinkdedList, [insertHead, 1], [insertTail, 2],[ insertHead, 0], [remove, 1]]


testList = LinkedList()
assert testList.getValues() == []

testList.insertHead(1)
assert testList.getValues() == [1]

testList.insertTail(2)
assert testList.getValues() == [1, 2]

testList.insertHead(0)
assert testList.getValues() == [0, 1, 2]

testList.remove(1)
assert testList.getValues() == [0, 2]
print()



#########################################################

# input [empty LinkdedList, "insertHead", 1, "remove", 0]

testList = LinkedList()
assert testList.getValues() == []
testList.insertHead(1)
assert testList.getValues() == [1]
testList.remove(0)
assert testList.getValues() == []



#########################################################
#[empty LinkdedList [insertHead, 1], [insertTail, 2],[ insertHead, 0], [remove, 2], [remove, 0]]
print()

testList = LinkedList()
assert testList.getValues() == []

testList.insertHead(1)
assert testList.getValues() == [1]

testList.insertTail(2)
assert testList.getValues() == [1, 2]

testList.insertHead(0)
assert testList.getValues() == [0, 1, 2]

testList.remove(2)
assert testList.getValues() == [0, 1]

testList.remove(0)
assert testList.getValues() == [1]
print()

#########################################################
#[empty LinkedList, "insertTail", 1, "insertTail", 2, "get", 1, "remove", 1, "insertTail", 2, "get", 1, "get", 0]

testList = LinkedList()
assert testList.getValues() == []

testList.insertTail(1)
assert testList.getValues() == [1]

testList.insertTail(2)
assert testList.getValues() == [1, 2]

assert testList.get(1) == 2
assert testList.getValues() == [1, 2]

testList.remove(1)
assert testList.getValues() == [1]

testList.insertTail(2)
assert testList.getValues() == [1, 2]

assert testList.get(1) == 2

assert testList.get(0) == 1

##############################################################
#["remove", 0]

testList = LinkedList()
testList.remove(0) == False
print('all tests ok')
