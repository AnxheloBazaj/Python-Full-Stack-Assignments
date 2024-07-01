// Push Front
function pushFront(arr, val) {
    for (let i = arr.length; i > 0; i--) {
        arr[i] = arr[i - 1];
    }
    arr[0] = val;
    return arr;
}

// Pop Front
function popFront(arr) {
    if (arr.length === 0) return undefined;
    let firstVal = arr[0];
    for (let i = 0; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
    }
    arr.length--;
    console.log(arr);
    return firstVal;
}

// Insert At
function insertAt(arr, index, val) {
    for (let i = arr.length; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    arr[index] = val;
    return arr;
}

// Remove At
function removeAt(arr, index) {
    if (index < 0 || index >= arr.length) return undefined;
    let removedVal = arr[index];
    for (let i = index; i < arr.length - 1; i++) {
        arr[i] = arr[i + 1];
    }
    arr.length--;
    console.log(arr);
    return removedVal;
}

// Swap Pairs
function swap(arr) {
    for (let i = 0; i < arr.length - 1; i += 2) {
        let temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i + 1] = temp;
    }
    return arr;
}

// Remove Duplicates
function removeDupes(arr) {
    if (arr.length <= 1) return arr;
    let index = 1;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] !== arr[index - 1]) {
            arr[index] = arr[i];
            index++;
        }
    }
    arr.length = index;
    return arr;
}

// Test cases
console.log(pushFront([5,7,2,3], 8));
console.log(pushFront([99], 7));

console.log(popFront([0,5,10,15]));
console.log(popFront([4,5,7,9]));

console.log(insertAt([100,200,5], 2, 311));
console.log(insertAt([9,33,7], 1, 42));

console.log(removeAt([1000,3,204,77], 1));
console.log(removeAt([8,20,55,44,98], 3));

console.log(swap([1,2,3,4]));
console.log(swap(["Anxhelo",true,42]));

console.log(removeDupes([-2,-2,3.14,5,5,10]));
console.log(removeDupes([9,19,19,19,19,19,29]));