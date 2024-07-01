class SLL {
    constructor() {
        this.head = null;
    }

    display() {
        let result = '';
        let runner = this.head;
        
        while (runner !== null) {
            result += runner.data;
            if (runner.next !== null) {
                result += ', ';
            }
            runner = runner.next;
        }
        
        return result;
    }
}