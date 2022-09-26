//  LIFO Stack implementation using a Python list as
//  its underlying storage.
class StackADT {
  stack = [];

  push(item) {
    this.stack.push(item);
  }
  pop() {
    if (this.is_empty()) {
      throw new Error("stack is empty");
    } else {
      this.stack.pop();
    }
  }
  peek() {
    if (this.is_empty()) {
      throw new Error("stack is empty");
    } else {
      return this.stack[this.stack.length - 1];
    }
  }
  is_empty() {
    return this.stack.length === 0;
  }
  size() {
    return this.stack.length;
  }
}

const Stack = new StackADT();

Stack.push("S");
Stack.push("T");
Stack.push("A");
Stack.push("C");
Stack.push("K");

Stack.pop();
Stack.pop();
Stack.pop();
Stack.pop();
Stack.pop();

//  FIFO Queue implementation using a Python list as
//  its underlying storage.
class QueueADT {
  constructor() {
    this.queue = [];
  }

  enqueue(item) {
    this.queue.unshift(item);
  }
  dequeue() {
    if (this.is_empty()) {
      throw new Error("queue is empty");
    } else {
      this.queue.pop();
    }
  }
  peek() {
    if (this.is_empty()) {
      throw new Error("queue is empty");
    } else {
      return this.queue[this.queue.length - 1];
    }
  }
  is_empty() {
    return this.queue.length === 0;
  }
  size() {
    return this.queue.length;
  }
}

const Queue = new QueueADT();

Queue.enqueue("Q");
Queue.enqueue("U");
Queue.enqueue("E");
Queue.enqueue("U");
Queue.enqueue("E");

Queue.dequeue();

class Node {
  constructor(e) {
    this.element = e;
    this.next = null;
  }
}

class LLStackADT {
  constructor() {
    this._size = 0;
    this.head = null;
  }
  push(item) {
    const newest = new Node(item);
    newest.next = this.head;
    this.head = newest;
    this._size += 1;
  }
  pop() {
    if (this._size === 0) {
      throw new Error("Stack is empty");
    } else {
      const elementToReturn = this.head.element;
      this.head = this.head.next;
      this._size -= 1;

      return elementToReturn;
    }
  }
  peek() {
    if (this._size === 0) {
      throw new Error("Stack is empty");
    } else {
      return this.head.element;
    }
  }
  is_empty() {
    return this._size === 0;
  }
  size() {
    return this._size;
  }
  find(e) {
    const findElement = null;
    let activeHead = { ...this.head };
    if (this.is_empty()) return findElement;
    for (let i = 0; i < this._size; i++) {
      if (activeHead.element === e) {
        findElement = e;
        break;
      } else activeHead = activeHead.next;
    }
    return findElement;
  }
}

const LLS = new LLStackADT();
// each element in the LLS is a Node instance with 2 properties 1. element and 2. next;
LLS.push("K");
LLS.push("C");
LLS.push("A");
LLS.push("T");
LLS.push("S");

console.log(LLS.head);

class LLQADT {
  constructor() {
    this._size = 0;
    this.head = null;
    this.tail = null;
  }
  enqueue(item) {
    const newest = new Node(item);
    if (this.is_empty()) {
      this.head = newest;
    }
    this.tail.next = this.tail;
    this.tail = newest;
    this._size += 1;
  }
  dequeue() {
    if (this.is_empty()) {
      throw new Error("Stack is empty");
    } else {
      const elementToReturn = this.head.element;
      this.head = this.head.next;
      this._size -= 1;
      if (this.is_empty()) {
        this.tail = null;
      }

      return elementToReturn;
    }
  }
  peek() {
    if (this.is_empty()) {
      throw new Error("Stack is empty");
    } else {
      return this.tail.element;
    }
  }
  is_empty() {
    return this._size === 0;
  }
  size() {
    return this._size;
  }
  find(e) {
    const findElement = null;
    let activeHead = { ...this.tail };
    if (this.is_empty()) return findElement;
    for (let i = 0; i < this._size; i++) {
      if (activeHead.element === e) {
        findElement = e;
        break;
      } else activeHead = activeHead.next;
    }
    return findElement;
  }
}
