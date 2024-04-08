//version 1
for (var i = 100; i >= 0; i--) {
    if (i % 3 == 0) {
        console.log(i)
    }
}

console.log()

//version 2
for (var i = 99; i >= 0; i -= 3) {
    console.log(i)
}