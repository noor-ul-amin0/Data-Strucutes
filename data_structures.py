import copy

# LIFO Stack implementation using a Python list as
# its underlying storage.


class StackADT:
    # Create an empty stack.
    def __init__(self):
        self.data = []

    # Add element e to the top of the stack
    def push(self, e):
        self.data.append(e)

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        else:
            return self.data[-1]

    # Return True if the stack is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the stack.
    def size(self):
        return len(self.data)


S = StackADT()
S.push("S")
S.push("T")
S.push("A")
S.push("C")
S.push("K")

# print('This is StackADT:', S.data)

# FIFO Queue implementation using a Python list as
# its underlying storage.


class QueueADT:
    # Create an empty queue.
    def __init__(self):
        self.data = []

    # Add element e to the back of the queue
    def enqueue(self, e):
        self.data.insert(0, e)

    # Remove and return the element from the front of the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data.pop()

    # Return (but do not remove) the first element of the
    # queue. Raise exception if the queue is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        else:
            return self.data[-1]

    # Return True if the queue is empty.
    def is_empty(self):
        return len(self.data) == 0

    # Return the number of elements in the queue.
    def size(self):
        return len(self.data)


Q = QueueADT()
Q.enqueue("Q")
Q.enqueue("U")
Q.enqueue("E")
Q.enqueue("U")
Q.enqueue("E")


# print('This is QueueADT:', Q.data)


# LIFO Stack implementation using a linked list
# as its underlying storage
class LinkedListStack:
    # ----------------------Nested Node Class ----------------------

    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e
            self.next = None   # reference to the next Node

# ---------------------- stack methods -------------------------
    # Create an empty stack
    def __init__(self):
        self._size = 0
        # reference to head node (top of stack)
        self.head = None

    # Add element e to the top of the stack.
    def push(self, e):
        # New node inserted at Head
        newest = self.Node(e)
        newest.next = self.head
        self.head = newest
        self._size += 1

    # Remove and return the element from the top of the stack
    # (i.e., LIFO). Raise exception if the stack is empty.
    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1

        return elementToReturn

    # Return (but do not remove) the element at the top of
    # the stack. Raise Empty exception if the stack is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        return self.head.element

    # Return True if the stack is empty.
    def is_empty(self):
        return self._size == 0

    # Return the number of elements in the stack.
    def size(self):
        return self._size

    def find(self, e):
        findElement = None
        activeHead = copy.deepcopy(self.head)
        if self.is_empty():
            return findElement
        for _ in range(self._size):
            if activeHead.element == e:
                findElement = e
                break
            else:
                activeHead = activeHead.next
        return findElement


LLS = LinkedListStack()
#  each element in the LLS is a Node instance with 2 properties 1. element and 2. next;
LLS.push("K")
LLS.push("C")
LLS.push("A")
LLS.push("T")
LLS.push("S")

# print("This is Stack DS using LinkedList Active Head's element:", LLS.head.element)
# print("This is Stack DS using LinkedList Ative Head's next Node:",
#       LLS.head.next.element)


# FIFO Queue implementation using a linked list
# as its underlying storage


class LinkedListQueue:
  # ----------------------Nested Node Class ----------------------
    # This Node class stores a piece of data (element) and
    # a reference to the Next node in the Linked List
    class Node:
        def __init__(self, e):
            self.element = e
            self.next = None   # reference to the next Node

# ---------------------- queue methods -------------------------
    # create an empty queue
    def __init__(self):
        self._size = 0
        self.head = None
        self.tail = None

    # Add element e to the back of the queue.
    def enqueue(self, e):
        newest = self.Node(e)

        if self.is_empty():
            self.head = newest
        else:
            self.tail.next = newest
        self.tail = newest
        self._size += 1

 # | head -> { element: 'A' , next: None} <- tail |
 # | head -> [Node A]  { element: 'B' , next:} <- tail |
 # |
    # Remove and return the first element from the queue
    # (i.e., FIFO). Raise exception if the queue is empty.
    def dequeue(self):
        if self.is_empty():
            raise IndexError('Queue is empty')

        elementToReturn = self.head.element
        self.head = self.head.next
        self._size -= 1
        if self.is_empty():
            self.tail = None

        return elementToReturn

    # Return (but do not remove) the element at the front of
    # the queue. Raise exception if the queue is empty.
    def peek(self):
        if self.is_empty():
            raise IndexError('Queue is empty')
        return self.head.element

    # Return True if the queue is empty.
    def is_empty(self):
        return self._size == 0

    # Return the number of elements in the queue.
    def size(self):
        return self._size


LLQ = LinkedListQueue()
LLQ.enqueue("L")
LLQ.enqueue("L")
LLQ.enqueue("Q")
LLQ.enqueue("U")
LLQ.enqueue("E")
LLQ.enqueue("U")
LLQ.enqueue("E")


# Binary Search Tree Python implementation
class BinarySearchTree:
  # ----------------------Nested Node Class ----------------------
    # This Node class stores a piece of data (element) and
    # a reference to it's left and right children
    class Node:
        __slots__ = 'element', 'left', 'right'

        def __init__(self, e):
            self.element = e
            self.left = None  # reference to the left Child
            self.right = None  # reference to the right Child

# ---------------------- BST methods -------------------------
    # create an empty BST
    def __init__(self):
        self.root = None
        self._size = 0

    # Recursively add element e to the tree
    def add_node(self, root, e):
        # If no root exists, set new Node as root
        if self.root == None:
            self.root = self.Node(e)
            self._size += 1
            return

        if e < root.element:
            if root.left == None:
                root.left = self.Node(e)
                self._size += 1
            else:
                self.add_node(root.left, e)
        else:
            if root.right == None:
                root.right = self.Node(e)
                self._size += 1
            else:
                self.add_node(root.right, e)

    # Recursively prints the values in tree in
    # ascending order.
    def traverse_in_order(self, root):
        if root != None:
            self.traverse_in_order(root.left)
            print(root.element, end=" ")
            self.traverse_in_order(root.right)

    # Returns the largest number of edges in a path from
    # root node of tree to a leaf node.
    def height(self, root):
        if root == None:
            return 0

        return max(self.height(root.left),
                   self.height(root.right)) + 1

    # Returns True if no elements found in tree,
    # else returns False
    def is_empty(self):
        return self._size == 0

    # Returns the number of elements in tree
    def size(self):
        return self._size


t = BinarySearchTree()
t.is_empty()            # True
t.add_node(t.root, 56)
t.add_node(t.root, 13)
t.add_node(t.root, 1)
t.add_node(t.root, 6)
t.add_node(t.root, 3)
t.add_node(t.root, 67)
t.add_node(t.root, 3)
t.add_node(t.root, 45)
t.add_node(t.root, 99)
t.add_node(t.root, 2)
t.is_empty()            # False
t.size()                # 10
t.height(t.root)        # 6
t.traverse_in_order(t.root)  # 1 2 3 3 6 13 45 56 67 99
