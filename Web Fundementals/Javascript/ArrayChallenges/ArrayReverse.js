function reverse(arr) {
    const arr2 = []
    for (var i = arr.length; i > 0; i--) {
        arr2.push(arr[i - 1])
    }
    return arr2;
}

var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result,); // we expect back ["e", "d", "c", "b", "a"]