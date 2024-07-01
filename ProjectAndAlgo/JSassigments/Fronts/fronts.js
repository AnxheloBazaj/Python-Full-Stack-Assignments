class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }

    addFront(value) {
        const newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head;
    }

    removeFront() {
        if (!this.head) {
            return null;
        }
        const oldHead = this.head;
        this.head = this.head.next;
        return this.head;
    }

    front() {
        return this.head ? this.head.data : null;
    }
    display() {
        let current = this.head;
        let result = '';
        while (current) {
            result += current.data + ' -> ';
            current = current.next;
        }
        console.log(result + 'null');
    }
}

// Test the implementation
const SLL1 = new SLL();

console.log(SLL1.addFront(18));
console.log(SLL1.addFront(5));
console.log(SLL1.addFront(73));

SLL1.display();

console.log(SLL1.removeFront());
SLL1.display();

console.log(SLL1.removeFront());
SLL1.display();

console.log(SLL1.front());

console.log(SLL1.removeFront());
console.log(SLL1.front());